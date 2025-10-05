"""
Trasy gry - tworzenie sesji, zarządzanie stanem, wydarzenia
"""
from flask import Blueprint, request, jsonify
import logging
from models import db, GameSession, LifeEvent
from routes.auth import get_current_user
import copy
import sys
import os

# Add parent directory to path for Docker
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.ai_events import AIEventGenerator
from utils.hardcoded_events import (
    get_event_for_session,
    get_random_pension_tip,
    EDUCATION_EVENTS,
    check_event_requirements,
)
from utils.pension_calculator import PensionCalculator
from config import Config
import random

logger = logging.getLogger(__name__)

game_bp = Blueprint('game', __name__, url_prefix='/api/game')

# Inicjalizuj AI generator (lazy loading)
ai_generator = None
pension_calc = PensionCalculator()


def get_ai_generator():
    """Lazy loading AI generatora"""
    global ai_generator
    if ai_generator is None and Config.ANTHROPIC_API_KEY:
        try:
            ai_generator = AIEventGenerator(Config.ANTHROPIC_API_KEY)
        except Exception as e:
            logger.error(f"Nie można zainicjalizować AI generatora: {e}")
    return ai_generator


def advance_session_years(session, years):
    """Przesuwa stan sesji o podaną liczbę lat, zachowując logikę ekonomiczną"""
    turned_23 = False

    for _ in range(max(0, years)):
        if session.game_over:
            break

        session.age += 1

        if session.age == 23 and session.monthly_costs == 0:
            session.monthly_costs = 1500
            turned_23 = True

        update_life_stage(session)

        if session.income == -999999 or session.income < 0 or not session.has_job:
            session.income = 0

        yearly_income = 0
        if session.has_job and session.income > 0:
            # ==============================================================
            # ZUS PENSION CONTRIBUTIONS - POLISH LAW (simplified for game)
            # ==============================================================
            # Real Polish ZUS rules:
            # 1. Umowa o pracę (UoP): MANDATORY 19.52% of gross salary
            #    - 9.76% paid by employee + 9.76% by employer
            #    - Both parts go to individual pension account
            #    - Employer handles everything automatically
            #
            # 2. Umowa zlecenie (civil contract):
            #    - If main job: partial contributions
            #    - If additional job: often zero contributions
            #    - Game simplification: 50% of UoP rate
            #
            # 3. B2B (Działalność gospodarcza / self-employed):
            #    - Can choose ZUS basis (minimum ~1800 PLN in 2025)
            #    - Often pay minimal contributions to save money
            #    - Game simplification: 30% of income as basis
            #
            # Higher contributions = higher pension!
            # ==============================================================
            
            if session.type_employment in ['umowa o pracę', 'UoP']:
                # Full pension contributions for employment contract
                monthly_contribution = pension_calc.calculate_monthly_contribution(session.income)
                session.zus_contributions += monthly_contribution * 12
            elif session.type_employment == 'zlecenie':
                # Partial contributions for civil contract (simplified: 50% of full rate)
                monthly_contribution = pension_calc.calculate_monthly_contribution(session.income) * 0.5
                session.zus_contributions += monthly_contribution * 12
            elif session.type_employment == 'B2B' and session.income >= 6000:
                # B2B: contributions only if income is high enough (simplified model)
                # Usually B2B pays less to ZUS or declares lower base
                monthly_contribution = pension_calc.calculate_monthly_contribution(session.income * 0.3)  # 30% of income as declared base
                session.zus_contributions += monthly_contribution * 12
            # Other employment types don't contribute to pension
            
            yearly_income = session.income * 12

        yearly_costs = session.monthly_costs * 12
        session.savings += yearly_income - yearly_costs

        if session.savings < -5000:
            session.savings = -5000

        apply_aging_effects(session)
        auto_retire_if_eligible(session)
        check_game_over(session)

        if session.game_over:
            break

    return turned_23


