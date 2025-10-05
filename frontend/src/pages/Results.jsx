/**
 * Ekran wyników - podsumowanie gry
 */
import React, { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { gameAPI } from '../utils/api';

function Results() {
  const { sessionId } = useParams();
  const [session, setSession] = useState(null);
  const [loading, setLoading] = useState(true);
  const navigate = useNavigate();

  useEffect(() => {
    loadSession();
  }, [sessionId]);

  const loadSession = async () => {
    try {
      const response = await gameAPI.getSession(sessionId);
      setSession(response.data);
    } catch (error) {
      console.error('Błąd ładowania wyników:', error);
    } finally {
      setLoading(false);
    }
  };

  const formatCurrency = (value) => {
    return new Intl.NumberFormat('pl-PL', {
      style: 'currency',
      currency: 'PLN',
      minimumFractionDigits: 0,
    }).format(value);
  };

  const getLifeAssessment = () => {
    if (!session) return { text: '', color: '' };

    const avgScore = (
      session.happiness +
      session.health +
      session.financial_security +
      session.relationship_quality +
      session.life_purpose
    ) / 5;

    if (avgScore >= 8) {
      return {
        text: '🌟 Wspaniałe życie! Udało Ci się osiągnąć równowagę i sukces!',
        color: 'text-green-600',
        emoji: '😄'
      };
    } else if (avgScore >= 6) {
      return {
        text: '✅ Dobre życie. Były wzloty i upadki, ale w sumie wszystko się udało.',
        color: 'text-blue-600',
        emoji: '🙂'
      };
    } else if (avgScore >= 4) {
      return {
        text: '⚠️ Trudne życie. Niektóre decyzje mogły być lepsze.',
        color: 'text-yellow-600',
        emoji: '😐'
      };
    } else {
      return {
        text: '❌ Bardzo trudne życie. Wiele wyzwań i problemów.',
        color: 'text-red-600',
        emoji: '😞'
      };
    }
  };

  const getPensionAssessment = () => {
    if (!session?.pension_info) return { text: '', color: '' };

    const pension = session.pension_info.monthly_pension;

    if (pension >= 5000) {
      return {
        text: '💰 Doskonale! Wysoka emerytura zapewni Ci komfortowe życie.',
        color: 'text-green-600'
      };
    } else if (pension >= 3000) {
      return {
        text: '✅ Nieźle. Emerytura powinna wystarczyć na podstawowe potrzeby.',
        color: 'text-blue-600'
      };
    } else if (pension >= 1500) {
      return {
        text: '⚠️ Niska emerytura. Będziesz musiał/a oszczędzać.',
        color: 'text-yellow-600'
      };
    } else {
      return {
        text: '❌ Bardzo niska emerytura. To będzie trudne.',
        color: 'text-red-600'
      };
    }
  };

  if (loading) {
    return (
      <div className="min-h-screen flex items-center justify-center">
        <div className="text-xl text-gray-600">Ładowanie wyników...</div>
      </div>
    );
  }

  if (!session) {
    return (
      <div className="min-h-screen flex items-center justify-center">
        <div className="card text-center">
          <h2 className="text-2xl font-bold text-red-600 mb-4">Błąd</h2>
          <p className="mb-4">Nie udało się załadować wyników gry.</p>
          <button
            onClick={() => navigate('/game')}
            className="btn-primary"
          >
            Wróć do gry
          </button>
        </div>
      </div>
    );
  }

  const lifeAssessment = getLifeAssessment();
  const pensionAssessment = getPensionAssessment();

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-900 via-blue-900 to-slate-800 py-8 px-4">
      <div className="container mx-auto max-w-6xl">
        {/* Nagłówek */}
        <div className="text-center mb-8">
          <h1 className="text-5xl font-black text-white mb-4 tracking-tight">
            🏁 KONIEC GRY
          </h1>
          <div className="bg-gradient-to-r from-zus-yellow to-orange-400 text-zus-dark-blue text-xl font-bold py-3 px-6 rounded-2xl inline-block shadow-xl">
            {session.game_over_reason}
          </div>
        </div>

        {/* Główna karta wyników */}
        <div className="bg-gradient-to-br from-white to-gray-100 rounded-3xl shadow-2xl p-8 mb-6 border-4 border-zus-yellow">
          <div className="text-center mb-6">
            <div className="text-9xl mb-4">{lifeAssessment.emoji}</div>
            <h2 className={`text-3xl font-black ${lifeAssessment.color} mb-2`}>
              {lifeAssessment.text}
            </h2>
            <div className="text-gray-600 text-xl font-semibold">
              Przeżyłeś/aś {session.age} lat
            </div>
          </div>

          {/* Statystyki końcowe - główne */}
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6 mt-8">
            {/* Finanse */}
            <div className="bg-gradient-to-br from-green-50 to-white rounded-2xl p-6 border-2 border-green-300 shadow-lg">
              <h3 className="text-2xl font-black text-zus-dark-blue mb-4 flex items-center gap-2">
                <span className="text-3xl">💰</span>
                Finanse końcowe
              </h3>
              <div className="space-y-3">
                <div className="flex justify-between items-center bg-white rounded-xl p-3 border border-gray-200">
                  <span className="font-semibold">Oszczędności:</span>
                  <span className="font-black text-2xl text-zus-green">
                    {formatCurrency(session.savings)}
                  </span>
                </div>
                <div className="flex justify-between items-center bg-white rounded-xl p-3 border border-gray-200">
                  <span className="font-semibold">Składki ZUS:</span>
                  <span className="font-black text-xl text-zus-blue">
                    {formatCurrency(session.zus_contributions)}
                  </span>
                </div>
                {session.pension_info && (
                  <div className="bg-gradient-to-r from-zus-yellow to-yellow-300 rounded-xl p-4 border-2 border-yellow-400 shadow-md">
                    <div className="flex justify-between mb-2">
                      <span className="font-bold">Emerytura miesięczna:</span>
                      <span className="font-black text-2xl text-zus-dark-blue">
                        {formatCurrency(session.pension_info.monthly_pension)}
                      </span>
                    </div>
                    <div className={`text-sm font-semibold ${pensionAssessment.color}`}>
                      {pensionAssessment.text}
                    </div>
                  </div>
                )}
              </div>
            </div>

            {/* Życie osobiste */}
            <div className="bg-gradient-to-br from-blue-50 to-white rounded-2xl p-6 border-2 border-blue-300 shadow-lg">
              <h3 className="text-2xl font-black text-zus-dark-blue mb-4 flex items-center gap-2">
                <span className="text-3xl">❤️</span>
                Życie osobiste
              </h3>
              <div className="space-y-3">
                <div className="flex justify-between bg-white rounded-xl p-3 border border-gray-200">
                  <span className="font-semibold">Stan cywilny:</span>
                  <span className="font-bold">{session.marital_status}</span>
                </div>
                <div className="flex justify-between bg-white rounded-xl p-3 border border-gray-200">
                  <span className="font-semibold">Dzieci:</span>
                  <span className="font-bold">{session.children}</span>
                </div>
                <div className="flex justify-between bg-white rounded-xl p-3 border border-gray-200">
                  <span className="font-semibold">Wykształcenie:</span>
                  <span className="font-bold">{session.education_level}</span>
                </div>
                <div className="flex justify-between bg-white rounded-xl p-3 border border-gray-200">
                  <span className="font-semibold">Praca:</span>
                  <span className="font-bold">{session.work || 'Brak'}</span>
                </div>
              </div>
            </div>
          </div>

          {/* Kluczowe wskaźniki - duże karty */}
          <div className="mt-8 grid grid-cols-2 md:grid-cols-4 gap-4">
            <StatCard label="Szczęście" value={session.happiness} icon="😊" />
            <StatCard label="Zdrowie" value={session.health} icon="❤️" />
            <StatCard label="Kariera" value={session.career_satisfaction} icon="💼" />
            <StatCard label="Relacje" value={session.relationship_quality} icon="👨‍👩‍👧‍👦" />
          </div>
        </div>

        {/* WSZYSTKIE SZCZEGÓŁOWE STATYSTYKI - pokazujemy tutaj! */}
        <div className="bg-gradient-to-br from-white to-gray-100 rounded-3xl shadow-2xl p-8 mb-6 border-4 border-purple-400">
          <h2 className="text-3xl font-black text-center text-purple-900 mb-6 flex items-center justify-center gap-3">
            <span className="text-4xl">📊</span>
            WSZYSTKIE STATYSTYKI KOŃCOWE
          </h2>
          
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {/* Zdrowie i samopoczucie */}
            <div className="bg-gradient-to-br from-red-50 to-white rounded-2xl p-5 border-2 border-red-300">
              <h3 className="text-lg font-black text-red-900 mb-4 flex items-center gap-2">
                <span className="text-2xl">❤️</span>
                Zdrowie
              </h3>
              <DetailStatBar label="Zdrowie fizyczne" value={session.physical_health} color="bg-red-500" />
              <DetailStatBar label="Zdrowie psychiczne" value={session.mental_health} color="bg-pink-500" />
              <DetailStatBar label="Szczęście" value={session.happiness} color="bg-yellow-500" />
              <DetailStatBar label="Poziom stresu" value={10 - session.stress_level} color="bg-orange-500" />
            </div>

            {/* Work-Life Balance */}
            <div className="bg-gradient-to-br from-blue-50 to-white rounded-2xl p-5 border-2 border-blue-300">
              <h3 className="text-lg font-black text-blue-900 mb-4 flex items-center gap-2">
                <span className="text-2xl">⚖️</span>
                Work-Life
              </h3>
              <DetailStatBar label="Satysfakcja z kariery" value={session.career_satisfaction} color="bg-blue-600" />
              <DetailStatBar label="Równowaga praca-życie" value={session.work_life_balance} color="bg-blue-500" />
              <DetailStatBar label="Wolny czas" value={session.free_time} color="bg-cyan-500" />
              <DetailStatBar label="Relacje rodzinne" value={session.relationship_quality} color="bg-indigo-500" />
            </div>

            {/* Rozwój osobisty */}
            <div className="bg-gradient-to-br from-purple-50 to-white rounded-2xl p-5 border-2 border-purple-300">
              <h3 className="text-lg font-black text-purple-900 mb-4 flex items-center gap-2">
                <span className="text-2xl">🌱</span>
                Rozwój
              </h3>
              <DetailStatBar label="Rozwój osobisty" value={session.personal_growth} color="bg-purple-600" />
              <DetailStatBar label="Samoocena" value={session.self_esteem} color="bg-purple-500" />
              <DetailStatBar label="Cel życiowy" value={session.life_purpose} color="bg-violet-500" />
              <DetailStatBar label="Więzi społeczne" value={session.social_connections} color="bg-fuchsia-500" />
            </div>

            {/* Dodatkowe statystyki */}
            <div className="bg-gradient-to-br from-green-50 to-white rounded-2xl p-5 border-2 border-green-300">
              <h3 className="text-lg font-black text-green-900 mb-4 flex items-center gap-2">
                <span className="text-2xl">💼</span>
                Kariera
              </h3>
              <DetailStatBar label="Bezpieczeństwo finansowe" value={session.financial_security} color="bg-green-600" />
              <div className="mt-2 text-sm text-gray-700 bg-white rounded-lg p-2 border">
                <strong>Miesięczny dochód:</strong><br/>
                {formatCurrency(session.income)}
              </div>
            </div>

            <div className="bg-gradient-to-br from-yellow-50 to-white rounded-2xl p-5 border-2 border-yellow-300">
              <h3 className="text-lg font-black text-yellow-900 mb-4 flex items-center gap-2">
                <span className="text-2xl">📚</span>
                Edukacja
              </h3>
              <div className="space-y-2 text-sm">
                <div className="bg-white rounded-lg p-3 border">
                  <strong>Poziom wykształcenia:</strong><br/>
                  {session.education_level || session.education}
                </div>
                <div className="bg-white rounded-lg p-3 border">
                  <strong>Etap życia:</strong><br/>
                  {session.life_stage}
                </div>
              </div>
            </div>

            <div className="bg-gradient-to-br from-orange-50 to-white rounded-2xl p-5 border-2 border-orange-300">
              <h3 className="text-lg font-black text-orange-900 mb-4 flex items-center gap-2">
                <span className="text-2xl">👔</span>
                Zatrudnienie
              </h3>
              <div className="space-y-2 text-sm">
                <div className="bg-white rounded-lg p-3 border">
                  <strong>Typ umowy:</strong><br/>
                  {session.type_employment || 'Brak'}
                </div>
                <div className="bg-white rounded-lg p-3 border">
                  <strong>Stanowisko:</strong><br/>
                  {session.work || 'Brak pracy'}
                </div>
              </div>
            </div>
          </div>
        </div>

        {/* Przyciski akcji - gaming style */}
        <div className="flex flex-wrap justify-center gap-4 mb-6">
          <button
            onClick={() => {
              localStorage.removeItem('activeSessionId');
              navigate('/game');
            }}
            className="bg-gradient-to-r from-green-600 to-emerald-600 hover:from-green-500 hover:to-emerald-500 text-white font-black text-xl px-10 py-4 rounded-2xl shadow-2xl transition transform hover:scale-105 border-2 border-green-400"
          >
            🎮 ZAGRAJ PONOWNIE
          </button>
          <button
            onClick={() => {
              localStorage.removeItem('token');
              localStorage.removeItem('activeSessionId');
              navigate('/login');
            }}
            className="bg-gradient-to-r from-red-600 to-orange-600 hover:from-red-500 hover:to-orange-500 text-white font-black text-xl px-10 py-4 rounded-2xl shadow-2xl transition transform hover:scale-105 border-2 border-red-400"
          >
            🚪 WYLOGUJ SIĘ
          </button>
        </div>

        {/* Podsumowanie edukacyjne - gaming style */}
        <div className="bg-gradient-to-br from-zus-yellow via-yellow-300 to-orange-300 rounded-3xl p-8 shadow-2xl border-4 border-yellow-500">
          <h3 className="text-3xl font-black text-zus-dark-blue mb-6 text-center flex items-center justify-center gap-3">
            <span className="text-4xl">📚</span>
            WNIOSKI Z GRY - CO ZAPAMIĘTAĆ?
          </h3>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div className="bg-white bg-opacity-90 rounded-xl p-4 border-2 border-green-500">
              <div className="flex items-start gap-3">
                <span className="text-3xl">💰</span>
                <div>
                  <strong className="text-green-700 text-lg">Oszczędzaj regularnie!</strong>
                  <p className="text-sm text-gray-700 mt-1">Składki ZUS to podstawa, ale dodatkowe oszczędności dają bezpieczeństwo.</p>
                </div>
              </div>
            </div>
            
            <div className="bg-white bg-opacity-90 rounded-xl p-4 border-2 border-red-500">
              <div className="flex items-start gap-3">
                <span className="text-3xl">❤️</span>
                <div>
                  <strong className="text-red-700 text-lg">Dbaj o zdrowie!</strong>
                  <p className="text-sm text-gray-700 mt-1">Zdrowie to fundament - bez niego pieniądze nie pomogą.</p>
                </div>
              </div>
            </div>
            
            <div className="bg-white bg-opacity-90 rounded-xl p-4 border-2 border-blue-500">
              <div className="flex items-start gap-3">
                <span className="text-3xl">⚖️</span>
                <div>
                  <strong className="text-blue-700 text-lg">Równowaga to klucz!</strong>
                  <p className="text-sm text-gray-700 mt-1">Work-life balance wpływa na szczęście i produktywność.</p>
                </div>
              </div>
            </div>
            
            <div className="bg-white bg-opacity-90 rounded-xl p-4 border-2 border-purple-500">
              <div className="flex items-start gap-3">
                <span className="text-3xl">📚</span>
                <div>
                  <strong className="text-purple-700 text-lg">Inwestuj w siebie!</strong>
                  <p className="text-sm text-gray-700 mt-1">Edukacja otwiera drzwi do lepszych możliwości zawodowych.</p>
                </div>
              </div>
            </div>
            
            <div className="bg-white bg-opacity-90 rounded-xl p-4 border-2 border-orange-500">
              <div className="flex items-start gap-3">
                <span className="text-3xl">⏰</span>
                <div>
                  <strong className="text-orange-700 text-lg">Nie zwlekaj!</strong>
                  <p className="text-sm text-gray-700 mt-1">Im wcześniej zaczniesz planować, tym lepsza emerytura.</p>
                </div>
              </div>
            </div>
            
            <div className="bg-white bg-opacity-90 rounded-xl p-4 border-2 border-pink-500">
              <div className="flex items-start gap-3">
                <span className="text-3xl">👨‍👩‍👧‍👦</span>
                <div>
                  <strong className="text-pink-700 text-lg">Relacje mają znaczenie!</strong>
                  <p className="text-sm text-gray-700 mt-1">Rodzina i przyjaciele to wsparcie w trudnych chwilach.</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

// Komponent pomocniczy dla statystyk - duże karty
function StatCard({ label, value, icon }) {
  const percentage = (value / 10) * 100;
  const getColor = () => {
    if (value >= 7) return { bg: 'bg-green-500', border: 'border-green-400', text: 'text-green-600' };
    if (value >= 4) return { bg: 'bg-yellow-500', border: 'border-yellow-400', text: 'text-yellow-600' };
    return { bg: 'bg-red-500', border: 'border-red-400', text: 'text-red-600' };
  };
  const color = getColor();

  return (
    <div className={`bg-white rounded-2xl p-5 text-center shadow-lg border-4 ${color.border}`}>
      <div className="text-5xl mb-3">{icon}</div>
      <div className="text-sm text-gray-600 mb-2 font-semibold uppercase tracking-wide">{label}</div>
      <div className={`text-4xl font-black mb-3 ${color.text}`}>{value}/10</div>
      <div className="w-full bg-gray-200 rounded-full h-3 overflow-hidden">
        <div
          className={`${color.bg} h-3 rounded-full transition-all shadow-inner`}
          style={{ width: `${percentage}%` }}
        ></div>
      </div>
    </div>
  );
}

// Komponent pomocniczy dla szczegółowych statystyk
function DetailStatBar({ label, value, color }) {
  const percentage = (value / 10) * 100;
  
  return (
    <div className="mb-3">
      <div className="flex justify-between text-sm mb-1">
        <span className="font-semibold text-gray-700">{label}</span>
        <span className="font-bold text-gray-900">{value}/10</span>
      </div>
      <div className="w-full bg-gray-200 rounded-full h-2 overflow-hidden">
        <div
          className={`${color} h-2 rounded-full transition-all`}
          style={{ width: `${percentage}%` }}
        ></div>
      </div>
    </div>
  );
}

export default Results;
