/**
 * Komponent wyświetlający radę od Wujka Dobrej Rady
 */
import React, { useState, useEffect } from 'react';
import { advisorAPI } from '../utils/api';

function WujekAdvice({ sessionId, trigger }) {
  const [advice, setAdvice] = useState('');
  const [loading, setLoading] = useState(false);
  const [visible, setVisible] = useState(false);

  useEffect(() => {
    if (trigger && sessionId) {
      fetchAdvice();
    }
  }, [trigger, sessionId]);

  const fetchAdvice = async () => {
    setLoading(true);
    try {
      const response = await advisorAPI.getAdvice(sessionId);
      setAdvice(response.data.advice);
      setVisible(true);
      
      // Auto-hide po 15 sekundach
      setTimeout(() => {
        setVisible(false);
      }, 15000);
    } catch (error) {
      console.error('Błąd pobierania rady:', error);
      setAdvice('Wujek Dobra Rada jest chwilowo niedostępny. Spróbuj później.');
      setVisible(true);
    } finally {
      setLoading(false);
    }
  };

  if (!visible && !loading) return null;

  return (
    <div className="fixed bottom-2 sm:bottom-4 right-2 sm:right-4 max-w-[95vw] sm:max-w-md z-40 animate-slide-in">
      <div className="bg-gradient-to-br from-zus-yellow to-yellow-300 rounded-lg sm:rounded-xl shadow-2xl p-4 sm:p-6 border-2 sm:border-4 border-zus-dark-blue">
        {/* Nagłówek */}
        <div className="flex items-center justify-between mb-3 sm:mb-4">
          <div className="flex items-center space-x-2 sm:space-x-3 flex-1 min-w-0">
            <div className="text-2xl sm:text-4xl flex-shrink-0">👴</div>
            <div className="min-w-0 flex-1">
              <div className="font-bold text-zus-dark-blue text-sm sm:text-lg truncate">
                Wujek Dobra Rada
              </div>
              <div className="text-xs sm:text-sm text-gray-700 truncate">
                Twój doradca
              </div>
            </div>
          </div>
          <button
            onClick={() => setVisible(false)}
            className="text-zus-dark-blue hover:text-gray-700 text-xl sm:text-2xl flex-shrink-0 ml-2"
          >
            ×
          </button>
        </div>

        {/* Treść */}
        <div className="bg-white bg-opacity-80 rounded-lg p-3 sm:p-4">
          {loading ? (
            <div className="text-center text-gray-600">
              <div className="animate-pulse text-sm sm:text-base">Wujek myśli...</div>
            </div>
          ) : (
            <p className="text-gray-800 leading-relaxed text-sm sm:text-base">
              {advice}
            </p>
          )}
        </div>

        {/* Stopka */}
        <div className="mt-2 sm:mt-3 text-xs text-center text-zus-dark-blue opacity-75">
          💡 Rada od Wujka Dobrej Rady
        </div>
      </div>
    </div>
  );
}

export default WujekAdvice;