@game_bp.route('/session/new', methods=['POST'])
def create_session():
    """
    Tworzy nową sesję gry
    
    Oczekuje JSON: { "sex": "male/female", "name": "..." (opcjonalnie) }
    """
    try:
        user = get_current_user()
        if not user:
            return jsonify({'error': 'Wymagana autoryzacja'}), 401
        
        data = request.get_json() or {}
        
        # Utwórz nową sesję
        session = GameSession(
            user_id=user.id,
            sex=data.get('sex', 'male'),
            age=18,
            life_stage='edukacja',
            student=True,
            completed_education=['podstawowe'],  # Wszyscy zaczynają z podstawowym
            completed_events=[],  # Pusta lista wydarzeń jednorazowych
            chosen_options_history=[],  # Pusta historia wyborów dla AI
            has_apartment=False,
            has_job=False,
            job_count=0,
            monthly_costs=0  # Brak kosztów do 23 roku życia
        )
        
        db.session.add(session)
        db.session.commit()
        
        logger.info(f"Utworzono nową sesję gry dla użytkownika {user.email}")
        
        return jsonify({
            'message': 'Sesja gry utworzona',
            'session': session.to_dict()
        }), 201
        
    except Exception as e:
        logger.error(f"Błąd tworzenia sesji: {e}")
        db.session.rollback()
        return jsonify({'error': 'Błąd tworzenia sesji gry'}), 500


@game_bp.route('/session/<int:session_id>', methods=['GET'])
def get_session(session_id):
    """Pobiera aktualny stan sesji gry"""
    try:
        user = get_current_user()
        if not user:
            return jsonify({'error': 'Wymagana autoryzacja'}), 401
        
        session = GameSession.query.filter_by(id=session_id, user_id=user.id).first()
        if not session:
            return jsonify({'error': 'Nie znaleziono sesji'}), 404
        
        # Oblicz emeryturę
        pension_info = pension_calc.calculate_pension(
            session.zus_contributions,
            session.age,
            session.sex
        )
        
        response = session.to_dict()
        response['pension_info'] = pension_info
        
        return jsonify(response), 200
        
    except Exception as e:
        logger.error(f"Błąd pobierania sesji: {e}")
        return jsonify({'error': 'Błąd pobierania sesji'}), 500


@game_bp.route('/session/<int:session_id>/advance', methods=['POST'])
def advance_time(session_id):
    """
    Przesuwa czas o 1 rok i aktualizuje stan gry
    """
    try:
        user = get_current_user()
        if not user:
            return jsonify({'error': 'Wymagana autoryzacja'}), 401
        
        session = GameSession.query.filter_by(id=session_id, user_id=user.id).first()
        if not session:
            return jsonify({'error': 'Nie znaleziono sesji'}), 404
        
        if session.game_over:
            return jsonify({'error': 'Gra zakończona'}), 400
        
        turned_23 = advance_session_years(session, 1)
        
        db.session.commit()
        
        logger.info(f"Sesja {session_id}: wiek zwiększony do {session.age}")
        
        return jsonify({
            'message': 'Rok przesunięty',
            'session': session.to_dict(),
            'turned_23': turned_23  # Flag informujący że gracz skończył 23 lata
        }), 200
        
    except Exception as e:
        logger.error(f"Błąd przesuwania czasu: {e}")
        db.session.rollback()
        return jsonify({'error': 'Błąd przesuwania czasu'}), 500


