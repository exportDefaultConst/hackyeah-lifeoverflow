/**
 * Strona logowania i rejestracji
 */
import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { authAPI } from '../utils/api';
import logoImage from '../assets/logo.png';

function Login({ setIsAuthenticated }) {
  const [isLogin, setIsLogin] = useState(true);
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
    setLoading(true);

    try {
      const response = isLogin 
        ? await authAPI.login(email, password)
        : await authAPI.register(email, password);

      const { token } = response.data;
      localStorage.setItem('token', token);
      setIsAuthenticated(true);
      navigate('/game');
    } catch (err) {
      setError(err.response?.data?.error || 'Wystąpił błąd. Spróbuj ponownie.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-slate-900 via-blue-900 to-slate-800 p-4">
      <div className="max-w-md w-full space-y-8">
        {/* Logo i tytuł - gaming style */}
        <div className="text-center">
          <div className="mb-6 flex justify-center">
            <div className="bg-gradient-to-br from-zus-yellow to-orange-400 rounded-3xl p-6 shadow-2xl border-4 border-yellow-300">
              <img src={logoImage} alt="Logo" className="w-[100px] h-[100px] object-contain" />
            </div>
          </div>
          <h1 className="text-5xl font-black text-white mb-3 tracking-tight">
            LIFEOVERFLOW
          </h1>
          <p className="text-zus-yellow text-xl font-bold">
            Planowanie Emerytalne ZUS
          </p>
          <p className="text-blue-300 text-sm mt-2">
            Symuluj życie, podejmuj decyzje, planuj przyszłość!
          </p>
        </div>

        {/* Formularz - nowoczesny */}
        <div className="bg-gradient-to-br from-white to-gray-100 rounded-3xl shadow-2xl p-8 border-4 border-zus-yellow">
          <div className="mb-6">
            <div className="flex bg-gray-200 rounded-xl p-1">
              <button
                className={`flex-1 py-3 font-bold rounded-lg transition-all ${
                  isLogin 
                    ? 'bg-gradient-to-r from-zus-blue to-zus-dark-blue text-white shadow-lg' 
                    : 'text-gray-600 hover:text-gray-800'
                }`}
                onClick={() => setIsLogin(true)}
              >
                Logowanie
              </button>
              <button
                className={`flex-1 py-3 font-bold rounded-lg transition-all ${
                  !isLogin 
                    ? 'bg-gradient-to-r from-zus-blue to-zus-dark-blue text-white shadow-lg' 
                    : 'text-gray-600 hover:text-gray-800'
                }`}
                onClick={() => setIsLogin(false)}
              >
                Rejestracja
              </button>
            </div>
          </div>

          <form onSubmit={handleSubmit} className="space-y-5">
            {error && (
              <div className="bg-gradient-to-r from-red-600 to-red-500 text-white px-5 py-4 rounded-xl font-semibold border-2 border-red-400 shadow-lg">
                ⚠️ {error}
              </div>
            )}

            <div>
              <label htmlFor="email" className="block text-sm font-bold text-gray-800 mb-2 uppercase tracking-wide">
                📧 Email
              </label>
              <input
                id="email"
                type="email"
                required
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                className="w-full px-5 py-3 border-2 border-gray-300 rounded-xl focus:ring-4 focus:ring-zus-blue focus:border-zus-blue text-lg font-semibold"
                placeholder="twoj@email.pl"
              />
            </div>

            <div>
              <label htmlFor="password" className="block text-sm font-bold text-gray-800 mb-2 uppercase tracking-wide">
                🔒 Hasło
              </label>
              <input
                id="password"
                type="password"
                required
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                className="w-full px-5 py-3 border-2 border-gray-300 rounded-xl focus:ring-4 focus:ring-zus-blue focus:border-zus-blue text-lg font-semibold"
                placeholder="••••••••"
                minLength={6}
              />
              <p className="text-xs text-gray-500 mt-1">Minimum 6 znaków</p>
            </div>

            <button
              type="submit"
              disabled={loading}
              className="w-full bg-gradient-to-r from-green-600 to-emerald-600 hover:from-green-500 hover:to-emerald-500 text-white font-black text-xl py-4 rounded-xl shadow-2xl transition transform hover:scale-105 disabled:opacity-50 disabled:cursor-not-allowed disabled:transform-none border-2 border-green-400"
            >
              {loading ? '⏳ Proszę czekać...' : (isLogin ? '🚀 ZALOGUJ SIĘ' : '✨ ZAREJESTRUJ SIĘ')}
            </button>
          </form>

          <div className="mt-6 text-center">
            <div className="bg-gradient-to-r from-blue-50 to-purple-50 rounded-xl p-4 border-2 border-blue-200">
              <p className="text-sm text-gray-700 font-semibold">
                🎓 Gra edukacyjna o planowaniu finansowym i emerytalnym
              </p>
            </div>
          </div>
        </div>

        {/* Info - stopka */}
        <div className="text-center">
          <div className="bg-white bg-opacity-10 rounded-2xl px-6 py-3 border-2 border-white border-opacity-20 backdrop-blur-sm">
            <p className="text-white text-sm font-semibold">
              © 2025 ZUS - LifeOverflow
            </p>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Login;
