"""
Konfiguracja aplikacji Flask
Zawiera wszystkie zmienne środowiskowe i ustawienia aplikacji
"""
import os
from dotenv import load_dotenv

# Załaduj zmienne środowiskowe z pliku .env
load_dotenv()

class Config:
    """Klasa konfiguracyjna dla aplikacji Flask"""
    
    # Sekretny klucz dla JWT i sesji
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key-change-in-production')
    
    # Konfiguracja bazy danych
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///game.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Klucz API Anthropic (Claude)
    ANTHROPIC_API_KEY = os.getenv('ANTHROPIC_API_KEY', '')
    
    # CORS
    CORS_HEADERS = 'Content-Type'
    
    # Debug mode
    DEBUG = os.getenv('FLASK_ENV', 'development') == 'development'