@game_bp.route('/session/<int:session_id>/action', methods=['POST'])
def perform_quick_action(session_id):
    """Wykonuje szybkie działanie dostępne z poziomu interfejsu"""
    try:
        user = get_current_user()
        if not user:
            return jsonify({'error': 'Wymagana autoryzacja'}), 401

        session = GameSession.query.filter_by(id=session_id, user_id=user.id).first()
        if not session:
            return jsonify({'error': 'Nie znaleziono sesji'}), 404

        if session.game_over:
            return jsonify({'error': 'Gra zakończona'}), 400

        data = request.get_json() or {}
        action_type = data.get('action_type')

        quick_actions = {
            'go_out': {
                'label': 'Wyjście na miasto',
                'message': 'Poszliście ze znajomymi na miasto. Trochę drogo, ale było warto!',
                'impacts': {
                    'savings': -200,
                    'happiness': 1,
                    'stress_level': -1,
                    'social_connections': 0.5,
                    'work_life_balance': 0.5
                },
                'trigger_advice': True
            },
            'medical_checkup': {
                'label': 'Badanie kontrolne',
                'message': 'Umówiłeś się na badania profilaktyczne - zdrowie najważniejsze!',
                'impacts': {
                    'savings': -300,
                    'health': 2,
                    'mental_health': 0.5,
                    'stress_level': -0.5
                },
                'trigger_advice': True
            },
            'retire_now': {
                'label': 'Przejdź na emeryturę',
                'message': 'Zdecydowałeś się na przejście na wcześniejszą emeryturę.',
                'impacts': {
                    'has_job': False,
                    'income': -999999,
                    'life_stage': 'retirement',
                    'stress_level': -1,
                    'work_life_balance': 1,
                    'financial_security': -0.5
                },
                'trigger_advice': True,
                'finishes_game': True
            }
        }

        if action_type not in quick_actions:
            return jsonify({'error': 'Nieznane działanie'}), 400

        action = quick_actions[action_type]

        savings_delta = action.get('impacts', {}).get('savings', 0)
        if session.savings + savings_delta < -5000:
            return jsonify({'error': 'Masz za mało środków na tę decyzję'}), 400

        # Zastosuj wpływy działania
        apply_choice_impacts(session, action.get('impacts', {}))

        response_payload = {
            'message': action.get('message'),
            'action_type': action_type
        }

        if action.get('finishes_game'):
            session.game_over = True
            session.is_active = False
            session.game_over_reason = 'Zakończyłeś karierę i przeszedłeś na emeryturę'
            # Po przejściu na emeryturę nie ma pracy
            session.has_job = False
            session.income = 0

        db.session.commit()

        response_payload['session'] = session.to_dict()
        response_payload['trigger_advice'] = action.get('trigger_advice', False)
        response_payload['game_over'] = session.game_over

        return jsonify(response_payload), 200

    except Exception as e:
        logger.error(f"Błąd wykonywania działania {session_id}: {e}")
        db.session.rollback()
        return jsonify({'error': 'Błąd wykonywania działania'}), 500


@game_bp.route('/session/<int:session_id>/event', methods=['GET'])
def get_event(session_id):
    """
    Generuje nowe wydarzenie życiowe dla gracza
    """
    try:
        user = get_current_user()
        if not user:
            return jsonify({'error': 'Wymagana autoryzacja'}), 401
        
        session = GameSession.query.filter_by(id=session_id, user_id=user.id).first()
        if not session:
            return jsonify({'error': 'Nie znaleziono sesji'}), 404
        
        completed_events = list(session.completed_events or [])
        force_education_event = 'education_intro' not in completed_events
        
        logger.info(f"DEBUG get_event: age={session.age}, completed_events={completed_events}, force_education={force_education_event}, completed_education={session.completed_education}")

        event_data = None
        event_type = 'hardcoded'

        # DIRTY FIX: Force technical school at age 18
        if session.age == 18 and 'education_intro' not in completed_events:
            logger.info("Age 18 detected - forcing technical_school event")
            event_data = copy.deepcopy(EDUCATION_EVENTS['technical_school'])
            event_data['event_key'] = 'technical_school'
        elif force_education_event:
            logger.info(f"Forcing education event, checking {len(EDUCATION_EVENTS)} education templates")
            for event_key, template in EDUCATION_EVENTS.items():
                candidate = copy.deepcopy(template)
                candidate['event_key'] = event_key
                requirements_met = check_event_requirements(candidate, session)
                logger.info(f"  - {event_key}: requirements_met={requirements_met}")
                if requirements_met:
                    event_data = candidate
                    logger.info(f"Selected education event: {event_key}")
                    break
            
            if not event_data:
                logger.warning(f"No education event matched requirements! Session: age={session.age}, completed_education={session.completed_education}")

        if not event_data:
            # 50% szansa na hardcoded event, 50% na AI (chyba że wymuszamy szkołę)
            use_ai = not force_education_event and (random.random() > 0.5)

            hardcoded_template = get_event_for_session(session)
            if hardcoded_template:
                event_data = copy.deepcopy(hardcoded_template)

            if use_ai and get_ai_generator():
                try:
                    event_data = get_ai_generator().generate_life_event(session.to_dict())
                    event_type = 'ai_generated'
                except Exception as e:
                    logger.warning(f"AI generation failed, using hardcoded: {e}")
                    if not event_data:
                        event_type = 'hardcoded'
                        event_data = copy.deepcopy(get_event_for_session(session))
        
        if not event_data:
            return jsonify({'error': 'Brak dostępnych wydarzeń'}), 404

        # Dodaj event_key do choices jeśli istnieje
        if 'event_key' in event_data:
            for choice in event_data.get('choices', []):
                choice['event_key'] = event_data['event_key']
        
        # Zapisz wydarzenie
        life_event = LifeEvent(
            session_id=session.id,
            event_type=event_type,
            event_name=event_data['event_name'],
            description=event_data['description'],
            choices=event_data['choices'],
            age_occurred=session.age
        )
        
        db.session.add(life_event)
        db.session.commit()
        
        logger.info(f"Wygenerowano wydarzenie: {event_data['event_name']}")
        
        return jsonify({
            'event': life_event.to_dict()
        }), 200
        
    except Exception as e:
        logger.error(f"Błąd generowania wydarzenia: {e}")
        db.session.rollback()
        return jsonify({'error': 'Błąd generowania wydarzenia'}), 500


