/**
 * Główny ekran gry
 */
import React, { useState, useEffect, useMemo } from 'react';
import { useNavigate } from 'react-router-dom';
import { gameAPI } from '../utils/api';
import CharacterAvatar from '../components/CharacterAvatar';
import StatsPanel from '../components/StatsPanel';
import EventModal from '../components/EventModal';
import WujekAdvice from '../components/WujekAdvice';
import ExpenseTracker from '../components/ExpenseTracker';
import logoImage from '../assets/logo.png';

function GameScreen() {
  const [session, setSession] = useState(null);
  const [currentEvent, setCurrentEvent] = useState(null);
  const [loading, setLoading] = useState(false);
  const [eventLoading, setEventLoading] = useState(false); // Loading dla generowania wydarzenia
  const [showNewGameDialog, setShowNewGameDialog] = useState(true);
  const [show23Modal, setShow23Modal] = useState(false); // Modal dla 23 lat
  const [adviceTrigger, setAdviceTrigger] = useState(0);
  const [eventUsedThisYear, setEventUsedThisYear] = useState(false);
  const [eventsCompletedThisYear, setEventsCompletedThisYear] = useState(0); // Licznik ukończonych wydarzeń
  const [actionMessage, setActionMessage] = useState(null);
  const [showGuide, setShowGuide] = useState(false);
  const navigate = useNavigate();

  const regularActions = useMemo(() => {
    if (!session) return [];

    const debtLimit = -5000;
    const savings = Number(session.savings ?? 0);

    const buildCostAction = ({ key, label, icon, description, cost }) => {
      const projectedBalance = savings - cost;
      const disabled = projectedBalance < debtLimit;
      return {
        key,
        label,
        icon,
        description,
        disabled,
        disabledReason: disabled ? `Przekroczysz limit zadłużenia (${debtLimit} zł)` : null,
      };
    };

    return [
      buildCostAction({
        key: 'go_out',
        label: 'Wyjście ze znajomymi',
        icon: '🎉',
        description: '-200 zł, + szczęście, - stres',
        cost: 200,
      }),
      buildCostAction({
        key: 'medical_checkup',
        label: 'Zbadaj się',
        icon: '🩺',
        description: '-300 zł, + zdrowie',
        cost: 300,
      }),
      {
        key: 'retire_now',
        label: 'Przejdź na emeryturę',
        icon: '🧓',
        description: 'Zakończ karierę i rozlicz emeryturę',
        disabled: session.age < 55 || session.life_stage === 'retirement',
        disabledReason: session.life_stage === 'retirement' ? 'Już jesteś na emeryturze' : 'Dostępne po ukończeniu 55 lat'
      }
    ];
  }, [session]);

  useEffect(() => {
    // Sprawdź czy istnieje aktywna sesja w localStorage
    const savedSessionId = localStorage.getItem('activeSessionId');
    if (savedSessionId) {
      loadSession(parseInt(savedSessionId));
      setShowNewGameDialog(false);
    }
  }, []);

  useEffect(() => {
    if (!actionMessage) return;

    const timeout = setTimeout(() => setActionMessage(null), 3500);
    return () => clearTimeout(timeout);
  }, [actionMessage]);

  const loadSession = async (sessionId) => {
    try {
  const response = await gameAPI.getSession(sessionId);
  setSession({ ...response.data });
      
      // Sprawdź czy gra się zakończyła
      if (response.data.game_over) {
        navigate(`/results/${sessionId}`);
      }
    } catch (error) {
      console.error('Błąd ładowania sesji:', error);
      setShowNewGameDialog(true);
    }
  };

  const startNewGame = async (sex) => {
    setLoading(true);
    try {
      const response = await gameAPI.createSession({ sex });
  const newSession = response.data.session;
  setSession({ ...newSession });
      localStorage.setItem('activeSessionId', newSession.id);
      setShowNewGameDialog(false);
      
      // Załaduj pierwsze wydarzenie
      setTimeout(() => generateEvent(), 1000);
    } catch (error) {
      console.error('Błąd tworzenia sesji:', error);
      alert('Nie udało się utworzyć nowej gry');
    } finally {
      setLoading(false);
    }
  };

  const advanceYear = async () => {
    if (!session) return;
    
    // BLOKADA: Nie można przesunąć czasu jeśli jest aktywne wydarzenie
    if (currentEvent) {
      alert('⚠️ Musisz najpierw podjąć decyzję w bieżącym wydarzeniu!');
      return;
    }
    
    // BLOKADA: Wymaga co najmniej 1 wydarzenia w roku
    if (eventsCompletedThisYear === 0) {
    //   alert('⚠️ Musisz ukończyć co najmniej jedno wydarzenie przed przejściem do następnego roku!');
      return;
    }
    
    setLoading(true);
    try {
  const response = await gameAPI.advanceTime(session.id);
  setSession({ ...response.data.session });
      
      // Sprawdź czy gracz skończył 23 lata
      if (response.data.turned_23) {
        setShow23Modal(true);
      }
      
      // Reset flag na nowy rok
      setEventUsedThisYear(false);
      setEventsCompletedThisYear(0);
      
      // Sprawdź game over
      if (response.data.session.game_over) {
        navigate(`/results/${session.id}`);
        return;
      }
      
      // Co kilka lat - generuj wydarzenie
      if (response.data.session.age % 2 === 0) {
        setTimeout(() => generateEvent(), 500);
      }
      
      // Co 5 lat - pokaż radę Wujka
      if (response.data.session.age % 5 === 0) {
        setAdviceTrigger(prev => prev + 1);
      }
    } catch (error) {
      console.error('Błąd przesuwania czasu:', error);
      alert('Wystąpił błąd podczas przesuwania czasu');
    } finally {
      setLoading(false);
    }
  };

  const generateEvent = async () => {
    if (!session) return;
    
    // BLOKADA: Tylko jedno wydarzenie na rok
    if (eventUsedThisYear) {
    //   alert('⚠️ Możesz wygenerować tylko jedno losowe wydarzenie na rok. Przesuń czas do następnego roku.');
      return;
    }
    
    setEventLoading(true); // Pokaż loading
    try {
      const response = await gameAPI.getEvent(session.id);
      
      // Sprawdź czy dostaliśmy wydarzenie (może być null jeśli 10% szans na brak)
      if (response.data.event) {
        setCurrentEvent(response.data.event);
        setEventUsedThisYear(true);
      } else {
        // Brak wydarzenia - spokojny rok
        alert('🌟 Spokojny rok! Nic szczególnego się nie wydarzyło.');
        setEventUsedThisYear(true);
        setEventsCompletedThisYear(1); // Traktuj jako "ukończone" żeby móc przejść do następnego roku
      }
    } catch (error) {
      console.error('Błąd generowania wydarzenia:', error);
      // Sprawdź czy błąd to 404 (brak wydarzeń)
      if (error.response && error.response.status === 404) {
        alert('🌟 Spokojny rok! Brak dostępnych wydarzeń.');
        setEventUsedThisYear(true);
        setEventsCompletedThisYear(1);
      } else {
        alert('Nie udało się wygenerować wydarzenia');
      }
    } finally {
      setEventLoading(false); // Ukryj loading
    }
  };

  const handleRegularAction = async (actionType) => {
    if (!session) return;

    setLoading(true);
    try {
  const response = await gameAPI.performAction(session.id, actionType);
  const updatedSession = response.data.session;
  setSession({ ...updatedSession });
      setCurrentEvent(null);

      if (actionType !== 'retire_now') {
        setEventsCompletedThisYear((prev) => Math.max(prev, 1));
        setEventUsedThisYear(true);
      }

      if (response.data.trigger_advice) {
        setAdviceTrigger((prev) => prev + 1);
      }

      if (response.data.message) {
        setActionMessage(response.data.message);
      }

      if (response.data.game_over) {
        setTimeout(() => navigate(`/results/${updatedSession.id}`), 600);
      }
    } catch (error) {
      console.error('Błąd wykonywania działania:', error);
      const backendMessage = error.response?.data?.error;
      setActionMessage(backendMessage || 'Nie udało się wykonać działania.');
    } finally {
      setLoading(false);
    }
  };

  const handleEventChoice = async (choiceIndex) => {
    if (!currentEvent) return;
    
    setLoading(true);
    try {
  const response = await gameAPI.makeChoice(currentEvent.id, choiceIndex);
  const updatedSession = response.data.session;
  setSession({ ...updatedSession });
      setCurrentEvent(null);
      
      // Zwiększ licznik ukończonych wydarzeń w tym roku
      setEventsCompletedThisYear(prev => prev + 1);
      
      // Pokaż radę Wujka po decyzji
      setAdviceTrigger(prev => prev + 1);

      if (response.data.turned_23) {
        setShow23Modal(true);
      }

      if (updatedSession?.game_over) {
        setTimeout(() => navigate(`/results/${updatedSession.id}`), 600);
      }
    } catch (error) {
      console.error('Błąd zapisywania wyboru:', error);
      alert('Nie udało się zapisać wyboru');
    } finally {
      setLoading(false);
    }
  };

  const handleLogout = () => {
    localStorage.removeItem('token');
    localStorage.removeItem('activeSessionId');
    window.location.href = '/login';
  };

  const handleRestartGame = () => {
    if (confirm('Czy na pewno chcesz rozpocząć nową grę? Obecny postęp zostanie utracony.')) {
      localStorage.removeItem('activeSessionId');
      setSession(null);
      setCurrentEvent(null);
      setShowNewGameDialog(true);
      setEventsCompletedThisYear(0);
      setEventUsedThisYear(false);
    }
  };

  // Dialog nowej gry - gaming style
  if (showNewGameDialog) {
    return (
      <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-slate-900 via-blue-900 to-slate-800 p-4">
        <div className="max-w-lg w-full">
          <div className="bg-gradient-to-br from-white to-gray-100 rounded-3xl shadow-2xl p-8 border-4 border-zus-yellow">
            <div className="text-center mb-6">
              <div className="bg-gradient-to-br from-zus-yellow to-orange-400 rounded-full p-6 inline-block shadow-xl mb-4">
                <img src={logoImage} alt="Logo" className="w-[50px] h-[50px] object-contain" />
              </div>
              <h2 className="text-4xl font-black text-zus-dark-blue mb-2 tracking-tight">
                NOWA GRA
              </h2>
              <p className="text-gray-700 text-lg font-semibold">
                Wybierz płeć swojej postaci i rozpocznij symulację życia!
              </p>
            </div>

            <div className="space-y-4">
              <button
                onClick={() => startNewGame('male')}
                disabled={loading}
                className="w-full bg-gradient-to-r from-blue-600 to-blue-700 hover:from-blue-500 hover:to-blue-600 text-white font-black text-2xl py-6 rounded-2xl shadow-xl transition transform hover:scale-105 disabled:opacity-50 disabled:transform-none border-4 border-blue-400"
              >
                <div className="flex items-center justify-center gap-3">
                  <span className="text-4xl">👨</span>
                  <span>MĘŻCZYZNA</span>
                </div>
              </button>
              
              <button
                onClick={() => startNewGame('female')}
                disabled={loading}
                className="w-full bg-gradient-to-r from-pink-600 to-pink-700 hover:from-pink-500 hover:to-pink-600 text-white font-black text-2xl py-6 rounded-2xl shadow-xl transition transform hover:scale-105 disabled:opacity-50 disabled:transform-none border-4 border-pink-400"
              >
                <div className="flex items-center justify-center gap-3">
                  <span className="text-4xl">👩</span>
                  <span>KOBIETA</span>
                </div>
              </button>

              <div className="mt-6 bg-gradient-to-r from-blue-50 to-purple-50 rounded-xl p-5 border-2 border-blue-200">
                <h3 className="font-bold text-gray-800 mb-2 flex items-center gap-2">
                  <span className="text-xl">💡</span>
                  Jak grać?
                </h3>
                <ul className="text-sm text-gray-700 space-y-1">
                  <li>• Symuluj życie od 18 lat do emerytury</li>
                  <li>• Podejmuj decyzje wpływające na finanse i zdrowie</li>
                  <li>• Planuj swoją emeryturę w systemie ZUS</li>
                  <li>• Uważaj - każda decyzja ma konsekwencje!</li>
                </ul>
              </div>
            </div>

            <button
              onClick={handleLogout}
              className="w-full mt-6 bg-gray-600 hover:bg-gray-700 text-white font-bold py-3 rounded-xl transition"
            >
              🚪 Wyloguj się
            </button>
          </div>
        </div>
      </div>
    );
  }

  if (!session) {
    return (
      <div className="min-h-screen flex items-center justify-center">
        <div className="text-xl text-gray-600">Ładowanie gry...</div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-900 via-blue-900 to-slate-800 pb-20">
      {actionMessage && (
        <div className="fixed top-24 left-1/2 -translate-x-1/2 transform z-40 max-w-md w-full px-4">
          <div className="bg-white/90 backdrop-blur-md rounded-2xl shadow-2xl border-2 border-zus-yellow px-5 py-4 text-center">
            <p className="text-sm sm:text-base text-slate-800 font-semibold">
              {actionMessage}
            </p>
          </div>
        </div>
      )}

      {/* Loading Overlay podczas generowania wydarzenia */}
      {eventLoading && (
        <div className="fixed inset-0 bg-black bg-opacity-70 flex items-center justify-center z-50 backdrop-blur-sm">
          <div className="bg-gradient-to-br from-white to-gray-100 rounded-3xl p-8 shadow-2xl border-4 border-zus-yellow text-center max-w-md">
            <div className="animate-spin text-7xl mb-4">🎲</div>
            <h3 className="text-2xl font-black text-zus-dark-blue mb-2">
              Generowanie wydarzenia...
            </h3>
            <p className="text-gray-600">
              Wujek Dobra Rada przygotowuje dla Ciebie życiowe wyzwanie!
            </p>
            <div className="mt-4">
              <div className="h-2 bg-gray-200 rounded-full overflow-hidden">
                <div className="h-full bg-gradient-to-r from-zus-blue to-zus-yellow animate-pulse" style={{ width: '100%' }}></div>
              </div>
            </div>
          </div>
        </div>
      )}

      {/* Floating Wujek Button - prawy dolny róg */}
      <button
        onClick={() => setAdviceTrigger(prev => prev + 1)}
        disabled={loading}
        className="fixed bottom-6 right-6 bg-gradient-to-r from-yellow-500 to-orange-500 hover:from-yellow-400 hover:to-orange-400 text-white font-black px-6 py-4 rounded-full shadow-2xl transition transform hover:scale-110 z-40 border-4 border-yellow-300 animate-bounce"
        title="Zapytaj Wujka Dobra Rada"
      >
        <div className="flex items-center gap-2">
          <span className="text-3xl">💡</span>
          <span className="text-sm hidden sm:inline">Wujek</span>
        </div>
      </button>

      {/* Nagłówek - nowoczesny gaming style */}
      <header className="bg-gradient-to-r from-zus-dark-blue via-zus-blue to-zus-dark-blue shadow-2xl border-b-4 border-zus-yellow sticky top-0 z-30">
        <div className="container mx-auto px-3 sm:px-4 py-3 sm:py-4">
          <div className="flex flex-wrap justify-between items-center gap-3">
            <div className="flex items-center gap-2 sm:gap-4">
              <div className="bg-zus-yellow rounded-full p-2 sm:p-3 shadow-lg">
                <img src={logoImage} alt="Logo" className="w-[50px] h-[50px] object-contain" />
              </div>
              <div>
                <h1 className="text-xl sm:text-3xl font-black text-white tracking-tight">
                  LIFEOVERFLOW
                </h1>
                <p className="text-xs sm:text-sm text-zus-yellow font-semibold">
                  Planowanie Emerytalne ZUS
                </p>
              </div>
            </div>
            <div className="flex items-center space-x-2 sm:space-x-6">
              <div className="text-right bg-white bg-opacity-10 rounded-xl px-3 sm:px-6 py-2 sm:py-3 border-2 border-zus-yellow">
                <div className="text-xs text-zus-yellow font-semibold uppercase tracking-wider">
                  Rok życia
                </div>
                <div className="text-2xl sm:text-4xl font-black text-white">
                  {session.age}
                </div>
              </div>
              <button
                onClick={handleRestartGame}
                className="hidden sm:flex items-center gap-2 bg-white/15 hover:bg-white/25 text-white font-semibold px-4 py-2 rounded-xl transition border border-white/30"
              >
                <span>🔁</span>
                <span>Nowa gra</span>
              </button>
              <button
                onClick={handleLogout}
                className="bg-red-600 hover:bg-red-700 text-white font-bold px-3 sm:px-5 py-2 sm:py-3 rounded-xl transition shadow-lg text-sm sm:text-base"
              >
                🚪 <span className="hidden sm:inline">Wyloguj</span>
              </button>
            </div>
          </div>
        </div>
      </header>

      {/* Główna zawartość - 3 kolumny */}
      <div className="container mx-auto px-3 sm:px-4 py-4 sm:py-6">
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-4 sm:gap-6">
          {/* Lewa kolumna - Awatar i finanse */}
          <div className="lg:col-span-3 space-y-3 sm:space-y-4">
            <CharacterAvatar
              age={session.age}
              sex={session.sex}
              happiness={session.happiness}
              health={session.health}
            />
            <ExpenseTracker session={session} />
          </div>

          {/* Środkowa kolumna - Statystyki */}
          <div className="lg:col-span-6">
            <StatsPanel session={session} />
          </div>

          {/* Prawa kolumna - Akcje */}
          <div className="lg:col-span-3 space-y-3 sm:space-y-4">
            {/* Panel akcji */}
            <div className="bg-gradient-to-br from-slate-800 to-slate-900 rounded-2xl p-4 sm:p-5 shadow-2xl border-2 border-slate-700">
              <h3 className="text-lg sm:text-xl font-black text-white mb-3 sm:mb-4 flex items-center gap-2 uppercase tracking-wide">
                <span className="text-xl sm:text-2xl">🎯</span>
                <span className="text-sm sm:text-base">Panel akcji</span>
              </h3>
              
              <div className="space-y-2 sm:space-y-3">
                {/* Alert gdy jest aktywne wydarzenie */}
                {currentEvent && (
                  <div className="bg-gradient-to-r from-red-600 to-orange-500 rounded-xl p-3 sm:p-4 text-center animate-pulse border-2 border-yellow-400">
                    <p className="text-xs sm:text-sm font-bold text-white">
                      ⚠️ AKTYWNE WYDARZENIE!
                    </p>
                    <p className="text-xs text-yellow-100 mt-1">
                      Podejmij decyzję przed przesunięciem czasu
                    </p>
                  </div>
                )}

                {/* Alert gdy brak wydarzeń w tym roku */}
                {eventsCompletedThisYear === 0 && !currentEvent && (
                  <div className="bg-gradient-to-r from-purple-600 to-pink-600 rounded-xl p-3 sm:p-4 text-center border-2 border-purple-400">
                    <p className="text-xs sm:text-sm font-bold text-white">
                      🎲 Wygeneruj wydarzenie!
                    </p>
                    <p className="text-xs text-purple-100 mt-1">
                      Minimum 1 wydarzenie przed następnym rokiem
                    </p>
                  </div>
                )}
                
                {/* Losowe wydarzenie */}
                <button
                  onClick={generateEvent}
                  disabled={loading || session.game_over || eventUsedThisYear || eventLoading}
                  className="w-full bg-gradient-to-r from-purple-600 to-pink-600 hover:from-purple-500 hover:to-pink-500 text-white font-bold py-3 sm:py-4 px-4 sm:px-6 rounded-xl shadow-lg transition transform hover:scale-105 disabled:opacity-50 disabled:cursor-not-allowed disabled:transform-none border-2 border-purple-400 text-sm sm:text-base"
                >
                  <div className="flex items-center justify-center gap-2 sm:gap-3">
                    <span className="text-xl sm:text-2xl">{eventLoading ? '⏳' : '🎲'}</span>
                    <span className="text-base sm:text-lg">
                      {eventLoading ? 'Generowanie...' : eventUsedThisYear ? 'Wydarzenie zrealizowane' : 'Losowe wydarzenie'}
                    </span>
                  </div>
                </button>

                {/* Szybkie akcje */}
                {regularActions.length > 0 && (
                  <div className="bg-slate-900/70 rounded-xl border border-slate-700 p-3 sm:p-4 space-y-3">
                    <div className="flex items-center justify-between">
                      <p className="text-xs sm:text-sm uppercase tracking-wide text-slate-200 font-semibold flex items-center gap-2">
                        <span className="text-base sm:text-lg">⚡</span>
                        <span>Szybkie decyzje</span>
                      </p>
                      <span className="text-[10px] sm:text-xs text-slate-400">Zajmuje czas tego roku</span>
                    </div>
                    <div className="grid grid-cols-1 gap-2">
                      {regularActions.map((action) => (
                        <button
                          key={action.key}
                          onClick={() => handleRegularAction(action.key)}
                          disabled={loading || session.game_over || action.disabled}
                          title={action.disabled ? action.disabledReason : action.description}
                          className="w-full bg-gradient-to-r from-slate-700 to-slate-800 hover:from-slate-600 hover:to-slate-700 text-white font-semibold py-3 px-4 rounded-xl shadow-lg transition transform hover:scale-[1.02] disabled:opacity-40 disabled:cursor-not-allowed disabled:transform-none border border-slate-600 text-left"
                        >
                          <div className="flex items-center justify-between gap-3">
                            <div className="flex items-center gap-3">
                              <span className="text-xl sm:text-2xl">{action.icon}</span>
                              <div>
                                <p className="text-sm sm:text-base font-bold">{action.label}</p>
                                <p className="text-xs text-slate-300">{action.description}</p>
                              </div>
                            </div>
                            {!action.disabled && (
                              <span className="text-xs font-semibold text-zus-yellow uppercase">Dostępne</span>
                            )}
                          </div>
                        </button>
                      ))}
                    </div>
                  </div>
                )}

                {/* Przejście do następnego roku */}
                {eventsCompletedThisYear > 0 && !currentEvent ? (
                  <button
                    onClick={advanceYear}
                    disabled={loading || session.game_over}
                    className="w-full bg-gradient-to-r from-green-600 to-emerald-600 hover:from-green-500 hover:to-emerald-500 text-white font-bold py-3 sm:py-4 px-4 sm:px-6 rounded-xl shadow-lg transition transform hover:scale-105 disabled:opacity-50 disabled:cursor-not-allowed disabled:transform-none border-2 border-green-400 text-sm sm:text-base"
                  >
                    <div className="flex items-center justify-center gap-2 sm:gap-3">
                      <span className="text-xl sm:text-2xl">⏭️</span>
                      <div className="text-left">
                        <div className="text-xs sm:text-sm opacity-90">Następny rok</div>
                        <div className="text-base sm:text-xl">Wiek: {session.age + 1}</div>
                      </div>
                    </div>
                  </button>
                ) : (
                  <div className="text-center text-xs sm:text-sm text-slate-300 bg-slate-900/60 border border-slate-700 rounded-xl py-3 px-4">
                    Zanim przejdziesz dalej, przeżyj wydarzenie lub wybierz jedną z szybkich decyzji.
                  </div>
                )}
              </div>
            </div>

            {/* Info o grze */}
            <div className="bg-gradient-to-br from-blue-900 to-blue-950 rounded-2xl p-3 sm:p-4 shadow-xl border-2 border-blue-700">
              <button
                onClick={() => setShowGuide((prev) => !prev)}
                className="w-full flex items-center justify-between text-left text-white font-black text-base sm:text-lg uppercase gap-2"
              >
                <span className="flex items-center gap-2">
                  <span className="text-lg sm:text-xl">ℹ️</span>
                  <span className="text-sm sm:text-base">Instrukcja</span>
                </span>
                <span className="text-sm text-zus-yellow font-semibold">
                  {showGuide ? 'ukryj' : 'pokaż'}
                </span>
              </button>
              {showGuide && (
                <ul className="mt-3 text-xs sm:text-sm text-blue-100 space-y-1 sm:space-y-2">
                  <li className="flex items-start gap-2">
                    <span className="text-green-400 font-bold">▸</span>
                    <span>Ukończ min. 1 wydarzenie przed następnym rokiem</span>
                  </li>
                  <li className="flex items-start gap-2">
                    <span className="text-purple-400 font-bold">▸</span>
                    <span>Wydarzenia pojawią się automatycznie</span>
                  </li>
                  <li className="flex items-start gap-2">
                    <span className="text-red-400 font-bold">▸</span>
                    <span>Każda decyzja ma konsekwencje!</span>
                  </li>
                  <li className="flex items-start gap-2">
                    <span className="text-yellow-400 font-bold">▸</span>
                    <span>Dbaj o zdrowie, finanse i relacje</span>
                  </li>
                  <li className="flex items-start gap-2">
                    <span className="text-orange-400 font-bold">▸</span>
                    <span>Kliknij Wujka w prawym dolnym rogu!</span>
                  </li>
                </ul>
              )}
              <div className="sm:hidden mt-4">
                <button
                  onClick={handleRestartGame}
                  className="w-full bg-white/15 hover:bg-white/25 text-white text-sm font-semibold py-2 rounded-lg border border-white/20"
                >
                  🔁 Rozpocznij nową grę
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>

      {/* Modal wydarzenia */}
      {currentEvent && (
        <EventModal
          event={currentEvent}
          onChoice={handleEventChoice}
          onClose={() => setCurrentEvent(null)}
        />
      )}

      {/* Modal 23 lata - gra staje się trudniejsza */}
      {show23Modal && (
        <div className="fixed inset-0 bg-black bg-opacity-70 flex items-center justify-center z-50 p-4">
          <div className="bg-gradient-to-br from-red-50 to-orange-50 rounded-2xl max-w-2xl w-full p-6 sm:p-8 shadow-2xl border-4 border-red-500 animate-pulse">
            <div className="text-center">
              <div className="text-6xl sm:text-8xl mb-4">⚠️</div>
              <h2 className="text-2xl sm:text-4xl font-black text-red-800 mb-4">
                SKOŃCZYŁEŚ 23 LATA!
              </h2>
              <div className="bg-white bg-opacity-80 rounded-xl p-6 mb-6 border-2 border-red-300">
                <p className="text-lg sm:text-xl text-gray-800 font-bold mb-4">
                  🏠 Gra staje się trudniejsza!
                </p>
                <div className="text-left space-y-3 text-gray-700">
                  <p className="flex items-start gap-3">
                    <span className="text-2xl">💸</span>
                    <span className="text-sm sm:text-base">
                      <strong>Koszty życia:</strong> Od teraz musisz płacić za jedzenie, transport i inne wydatki (1500 zł/mies.)
                    </span>
                  </p>
                  <p className="flex items-start gap-3">
                    <span className="text-2xl">🏘️</span>
                    <span className="text-sm sm:text-base">
                      <strong>Mieszkanie:</strong> Jeśli pracujesz, będziesz musiał wynająć mieszkanie
                    </span>
                  </p>
                  <p className="flex items-start gap-3">
                    <span className="text-2xl">📊</span>
                    <span className="text-sm sm:text-base">
                      <strong>Bilans:</strong> Sprawdź panel finansowy - musi się bilansować!
                    </span>
                  </p>
                  <p className="flex items-start gap-3">
                    <span className="text-2xl">⚡</span>
                    <span className="text-sm sm:text-base">
                      <strong>Strategia:</strong> Musisz zarabiać więcej niż wydajesz, inaczej szybko wpadniesz w długi!
                    </span>
                  </p>
                </div>
              </div>
              <button
                onClick={() => setShow23Modal(false)}
                className="bg-gradient-to-r from-red-600 to-orange-600 hover:from-red-500 hover:to-orange-500 text-white font-black text-lg sm:text-xl px-8 py-4 rounded-xl shadow-lg transition transform hover:scale-105"
              >
                ROZUMIEM - ZACZNIJMY! 💪
              </button>
            </div>
          </div>
        </div>
      )}

      {/* Wujek Dobra Rada */}
      {session && (
        <WujekAdvice
          sessionId={session.id}
          trigger={adviceTrigger}
        />
      )}
    </div>
  );
}

export default GameScreen;
