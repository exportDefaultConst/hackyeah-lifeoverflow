import React from 'react';

/**
 * ExpenseTracker - wyświetla podsumowanie dochodów i wydatków
 */
export default function ExpenseTracker({ session }) {
  if (!session) return null;

  const monthlyIncome = session.has_job ? session.income : 0;
  const monthlyCosts = session.monthly_costs || 0;
  const monthlyBalance = monthlyIncome - monthlyCosts;
  const yearlyBalance = monthlyBalance * 12;

  const formatCurrency = (value) => {
    return new Intl.NumberFormat('pl-PL', {
      style: 'currency',
      currency: 'PLN',
      minimumFractionDigits: 0,
      maximumFractionDigits: 0,
    }).format(value);
  };

  return (
    <div className="bg-gradient-to-br from-slate-800 to-slate-900 rounded-2xl p-4 sm:p-5 shadow-2xl border-2 border-slate-700">
      <h3 className="text-lg sm:text-xl font-black text-white mb-3 sm:mb-4 flex items-center gap-2 uppercase tracking-wide">
        <span className="text-xl sm:text-2xl">💰</span>
        <span className="text-sm sm:text-base">Bilans finansowy</span>
      </h3>
      
      <div className="space-y-2">
        {/* Dochód miesięczny */}
        <div className="flex justify-between items-center p-2 sm:p-3 bg-slate-700/50 rounded-lg">
          <div className="flex items-center gap-2">
            <span className="text-lg sm:text-xl">📈</span>
            <span className="text-slate-300 text-xs sm:text-sm font-medium">Dochód miesięczny:</span>
          </div>
          <span className="text-green-400 font-bold text-sm sm:text-base">
            {formatCurrency(monthlyIncome)}
          </span>
        </div>

        {/* Koszty miesięczne */}
        <div className="flex justify-between items-center p-2 sm:p-3 bg-slate-700/50 rounded-lg">
          <div className="flex items-center gap-2">
            <span className="text-lg sm:text-xl">📉</span>
            <span className="text-slate-300 text-xs sm:text-sm font-medium">Koszty miesięczne:</span>
          </div>
          <span className="text-red-400 font-bold text-sm sm:text-base">
            {formatCurrency(-monthlyCosts)}
          </span>
        </div>

        {/* Bilans miesięczny */}
        <div className={`flex justify-between items-center p-2 sm:p-3 rounded-lg border-2 ${monthlyBalance >= 0 ? 'bg-green-900/30 border-green-500' : 'bg-red-900/30 border-red-500'}`}>
          <div className="flex items-center gap-2">
            <span className="text-lg sm:text-xl">💵</span>
            <span className="text-white text-xs sm:text-sm font-bold">Bilans miesięczny:</span>
          </div>
          <span className={`font-bold text-sm sm:text-base ${monthlyBalance >= 0 ? 'text-green-300' : 'text-red-300'}`}>
            {monthlyBalance >= 0 ? '+' : ''}{formatCurrency(monthlyBalance)}
          </span>
        </div>

        {/* Prognoza roczna */}
        <div className={`flex justify-between items-center p-2 sm:p-3 rounded-lg border-2 ${yearlyBalance >= 0 ? 'bg-green-900/30 border-green-500' : 'bg-red-900/30 border-red-500'}`}>
          <div className="flex items-center gap-2">
            <span className="text-lg sm:text-xl">📊</span>
            <span className="text-white text-xs sm:text-sm font-bold">Prognoza roczna:</span>
          </div>
          <span className={`font-bold text-sm sm:text-base ${yearlyBalance >= 0 ? 'text-green-300' : 'text-red-300'}`}>
            {yearlyBalance >= 0 ? '+' : ''}{formatCurrency(yearlyBalance)}
          </span>
        </div>
      </div>

      {/* Ostrzeżenia */}
      <div className="mt-3 space-y-2">
        {!session.has_job && monthlyIncome === 0 && (
          <div className="p-2 bg-yellow-900/50 border-l-4 border-yellow-500 rounded">
            <p className="text-yellow-200 text-xs sm:text-sm font-medium">
              ⚠️ Nie masz pracy - nie zarabiasz!
            </p>
          </div>
        )}

        {monthlyBalance < 0 && (
          <div className="p-2 bg-red-900/50 border-l-4 border-red-500 rounded">
            <p className="text-red-200 text-xs sm:text-sm font-medium">
              🚨 Wydajesz więcej niż zarabiasz!
            </p>
          </div>
        )}

        {session.savings < 0 && (
          <div className="p-2 bg-orange-900/50 border-l-4 border-orange-500 rounded">
            <p className="text-orange-200 text-xs sm:text-sm font-medium">
              💳 Jesteś na minusie: {formatCurrency(session.savings)}
            </p>
          </div>
        )}
      </div>
    </div>
  );
}