@game_bp.route('/event/<int:event_id>/choose', methods=['POST'])
def make_choice(event_id):
    """
    Gracz dokonuje wyboru w wydarzeniu
    
    Oczekuje JSON: { "choice_index": 0 }
    """
    try:
        user = get_current_user()
        if not user:
            return jsonify({'error': 'Wymagana autoryzacja'}), 401
        
        data = request.get_json()
        if 'choice_index' not in data:
            return jsonify({'error': 'Wymagany choice_index'}), 400
        
        choice_index = data['choice_index']
        
        # Znajdź wydarzenie
        event = LifeEvent.query.get(event_id)
        if not event:
            return jsonify({'error': 'Nie znaleziono wydarzenia'}), 404
        
        session = GameSession.query.filter_by(id=event.session_id, user_id=user.id).first()
        if not session:
            return jsonify({'error': 'Brak dostępu do tej sesji'}), 403
        
        # Sprawdź czy wybór jest poprawny
        if choice_index < 0 or choice_index >= len(event.choices):
            return jsonify({'error': 'Nieprawidłowy indeks wyboru'}), 400
        
        # Zapisz wybór
        event.player_choice = choice_index
        chosen_option = event.choices[choice_index]
        
        # Zastosuj wpływ wyboru
        apply_choice_impacts(session, chosen_option.get('impacts', {}))
        
        # Dodaj wybór do historii dla AI (tylko tekst wyboru)
        choice_history = session.chosen_options_history or []
        choice_text = chosen_option.get('text', '')
        if choice_text and choice_text not in choice_history:
            choice_history.append(choice_text)
            # Zachowaj tylko ostatnie 20 wyborów żeby nie robić historii za długiej
            session.chosen_options_history = choice_history[-20:]
        
        # Jeśli wydarzenie ma flagę show_once, dodaj do completed_events
        if event.event_type == 'hardcoded':
            # Pobierz event_key z wyboru lub spróbuj znaleźć w impacts
            event_key = chosen_option.get('event_key')
            if not event_key:
                # Spróbuj znaleźć event_key w nazwie wydarzenia lub opisie
                event_name = event.event_name.lower()
                if 'pierwsza praca' in event_name or 'first job' in event_name:
                    event_key = 'first_job'
                elif 'szkoła zawodowa' in event_name or 'technical school' in event_name:
                    event_key = 'technical_school'
                elif 'studia' in event_name or 'university' in event_name:
                    event_key = 'university'
                elif 'potrzebujesz mieszkania' in event_name or 'need apartment' in event_name:
                    event_key = 'need_apartment'

            record_completed_event(session, event_key)
            
            # Zaznacz że edukacja została już wybrana (blokuje kolejne szkoły)
            if event_key in EDUCATION_EVENTS:
                record_completed_event(session, 'education_intro')
        
        # Sprawdź czy wybór ma skip_years (przeskocz lata)
        raw_skip_years = chosen_option.get('skip_years', 0)
        logger.info(f"DEBUG: chosen_option keys: {chosen_option.keys()}, skip_years raw value: {raw_skip_years}")
        
        # DIRTY FIX: If age is 18 and it's a school event, force skip years
        if session.age == 18 and event.event_type == 'hardcoded':
            event_name_lower = event.event_name.lower()
            if 'studia' in event_name_lower or 'university' in event_name_lower:
                raw_skip_years = 5
                logger.info(f"Age 18 + university detected - forcing skip_years=5")
            elif 'szkoła' in event_name_lower or 'technical' in event_name_lower or 'zawodowa' in event_name_lower:
                raw_skip_years = 2
                logger.info(f"Age 18 + technical school detected - forcing skip_years=2")
        
        try:
            skip_years = int(raw_skip_years or 0)
        except (TypeError, ValueError):
            logger.warning(f"Could not parse skip_years: {raw_skip_years}")
            skip_years = 0
        years_skipped_triggered_23 = False
        if skip_years > 0:
            logger.info(f"Przeskakuję {skip_years} lat z powodu wydarzenia: {event.event_name}")
            years_skipped_triggered_23 = advance_session_years(session, skip_years)
        else:
            logger.info(f"No skip_years for this choice (skip_years={skip_years})")
        
        db.session.commit()
        
        logger.info(f"Gracz wybrał opcję {choice_index} w wydarzeniu {event.event_name}")
        
        return jsonify({
            'message': 'Wybór zapisany',
            'chosen_option': chosen_option,
            'session': session.to_dict(),
            'turned_23': years_skipped_triggered_23
        }), 200
        
    except Exception as e:
        logger.error(f"Błąd zapisywania wyboru: {e}")
        db.session.rollback()
        return jsonify({'error': 'Błąd zapisywania wyboru'}), 500


