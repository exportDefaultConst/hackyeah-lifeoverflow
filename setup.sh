#!/bin/bash

# 🚀 Quick Setup Script - Life Simulation Game

echo "======================================"
echo "🎮 Life Simulation - ZUS Game Setup"
echo "======================================"
echo ""

# Sprawdź czy Docker działa
if ! docker info > /dev/null 2>&1; then
    echo "❌ Docker nie jest uruchomiony. Uruchom Docker Desktop i spróbuj ponownie."
    exit 1
fi

echo "✅ Docker jest uruchomiony"
echo ""

# Sprawdź czy istnieje plik .env
if [ ! -f .env ]; then
    echo "⚠️  Nie znaleziono pliku .env"
    echo "📝 Kopiuję .env.example do .env..."
    cp .env.example .env
    echo ""
    echo "⚠️  WAŻNE: Edytuj plik .env i dodaj swój ANTHROPIC_API_KEY!"
    echo ""
    read -p "Naciśnij Enter gdy dodasz klucz API lub Ctrl+C aby przerwać..."
fi

echo "🏗️  Buduję i uruchamiam kontenery Docker..."
echo ""

docker-compose down
docker-compose up --build -d

echo ""
echo "======================================"
echo "✅ Aplikacja uruchomiona!"
echo "======================================"
echo ""
echo "🌐 Frontend: http://localhost"
echo "🔧 Backend API: http://localhost:4442/api"
echo ""
echo "📋 Sprawdź logi:"
echo "   docker-compose logs -f"
echo ""
echo "🛑 Zatrzymaj aplikację:"
echo "   docker-compose down"
echo ""
echo "======================================"
