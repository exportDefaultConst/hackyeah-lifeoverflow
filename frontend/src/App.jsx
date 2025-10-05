/**
 * Główny komponent aplikacji - routing i zarządzanie stanem
 */
import React, { useState, useEffect } from 'react';
import { Routes, Route, Navigate } from 'react-router-dom';
import Login from './pages/Login';
import GameScreen from './pages/GameScreen';
import Results from './pages/Results';

function App() {
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const [loading, setLoading] = useState(true);

  // Sprawdź czy użytkownik jest zalogowany
  useEffect(() => {
    const token = localStorage.getItem('token');
    setIsAuthenticated(!!token);
    setLoading(false);
  }, []);

  if (loading) {
    return (
      <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-zus-blue to-zus-dark-blue">
        <div className="text-white text-2xl">Ładowanie...</div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gray-50">
      <Routes>
        <Route 
          path="/login" 
          element={
            isAuthenticated ? 
            <Navigate to="/game" replace /> : 
            <Login setIsAuthenticated={setIsAuthenticated} />
          } 
        />
        <Route 
          path="/game" 
          element={
            isAuthenticated ? 
            <GameScreen /> : 
            <Navigate to="/login" replace />
          } 
        />
        <Route 
          path="/results/:sessionId" 
          element={
            isAuthenticated ? 
            <Results /> : 
            <Navigate to="/login" replace />
          } 
        />
        <Route 
          path="/" 
          element={<Navigate to={isAuthenticated ? "/game" : "/login"} replace />} 
        />
      </Routes>
    </div>
  );
}

export default App;
