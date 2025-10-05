/**
 * Komponent awatara postaci - używa obrazków z assets/
 * Obrazki: gender + wiek + nastrój (male1.png, woman2h.png, male3s.png)
 */
import React from 'react';

function CharacterAvatar({ age, sex, happiness, health }) {
  // Określ kategorię wieku (1=młody, 2=średni, 3=stary)
  const getAgeCategory = () => {
    if (age < 30) return '1';
    if (age < 50) return '2';
    return '3';
  };

  // Określ nastrój (h=happy, s=sad, brak=neutral)
  const getMood = () => {
    if (happiness > 7) return 'h';
    if (happiness < 4) return 's';
    return '';
  };

  // Określ stan zdrowia (kolor obramowania)
  const getHealthBorder = () => {
    if (health > 7) return 'border-green-400';
    if (health > 4) return 'border-yellow-400';
    return 'border-red-400';
  };

  // Generuj ścieżkę do obrazka
  const getImagePath = () => {
    const gender = sex === 'male' ? 'male' : 'woman';
    const ageNum = getAgeCategory();
    const mood = getMood();
    // Używamy bezpośredniej ścieżki do assets
    try {
      return new URL(`../assets/${gender}${ageNum}${mood}.png`, import.meta.url).href;
    } catch (error) {
      // Fallback do podstawowego obrazka
      return new URL(`../assets/${gender}1.png`, import.meta.url).href;
    }
  };

  return (
    <div className={`bg-gradient-to-br from-white to-gray-50 rounded-xl sm:rounded-2xl border-2 sm:border-4 ${getHealthBorder()} shadow-xl overflow-hidden`}>
      {/* Obrazek awatara - wyższy dla ratio 324x774 */}
      <div className="relative h-64 sm:h-96 flex items-end justify-center bg-gradient-to-b from-blue-50 to-transparent overflow-hidden">
        <img 
          src={getImagePath()} 
          alt="Awatar postaci"
          className="h-full w-auto object-contain drop-shadow-2xl"
          onError={(e) => {
            // Fallback jeśli obrazek nie istnieje - spróbuj bez nastroju
            const gender = sex === 'male' ? 'male' : 'woman';
            const ageNum = getAgeCategory();
            e.target.onerror = null; // Zapobiega pętli
            e.target.src = new URL(`../assets/${gender}${ageNum}.png`, import.meta.url).href;
          }}
        />
      </div>
      
      {/* Info pod awatarem */}
      <div className="p-3 sm:p-4 bg-white border-t border-gray-200 sm:border-t-2">
        <div className="text-center mb-2 sm:mb-3">
          <div className="text-lg sm:text-2xl font-bold text-gray-800">
            {sex === 'male' ? '👨' : '👩'} <span className="hidden sm:inline">{sex === 'male' ? 'Mężczyzna' : 'Kobieta'},</span> {age} lat
          </div>
        </div>
        
        {/* Pasek zdrowia i szczęścia */}
        <div className="grid grid-cols-2 gap-2 sm:gap-3">
          <div className="bg-gradient-to-br from-red-50 to-white rounded-lg sm:rounded-xl p-2 sm:p-3 border border-red-200">
            <div className="text-xs font-semibold text-red-700 mb-1">❤️ <span className="hidden sm:inline">Zdrowie</span></div>
            {/* health rounded to 1 decimal place */}
            <div className="text-2xl sm:text-3xl font-bold text-red-600">{health.toFixed(1)}/10</div>
          </div>
          <div className="bg-gradient-to-br from-yellow-50 to-white rounded-lg sm:rounded-xl p-2 sm:p-3 border border-yellow-200">
            <div className="text-xs font-semibold text-yellow-700 mb-1">😊 <span className="hidden sm:inline">Szczęście</span></div>
            <div className="text-2xl sm:text-3xl font-bold text-yellow-600">{happiness.toFixed(1)}/10</div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default CharacterAvatar;
