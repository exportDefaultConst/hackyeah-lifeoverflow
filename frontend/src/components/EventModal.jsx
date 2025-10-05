/**
 * Modal z wydarzeniem życiowym
 */
import React from 'react';

function EventModal({ event, onChoice, onClose }) {
  if (!event) return null;

  const handleChoice = (index) => {
    onChoice(index);
    // Modal zamknie się automatycznie po wyborze
  };

  // Zapobiega zamknięciu gdy klikamy na tło
  const handleBackdropClick = (e) => {
    // Nie zamykaj - wymagamy podjęcia decyzji
    e.stopPropagation();
  };

  return (
    <div 
      className="fixed inset-0 bg-black bg-opacity-70 flex items-center justify-center z-50 p-2 sm:p-4 backdrop-blur-sm"
      onClick={handleBackdropClick}
    >
      <div className="bg-gradient-to-br from-white to-gray-100 rounded-2xl sm:rounded-3xl max-w-3xl w-full max-h-[90vh] overflow-y-auto shadow-2xl border-2 sm:border-4 border-zus-yellow">
        {/* Nagłówek - gaming style */}
        <div className="bg-gradient-to-r from-zus-blue via-blue-600 to-zus-dark-blue text-white p-4 sm:p-6 rounded-t-2xl sm:rounded-t-3xl border-b-2 sm:border-b-4 border-zus-yellow">
          <div className="flex justify-between items-start gap-2">
            <div className="flex-1 min-w-0">
              <div className="text-xs sm:text-sm opacity-90 mb-1 font-bold uppercase tracking-wider">
                {event.event_type === 'ai_generated' ? '🤖 AI' : '📋 Wydarzenie'}
              </div>
              <h2 className="text-xl sm:text-3xl font-black tracking-tight truncate">{event.event_name}</h2>
            </div>
            {/* Wskazówka zamiast przycisku X */}
            <div className="bg-zus-yellow text-zus-dark-blue text-xs sm:text-sm font-black px-2 sm:px-4 py-1 sm:py-2 rounded-lg sm:rounded-xl shadow-lg animate-pulse whitespace-nowrap">
              Wybierz ↓
            </div>
          </div>
        </div>

        {/* Opis - lepszy design */}
        <div className="p-4 sm:p-8">
          <div className="bg-gradient-to-br from-blue-50 to-purple-50 rounded-xl sm:rounded-2xl p-4 sm:p-6 mb-4 sm:mb-6 border border-blue-200 sm:border-2 shadow-inner">
            <p className="text-gray-800 text-sm sm:text-lg leading-relaxed font-medium">
              {event.description}
            </p>
          </div>

          {/* Opcje wyboru - gaming style */}
          <div className="space-y-3 sm:space-y-4">
            <h3 className="text-lg sm:text-2xl font-black text-gray-900 mb-3 sm:mb-4 flex items-center gap-2">
              <span className="text-2xl sm:text-3xl">🎯</span>
              <span className="text-sm sm:text-base">Co chcesz zrobić?</span>
            </h3>
            {event.choices && event.choices.map((choice, index) => (
              <button
                key={index}
                onClick={() => handleChoice(index)}
                className="w-full text-left bg-white border-2 sm:border-4 border-gray-300 hover:border-zus-blue hover:bg-gradient-to-br hover:from-blue-50 hover:to-white rounded-xl sm:rounded-2xl p-3 sm:p-5 transition-all duration-200 group shadow-lg hover:shadow-2xl transform hover:scale-102"
              >
                <div className="flex items-start justify-between gap-2">
                  <div className="flex-1 min-w-0">
                    <div className="font-bold text-gray-900 mb-2 sm:mb-3 group-hover:text-zus-blue text-sm sm:text-lg">
                      {choice.text}
                    </div>
                    {choice.impacts && Object.keys(choice.impacts).length > 0 && (
                      <div className="flex flex-wrap gap-1 sm:gap-2 mt-2">
                        {Object.entries(choice.impacts).map(([key, value]) => {
                          const isPositive = typeof value === 'number' ? value > 0 : false;
                          const isNegative = typeof value === 'number' ? value < 0 : false;
                          
                          return (
                            <span
                              key={key}
                              className={`text-xs sm:text-sm font-bold px-2 sm:px-3 py-1 rounded-md sm:rounded-lg shadow-sm ${
                                isPositive
                                  ? 'bg-gradient-to-r from-green-500 to-emerald-500 text-white'
                                  : isNegative
                                  ? 'bg-gradient-to-r from-red-500 to-orange-500 text-white'
                                  : 'bg-gradient-to-r from-gray-400 to-gray-500 text-white'
                              }`}
                            >
                              {translateStatName(key)}: {formatImpact(value)}
                            </span>
                          );
                        })}
                      </div>
                    )}
                  </div>
                  <div className="ml-2 sm:ml-4 text-zus-blue group-hover:translate-x-2 transition-transform text-xl sm:text-3xl flex-shrink-0">
                    ▶
                  </div>
                </div>
              </button>
            ))}
          </div>

          {/* Info */}
          <div className="mt-4 sm:mt-6 text-center text-xs sm:text-sm text-gray-500">
            <p>💡 Każda decyzja ma konsekwencje. Wybieraj mądrze!</p>
          </div>
        </div>
      </div>
    </div>
  );
}

// Pomocnicze funkcje
function translateStatName(key) {
  const translations = {
    health: 'Zdrowie',
    mental_health: 'Zdrowie psychiczne',
    savings: 'Oszczędności',
    income: 'Dochód',
    happiness: 'Szczęście',
    stress_level: 'Stres',
    career_satisfaction: 'Kariera',
    work_life_balance: 'Work-life',
    free_time: 'Wolny czas',
    financial_security: 'Bezpieczeństwo fin.',
    personal_growth: 'Rozwój',
    self_esteem: 'Samoocena',
    relationship_quality: 'Relacje',
    physical_health: 'Zdrowie fizyczne',
    children: 'Dzieci',
    education_level: 'Wykształcenie',
    family_satisfaction: 'Rodzina',
    family_support: 'Wsparcie rodziny',
    social_connections: 'Znajomości',
    emotional_wellbeing: 'Samopoczucie',
    life_purpose: 'Cel życia',
    community_involvement: 'Społeczność',
    spirituality: 'Duchowość',
    monthly_costs: 'Koszty miesięczne',
    has_apartment: 'Mieszkanie',
    has_job: 'Praca',
    student: 'Student',
    work: 'Zawód',
    type_employment: 'Typ umowy',
    marital_status: 'Stan cywilny',
    job_count: 'Dodatkowe prace',
  };
  return translations[key] || key;
}

function formatImpact(value) {
  if (typeof value === 'number') {
    return value > 0 ? `+${value}` : value;
  }
  return value;
}

export default EventModal;
