/**
 * Panel statystyk - pokazuje TYLKO średnie zgrupowane, szczegóły na końcu gry
 */
import React, { useState, useEffect } from 'react';

// Porady emerytalne - pokazujemy tylko 1 losową
const PENSION_TIPS = [
  {
    icon: '💼',
    title: 'Wiek emerytalny',
    text: 'Kobiety: 60 lat, Mężczyźni: 65 lat (wymaga min. 20/25 lat składek)',
    color: 'border-zus-blue'
  },
  {
    icon: '💰',
    title: 'Składka emerytalna',
    text: '19,52% wynagrodzenia brutto trafia na Twoje indywidualne konto w ZUS',
    color: 'border-zus-green'
  },
  {
    icon: '📈',
    title: 'Kapitał początkowy',
    text: 'Składki sprzed 1999 r. są przeliczane i doliczane do kapitału',
    color: 'border-zus-yellow'
  },
  {
    icon: '⏱️',
    title: 'Dalsze zatrudnienie',
    text: 'Możesz pracować po osiągnięciu wieku emerytalnego i zwiększać kapitał',
    color: 'border-orange-400'
  },
  {
    icon: '⚠️',
    title: 'Wzór na emeryturę',
    text: 'Emerytura = kapitał ÷ średnie dalsze trwanie życia. Im dłużej odkładasz, tym wyższa!',
    color: 'border-red-400'
  },
  {
    icon: '🏢',
    title: 'Rodzaje umów',
    text: 'Umowa o pracę daje najwyższe składki ZUS. Zlecenie i B2B często mają niższe składki.',
    color: 'border-purple-400'
  },
  {
    icon: '💡',
    title: 'Dodatkowe oszczędzanie',
    text: 'PPK i IKE to dodatkowe sposoby oszczędzania na emeryturę z korzyściami podatkowymi.',
    color: 'border-blue-400'
  }
];

