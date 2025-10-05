@echo off
REM 🚀 Quick Setup Script - Life Simulation Game (Windows)

echo ======================================
echo 🎮 Life Simulation - ZUS Game Setup
echo ======================================
echo.

REM Sprawdź czy Docker działa
docker info >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Docker nie jest uruchomiony. Uruchom Docker Desktop i spróbuj ponownie.
    pause
    exit /b 1
)

echo ✅ Docker jest uruchomiony
echo.

REM Sprawdź czy istnieje plik .env
if not exist .env (
    echo ⚠️  Nie znaleziono pliku .env
    echo 📝 Kopiuję .env.example do .env...
    copy .env.example .env
    echo.
    echo ⚠️  WAŻNE: Edytuj plik .env i dodaj swój ANTHROPIC_API_KEY!
    echo.
    pause
)

echo 🏗️  Buduję i uruchamiam kontenery Docker...
echo.

docker-compose down
docker-compose up --build -d

echo.
echo ======================================
echo ✅ Aplikacja uruchomiona!
echo ======================================
echo.
echo 🌐 Frontend: http://localhost
echo 🔧 Backend API: http://localhost:4442/api
echo.
echo 📋 Sprawdź logi:
echo    docker-compose logs -f
echo.
echo 🛑 Zatrzymaj aplikację:
echo    docker-compose down
echo.
echo ======================================
echo.
pause
