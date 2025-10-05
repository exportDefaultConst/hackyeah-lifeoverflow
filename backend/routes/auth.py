"""
Trasy autentykacji - rejestracja i logowanie
"""
from flask import Blueprint, request, jsonify
import jwt
import logging
from datetime import datetime, timedelta
from models import db, User
from config import Config

logger = logging.getLogger(__name__)

auth_bp = Blueprint('auth', __name__, url_prefix='/api/auth')


@auth_bp.route('/register', methods=['POST'])
def register():
    """
    Rejestracja nowego użytkownika
    
    Oczekuje JSON: { "email": "...", "password": "..." }
    """
    try:
        data = request.get_json()
        
        # Walidacja danych
        if not data or 'email' not in data or 'password' not in data:
            return jsonify({'error': 'Email i hasło są wymagane'}), 400
        
        email = data['email'].lower().strip()
        password = data['password']
        
        # Sprawdź czy użytkownik już istnieje
        if User.query.filter_by(email=email).first():
            return jsonify({'error': 'Użytkownik o tym adresie email już istnieje'}), 409
        
        # Utwórz nowego użytkownika
        user = User(email=email)
        user.set_password(password)
        
        db.session.add(user)
        db.session.commit()
        
        logger.info(f"Zarejestrowano nowego użytkownika: {email}")
        
        # Wygeneruj token JWT
        token = generate_token(user.id)
        
        return jsonify({
            'message': 'Rejestracja pomyślna',
            'token': token,
            'user': user.to_dict()
        }), 201
        
    except Exception as e:
        logger.error(f"Błąd podczas rejestracji: {e}")
        db.session.rollback()
        return jsonify({'error': 'Błąd serwera podczas rejestracji'}), 500


@auth_bp.route('/login', methods=['POST'])
def login():
    """
    Logowanie użytkownika
    
    Oczekuje JSON: { "email": "...", "password": "..." }
    """
    try:
        data = request.get_json()
        
        # Walidacja danych
        if not data or 'email' not in data or 'password' not in data:
            return jsonify({'error': 'Email i hasło są wymagane'}), 400
        
        email = data['email'].lower().strip()
        password = data['password']
        
        # Znajdź użytkownika
        user = User.query.filter_by(email=email).first()
        
        if not user or not user.check_password(password):
            return jsonify({'error': 'Nieprawidłowy email lub hasło'}), 401
        
        logger.info(f"Zalogowano użytkownika: {email}")
        
        # Wygeneruj token JWT
        token = generate_token(user.id)
        
        return jsonify({
            'message': 'Logowanie pomyślne',
            'token': token,
            'user': user.to_dict()
        }), 200
        
    except Exception as e:
        logger.error(f"Błąd podczas logowania: {e}")
        return jsonify({'error': 'Błąd serwera podczas logowania'}), 500


def generate_token(user_id):
    """
    Generuje JWT token dla użytkownika (bez wygasania)
    
    Args:
        user_id: ID użytkownika
        
    Returns:
        Token JWT jako string
    """
    try:
        payload = {
            'user_id': user_id,
            'iat': datetime.utcnow()
        }
        
        token = jwt.encode(payload, Config.SECRET_KEY, algorithm='HS256')
        return token
        
    except Exception as e:
        logger.error(f"Błąd generowania tokenu: {e}")
        raise


def verify_token(token):
    """
    Weryfikuje JWT token i zwraca user_id
    
    Args:
        token: Token JWT
        
    Returns:
        user_id lub None jeśli token nieprawidłowy
    """
    try:
        payload = jwt.decode(token, Config.SECRET_KEY, algorithms=['HS256'])
        return payload['user_id']
    except jwt.InvalidTokenError as e:
        logger.warning(f"Nieprawidłowy token: {e}")
        return None
    except Exception as e:
        logger.error(f"Błąd weryfikacji tokenu: {e}")
        return None


def get_current_user():
    """
    Pobiera aktualnego użytkownika z tokenu w nagłówku Authorization
    
    Returns:
        Obiekt User lub None
    """
    try:
        auth_header = request.headers.get('Authorization')
        
        if not auth_header:
            return None
        
        # Format: "Bearer <token>"
        parts = auth_header.split()
        if len(parts) != 2 or parts[0].lower() != 'bearer':
            return None
        
        token = parts[1]
        user_id = verify_token(token)
        
        if not user_id:
            return None
        
        user = User.query.get(user_id)
        return user
        
    except Exception as e:
        logger.error(f"Błąd pobierania użytkownika: {e}")
        return None