function StatsPanel({ session }) {
  const [currentTip, setCurrentTip] = useState(null);

  // Wybierz losową poradę przy pierwszym renderowaniu
  useEffect(() => {
    const randomTip = PENSION_TIPS[Math.floor(Math.random() * PENSION_TIPS.length)];
    setCurrentTip(randomTip);
  }, [session?.age]); // Zmień poradę gdy zmieni się wiek

  if (!session) return null;

  const formatCurrency = (value) => {
    return new Intl.NumberFormat('pl-PL', {
      style: 'currency',
      currency: 'PLN',
      minimumFractionDigits: 0,
      maximumFractionDigits: 0,
    }).format(value);
  };

  // Oblicz średnie dla głównych kategorii
  const calculateAverages = () => {
    const health = Math.round((session.physical_health + session.mental_health) / 2);
    const wellbeing = Math.round((session.happiness + (10 - session.stress_level)) / 2);
    const workLife = Math.round((session.career_satisfaction + session.work_life_balance + session.free_time) / 3);
    const personal = Math.round((session.personal_growth + session.self_esteem + session.life_purpose + session.social_connections) / 4);
    
    return { health, wellbeing, workLife, personal };
  };

  const averages = calculateAverages();

  // Komponenty dla pojedynczej statystyki
  const StatBar = ({ label, value, max = 10, color = 'blue', icon }) => {
    const percentage = (value / max) * 100;
    const colorClass = {
      blue: 'bg-zus-blue',
      green: 'bg-zus-green',
      yellow: 'bg-zus-yellow',
      red: 'bg-red-500',
      purple: 'bg-purple-500',
      orange: 'bg-orange-500',
    }[color] || 'bg-gray-400';

    return (
      <div className="mb-3">
        <div className="flex justify-between items-center mb-1">
          <span className="font-medium text-gray-700 flex items-center gap-2">
            <span className="text-xl">{icon}</span>
            {label}
          </span>
          <span className="text-lg font-bold text-gray-800">{value}/{max}</span>
        </div>
        <div className="stat-bar">
          <div 
            className={`stat-fill ${colorClass}`}
            style={{ width: `${percentage}%` }}
          ></div>
        </div>
      </div>
    );
  };

  return (
    <div className="space-y-3 sm:space-y-4">
      {/* Podstawowe info - kompaktowe */}
      <div className="bg-gradient-to-br from-blue-50 to-white rounded-xl sm:rounded-2xl p-3 sm:p-4 shadow-lg border-2 border-blue-200">
        <h3 className="text-base sm:text-lg font-bold text-zus-dark-blue mb-2 sm:mb-3 flex items-center gap-2">
          <span className="text-xl sm:text-2xl">📋</span>
          <span className="text-sm sm:text-base">Podstawowe Info</span>
        </h3>
        <div className="grid grid-cols-2 gap-2 text-xs sm:text-sm">
          <div className="bg-white bg-opacity-60 rounded-lg p-2">
            <span className="text-gray-600 text-xs">Praca</span>
            <div className="font-semibold text-gray-800 truncate">{session.work || 'Brak'}</div>
          </div>
          <div className="bg-white bg-opacity-60 rounded-lg p-2">
            <span className="text-gray-600 text-xs">Wykształcenie</span>
            <div className="font-semibold text-gray-800 truncate">{session.education_level || session.education}</div>
          </div>
          <div className="bg-white bg-opacity-60 rounded-lg p-2">
            <span className="text-gray-600 text-xs">Stan cywilny</span>
            <div className="font-semibold text-gray-800 truncate">
              {session.marital_status === 'single' ? 'Singiel' : session.marital_status}
            </div>
          </div>
          <div className="bg-white bg-opacity-60 rounded-lg p-2">
            <span className="text-gray-600 text-xs">Dzieci</span>
            <div className="font-semibold text-gray-800">{session.children}</div>
          </div>
        </div>
      </div>

      {/* Zgrupowane średnie statystyki */}
      <div className="bg-gradient-to-br from-purple-50 to-white rounded-xl sm:rounded-2xl p-4 sm:p-5 shadow-lg border-2 border-purple-300">
        <h3 className="text-lg sm:text-xl font-bold text-zus-dark-blue mb-3 sm:mb-4 flex items-center gap-2">
          <span className="text-2xl sm:text-3xl">📊</span>
          <span className="text-sm sm:text-base">Stan Ogólny</span>
        </h3>
        <StatBar label="Zdrowie" value={averages.health} color="red" icon="❤️" />
        <StatBar label="Samopoczucie" value={averages.wellbeing} color="yellow" icon="😊" />
        <StatBar label="Work-Life Balance" value={averages.workLife} color="blue" icon="⚖️" />
        <StatBar label="Rozwój osobisty" value={averages.personal} color="purple" icon="🌱" />
      </div>

      {/* Porady prawne ZUS - pokazuje 1 losową */}
      <div className="bg-gradient-to-br from-yellow-50 to-white rounded-xl sm:rounded-2xl p-4 sm:p-5 shadow-lg border-2 border-yellow-300">
        <h3 className="text-base sm:text-lg font-bold text-zus-dark-blue mb-3 flex items-center gap-2">
          <span className="text-xl sm:text-2xl">⚖️</span>
          <span className="text-sm sm:text-base">💡 Porada emerytalna</span>
        </h3>
        {currentTip && (
          <div className={`bg-white bg-opacity-60 rounded-lg p-3 sm:p-4 border-l-4 ${currentTip.color}`}>
            <strong className="text-zus-dark-blue text-sm sm:text-base flex items-center gap-2">
              <span>{currentTip.icon}</span>
              {currentTip.title}:
            </strong>
            <p className="mt-2 text-xs sm:text-sm text-gray-700">{currentTip.text}</p>
          </div>
        )}
        <div className="mt-3 text-xs text-center text-gray-500">
          💡 Porada zmienia się co rok
        </div>
      </div>
    </div>
  );
}

export default StatsPanel;
