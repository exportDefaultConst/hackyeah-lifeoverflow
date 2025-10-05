"""
Modele bazy danych SQLAlchemy
Zawiera wszystkie tabele i relacje w bazie danych
"""
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()


class User(db.Model):
    """Model użytkownika - przechowuje dane autentykacji"""
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(256), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relacja do sesji gry
    game_sessions = db.relationship('GameSession', backref='user', lazy=True, cascade='all, delete-orphan')
    
    def set_password(self, password):
        """Hashuje i zapisuje hasło"""
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        """Sprawdza poprawność hasła"""
        return check_password_hash(self.password_hash, password)
    
    def to_dict(self):
        """Konwertuje użytkownika do słownika (bez hasła)"""
        return {
            'id': self.id,
            'email': self.email,
            'created_at': self.created_at.isoformat()
        }


class GameSession(db.Model):
    """Model sesji gry - przechowuje stan gry gracza"""
    __tablename__ = 'game_sessions'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, index=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Podstawowe statystyki postaci
    work = db.Column(db.String(50), default="bezrobotny")
    work_satisfaction = db.Column(db.Integer, default=5)
    type_employment = db.Column(db.String(50), default="")
    marital_status = db.Column(db.String(20), default="single")
    children = db.Column(db.Integer, default=0)
    education = db.Column(db.String(50), default="podstawowe")
    free_time = db.Column(db.Integer, default=5)
    age = db.Column(db.Integer, default=18)
    sex = db.Column(db.String(10), default="male")
    health = db.Column(db.Integer, default=8)
    mental_health = db.Column(db.Integer, default=7)
    savings = db.Column(db.Float, default=5000.0)  # PLN
    income = db.Column(db.Float, default=0.0)  # PLN miesięcznie
    monthly_costs = db.Column(db.Float, default=0.0)  # PLN miesięcznie (jedzenie, czynsz, etc)
    student = db.Column(db.Boolean, default=True)
    education_level = db.Column(db.String(50), default="podstawowe")
    life_stage = db.Column(db.String(50), default="edukacja")
    
    # Historia ukończonych szkół/prac
    completed_education = db.Column(db.JSON, default=list)  # ['podstawowe', 'zawodowe', etc.]
    completed_events = db.Column(db.JSON, default=list)  # ['first_job', 'get_married', etc.] - wydarzenia które mogą wystąpić tylko raz
    chosen_options_history = db.Column(db.JSON, default=list)  # Historia wybranych opcji dla AI
    has_apartment = db.Column(db.Boolean, default=False)  # Czy ma mieszkanie
    has_job = db.Column(db.Boolean, default=False)  # Czy ma pracę
    job_count = db.Column(db.Integer, default=0)  # Liczba dodatkowych prac (dla multi-jobbing)
    actively_job_searching = db.Column(db.Boolean, default=False)  # Flaga czy aktywnie szuka pracy (zwiększa szanse)
    
    # Składki ZUS
    zus_contributions = db.Column(db.Float, default=0.0)  # Łączne składki emerytalne
    
    # Obliczone statystyki (0-10)
    computed_mental_health = db.Column(db.Integer, default=7)
    family_satisfaction = db.Column(db.Integer, default=5)
    family_support = db.Column(db.Integer, default=5)
    career_satisfaction = db.Column(db.Integer, default=5)
    social_connections = db.Column(db.Integer, default=6)
    physical_health = db.Column(db.Integer, default=8)
    personal_growth = db.Column(db.Integer, default=6)
    emotional_wellbeing = db.Column(db.Integer, default=7)
    financial_security = db.Column(db.Integer, default=3)
    work_life_balance = db.Column(db.Integer, default=5)
    happiness = db.Column(db.Integer, default=6)
    stress_level = db.Column(db.Integer, default=4)
    life_purpose = db.Column(db.Integer, default=5)
    relationship_quality = db.Column(db.Integer, default=5)
    self_esteem = db.Column(db.Integer, default=6)
    spirituality = db.Column(db.Integer, default=5)
    community_involvement = db.Column(db.Integer, default=4)
    
    # Status gry
    is_active = db.Column(db.Boolean, default=True)
    game_over = db.Column(db.Boolean, default=False)
    game_over_reason = db.Column(db.String(200), default="")
    
    # Relacja do wydarzeń życiowych
    life_events = db.relationship('LifeEvent', backref='session', lazy=True, cascade='all, delete-orphan')
    
    def to_dict(self):
        """Konwertuje sesję gry do słownika"""
        return {
            'id': self.id,
            'user_id': self.user_id,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
            
            # Podstawowe dane
            'work': self.work,
            'work_satisfaction': self.work_satisfaction,
            'type_employment': self.type_employment,
            'marital_status': self.marital_status,
            'children': self.children,
            'education': self.education,
            'free_time': self.free_time,
            'age': self.age,
            'sex': self.sex,
            'health': self.health,
            'mental_health': self.mental_health,
            'savings': self.savings,
            'income': self.income,
            'monthly_costs': self.monthly_costs,
            'student': self.student,
            'education_level': self.education_level,
            'life_stage': self.life_stage,
            'zus_contributions': self.zus_contributions,
            'completed_education': self.completed_education or [],
            'completed_events': self.completed_events or [],
            'chosen_options_history': self.chosen_options_history or [],
            'has_apartment': self.has_apartment,
            'has_job': self.has_job,
            'job_count': self.job_count,
            'actively_job_searching': self.actively_job_searching,
            
            # Statystyki obliczone
            'computed_mental_health': self.computed_mental_health,
            'family_satisfaction': self.family_satisfaction,
            'family_support': self.family_support,
            'career_satisfaction': self.career_satisfaction,
            'social_connections': self.social_connections,
            'physical_health': self.physical_health,
            'personal_growth': self.personal_growth,
            'emotional_wellbeing': self.emotional_wellbeing,
            'financial_security': self.financial_security,
            'work_life_balance': self.work_life_balance,
            'happiness': self.happiness,
            'stress_level': self.stress_level,
            'life_purpose': self.life_purpose,
            'relationship_quality': self.relationship_quality,
            'self_esteem': self.self_esteem,
            'spirituality': self.spirituality,
            'community_involvement': self.community_involvement,
            
            # Status
            'is_active': self.is_active,
            'game_over': self.game_over,
            'game_over_reason': self.game_over_reason
        }


class LifeEvent(db.Model):
    """Model wydarzenia życiowego"""
    __tablename__ = 'life_events'
    
    id = db.Column(db.Integer, primary_key=True)
    session_id = db.Column(db.Integer, db.ForeignKey('game_sessions.id'), nullable=False, index=True)
    event_type = db.Column(db.String(50), nullable=False)  # 'hardcoded' lub 'ai_generated'
    event_name = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    choices = db.Column(db.JSON)  # Lista opcji wyboru
    impact = db.Column(db.JSON)   # Wpływ na statystyki
    age_occurred = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Wybór gracza
    player_choice = db.Column(db.Integer)  # Index wybranej opcji
    
    def to_dict(self):
        """Konwertuje wydarzenie do słownika"""
        return {
            'id': self.id,
            'session_id': self.session_id,
            'event_type': self.event_type,
            'event_name': self.event_name,
            'description': self.description,
            'choices': self.choices,
            'impact': self.impact,
            'age_occurred': self.age_occurred,
            'created_at': self.created_at.isoformat(),
            'player_choice': self.player_choice
        }
