"""
Główna aplikacja Flask - Life Simulation Pension Planning Game
"""

from flask import Flask, jsonify
from flask_cors import CORS
import logging
from logging.handlers import RotatingFileHandler
import os

from config import Config
from models import db

# Konfiguracja logowania
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


def create_app(config_class=Config):
    """
    Factory function do tworzenia aplikacji Flask

    Args:
        config_class: Klasa konfiguracyjna

    Returns:
        Skonfigurowana aplikacja Flask
    """
    app = Flask(__name__)
    app.config.from_object(config_class)

    # CORS - allow all origins for API endpoints
    # allow all cors
    CORS(app, resources={r"/api/*": {"origins": "*"}})
    # Inicjalizuj bazę danych
    db.init_app(app)

    # Zarejestruj blueprinty (routes)
    register_blueprints(app)

    # Utwórz tabele w bazie danych
    with app.app_context():
        db.create_all()
        logger.info("Tabele bazy danych utworzone/zaktualizowane")

    # Obsługa błędów
    register_error_handlers(app)

    # Logging do pliku w produkcji
    if not app.debug:
        setup_file_logging(app)

    logger.info("Aplikacja Flask zainicjalizowana pomyślnie")

    return app


def register_blueprints(app):
    """Rejestruje wszystkie blueprinty (routes)"""
    from routes.auth import auth_bp
    from routes.game import game_bp
    from routes.ai_advisor import advisor_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(game_bp)
    app.register_blueprint(advisor_bp)

    logger.info("Blueprinty zarejestrowane")


def register_error_handlers(app):
    """Rejestruje globalne handlery błędów"""

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({"error": "Nie znaleziono zasobu"}), 404

    @app.errorhandler(500)
    def internal_error(error):
        logger.error(f"Błąd serwera: {error}")
        return jsonify({"error": "Wewnętrzny błąd serwera"}), 500

    @app.errorhandler(Exception)
    def handle_exception(error):
        logger.error(f"Nieobsłużony wyjątek: {error}", exc_info=True)
        return jsonify({"error": "Wystąpił nieoczekiwany błąd"}), 500


def setup_file_logging(app):
    """Konfiguruje logowanie do pliku"""
    if not os.path.exists("logs"):
        os.mkdir("logs")

    file_handler = RotatingFileHandler(
        "logs/app.log", maxBytes=10240000, backupCount=10  # 10MB
    )
    file_handler.setFormatter(
        logging.Formatter(
            "%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]"
        )
    )
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)

    app.logger.setLevel(logging.INFO)
    app.logger.info("Aplikacja wystartowana")


# Trasa testowa - health check
@create_app().route("/api/health", methods=["GET"])
def health_check():
    """Endpoint do sprawdzenia czy serwer działa"""
    return jsonify({"status": "ok", "message": "Life Simulation API is running"}), 200


if __name__ == "__main__":
    # Utwórz aplikację
    app = create_app()

    # Uruchom serwer deweloperski
    port = int(os.getenv("PORT", 4442))
    app.run(host="0.0.0.0", port=port, debug=Config.DEBUG)