def update_life_stage(session):
    """Aktualizuje etap życia na podstawie wieku"""
    age = session.age
    
    if age < 25:
        session.life_stage = 'edukacja'
    elif age < 35:
        session.life_stage = 'early_career'
    elif age < 55:
        session.life_stage = 'mid_career'
    elif age < 65:
        session.life_stage = 'late_career'
    else:
        session.life_stage = 'retirement'


def calculate_monthly_expenses(session):
    """Oblicza miesięczne wydatki na podstawie sytuacji życiowej"""
    base_expenses = 2000  # Podstawowe koszty życia
    
    # Dodaj koszty dzieci
    base_expenses += session.children * 1000
    
    # Dodaj koszty związane z statusem
    if session.marital_status in ['zamężna', 'żonaty']:
        base_expenses += 500
    
    # Studenci mają mniejsze wydatki
    if session.student:
        base_expenses *= 0.7
    
    return base_expenses


def apply_aging_effects(session):
    """Stosuje naturalne efekty starzenia się"""
    # Zdrowie fizyczne pogarsza się z wiekiem
    if session.age > 40:
        session.health = max(1, session.health - 0.1)
    
    # Po 60 roku życia bardziej
    if session.age > 60:
        session.health = max(1, session.health - 0.2)


def check_game_over(session):
    """Sprawdza warunki zakończenia gry"""
    # Śmierć z powodu zdrowia
    if session.health <= 0:
        session.game_over = True
        session.game_over_reason = "Śmierć z powodu złego zdrowia"
        session.is_active = False
    
    # Maksymalny wiek
    if session.age >= 90:
        session.game_over = True
        session.game_over_reason = "Naturalna śmierć - długie życie!"
        session.is_active = False


