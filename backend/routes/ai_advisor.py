"""
Trasy dla AI Doradcy - Wujek Dobra Rada
"""
from flask import Blueprint, request, jsonify
import logging
from models import GameSession
from routes.auth import get_current_user
from utils.wujek_rada import WujekDobraRada
from config import Config

logger = logging.getLogger(__name__)

advisor_bp = Blueprint('advisor', __name__, url_prefix='/api/advisor')

# Lazy loading
wujek = None


def get_wujek():
    """Lazy loading Wujka Dobrej Rady"""
    global wujek
    if wujek is None and Config.ANTHROPIC_API_KEY:
        try:
            wujek = WujekDobraRada(Config.ANTHROPIC_API_KEY)
        except Exception as e:
            logger.error(f"Nie można zainicjalizować Wujka: {e}")
    return wujek


@advisor_bp.route('/advice/<int:session_id>', methods=['GET'])
def get_advice(session_id):
    """
    Pobiera radę od Wujka Dobrej Rady dla danej sesji
    """
    try:
        user = get_current_user()
        if not user:
            return jsonify({'error': 'Wymagana autoryzacja'}), 401
        
        session = GameSession.query.filter_by(id=session_id, user_id=user.id).first()
        if not session:
            return jsonify({'error': 'Nie znaleziono sesji'}), 404
        
        # Sprawdź czy Wujek jest dostępny
        wujek_instance = get_wujek()
        if not wujek_instance:
            return jsonify({
                'advice': 'Wujek Dobra Rada jest chwilowo niedostępny. Skonfiguruj ANTHROPIC_API_KEY.'
            }), 200
        
        # Pobierz ostatnią decyzję z parametru query (opcjonalnie)
        recent_decision = request.args.get('recent_decision', None)
        
        # Generuj radę
        advice = wujek_instance.get_advice(
            session.to_dict(),
            recent_decision=recent_decision
        )
        
        logger.info(f"Wygenerowano radę dla sesji {session_id}")
        
        return jsonify({
            'advice': advice,
            'session_id': session_id
        }), 200
        
    except Exception as e:
        logger.error(f"Błąd generowania rady: {e}")
        return jsonify({'error': 'Błąd generowania rady'}), 500
