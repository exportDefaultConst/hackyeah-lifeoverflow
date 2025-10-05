# Life Simulation - ZUS Pension Planning Game 🎮

Interaktywna gra edukacyjna symulująca życie i planowanie emerytalne w polskich realiach.

## 🚀 Szybki start z Docker

### Wymagania

- Docker
- Docker Compose
- Klucz API Anthropic (dla funkcji AI)

### Uruchomienie

1. **Sklonuj repozytorium**

```bash
git clone <repository-url>
cd hack-bieg
```

2. **Skonfiguruj zmienne środowiskowe**

```bash
cp .env.example .env
# Edytuj .env i dodaj swój ANTHROPIC_API_KEY
```

3. **Uruchom aplikację**

```bash
docker-compose up --build
```

4. **Otwórz przeglądarkę**

- Frontend: https://localhost
- Backend API: https://localhost:4442/api

## 📁 Struktura projektu

```
hack-bieg/
├── backend/           # Flask API
│   ├── app.py        # Główna aplikacja
│   ├── models.py     # Modele bazy danych
│   ├── config.py     # Konfiguracja
│   ├── routes/       # Endpointy API
│   └── utils/        # Narzędzia (AI, kalkulator emerytur)
├── frontend/         # React aplikacja
│   ├── src/
│   │   ├── components/  # Komponenty React
│   │   ├── pages/      # Strony
│   │   └── utils/      # API client
│   └── public/
└── docker-compose.yml
```

## 🎮 Funkcje

- ✅ **Symulacja życia** - Od 18 do 90+ lat
- ✅ **AI Wydarzenia** - Dynamiczne wydarzenia generowane przez Claude AI
- ✅ **Wujek Dobra Rada** - AI doradca finansowy
- ✅ **System emerytalny ZUS** - Realistyczny kalkulator
- ✅ **Decyzje życiowe** - Praca, edukacja, rodzina, zdrowie
- ✅ **Polski interface** - W pełni po polsku
- ✅ **Tailwind CSS** - Nowoczesny design w kolorach ZUS

## 🛠️ Rozwój lokalny

### Backend

```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

## 🎨 Kolory ZUS

- Yellow: `#FFB34F`
- Green: `#00993F`
- Blue: `#3F84D2`
- Dark Blue: `#00416E`

## 📝 Licencja

Projekt edukacyjny dla ZUS.

## 👥 Autorzy

Hackathon Hack-Bieg 2025