def apply_choice_impacts(session, impacts):
    """Aplikuje wpływ wyboru na statystyki sesji z limitem długu"""
    MAX_DEBT = -5000  # Maksymalny dług: -5000 zł
    
    # Obsługa specjalnego pola add_to_completed (dodaje wykształcenie do listy)
    if 'add_to_completed' in impacts:
        completed = session.completed_education or []
        if impacts['add_to_completed'] not in completed:
            completed.append(impacts['add_to_completed'])
            session.completed_education = completed
        del impacts['add_to_completed']  # Usuń z impacts żeby nie próbować ustawić normalnie
    
    # VALIDATION: If getting a job, must have type_employment
    if impacts.get('has_job') is True and 'type_employment' not in impacts:
        logger.warning("Event gives job but no type_employment specified! Defaulting to 'UoP'")
        impacts['type_employment'] = 'UoP'  # Default to full employment contract
    
    # If losing job, clear type_employment
    if impacts.get('has_job') is False:
        impacts['type_employment'] = ''
        impacts['work'] = 'bezrobotny'
    
    for key, value in impacts.items():
        if hasattr(session, key):
            current = getattr(session, key)
            
            # Boolean - konwertuj wartość na boolean
            if isinstance(current, bool):
                # Konwertuj różne typy na boolean
                if isinstance(value, bool):
                    setattr(session, key, value)
                elif isinstance(value, (int, float)):
                    # Traktuj 0 jako False, wszystko inne jako True
                    setattr(session, key, bool(value))
                elif isinstance(value, str):
                    # Traktuj "true", "1", "yes" jako True
                    setattr(session, key, value.lower() in ['true', '1', 'yes'])
                else:
                    setattr(session, key, bool(value))
            # Numeryczne - dodaj wartość
            elif isinstance(current, (int, float)):
                # Specjalne wartości -999999 oznaczają "wyzeruj to pole"
                if value == -999999:
                    new_value = 0
                else:
                    new_value = current + value
                
                # Specjalna obsługa savings - nie może spaść poniżej -5000 zł
                if key == 'savings':
                    if new_value < MAX_DEBT:
                        logger.warning(f"Próba przekroczenia maksymalnego długu. Oszczędności: {new_value}, Limit: {MAX_DEBT}")
                        new_value = MAX_DEBT  # Ogranicz do maksymalnego długu
                    setattr(session, key, new_value)
                # Specjalna obsługa income - może być wyzerowany
                elif key == 'income':
                    new_value = max(0, new_value)  # Income nie może być ujemny
                    setattr(session, key, new_value)
                # Ogranicz do sensownych zakresów dla innych statystyk
                elif key in ['health', 'mental_health', 'happiness', 'stress_level',
                            'physical_health', 'career_satisfaction', 'work_life_balance',
                            'relationship_quality', 'personal_growth', 'self_esteem',
                            'life_purpose', 'social_connections', 'free_time', 'financial_security']:
                    new_value = max(0, min(10, new_value))
                    setattr(session, key, new_value)
                else:
                    setattr(session, key, new_value)
            # Stringi - ustaw nową wartość
            elif isinstance(current, str):
                setattr(session, key, value)


def auto_retire_if_eligible(session):
    """Automatycznie zakańcza grę po osiągnięciu wieku emerytalnego"""
    if session.game_over:
        return

    retirement_age = 65 if (session.sex or '').lower() == 'male' else 60
    if session.age < retirement_age:
        return

    session.life_stage = 'retirement'
    session.has_job = False
    session.income = 0
    session.work = 'emeryt'
    session.game_over = True
    session.is_active = False
    session.game_over_reason = 'Osiągnąłeś ustawowy wiek emerytalny'


def record_completed_event(session, event_key):
    """Dodaje jednorazowe wydarzenie do listy ukończonych (bez duplikatów)"""
    if not event_key:
        return

    completed = list(session.completed_events or [])
    if event_key not in completed:
        completed.append(event_key)

    seen = set()
    session.completed_events = [ek for ek in completed if not (ek in seen or seen.add(ek))]
