/**
 * API Service - Komunikacja z backendem
 */
import axios from 'axios';

const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://lifeoverflow.packt.pl:5000/api';

// Konfiguracja axios
const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Interceptor - dodaj token do każdego zapytania
api.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('token');
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

// Interceptor - obsługa błędów
api.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      // Token wygasł lub nieprawidłowy
      localStorage.removeItem('token');
      window.location.href = '/login';
    }
    return Promise.reject(error);
  }
);

// Auth endpoints
export const authAPI = {
  register: (email, password) => 
    api.post('/auth/register', { email, password }),
  
  login: (email, password) => 
    api.post('/auth/login', { email, password }),
};

// Game endpoints
export const gameAPI = {
  createSession: (data) => 
    api.post('/game/session/new', data),
  
  getSession: (sessionId) => 
    api.get(`/game/session/${sessionId}`),
  
  advanceTime: (sessionId) => 
    api.post(`/game/session/${sessionId}/advance`),
  
  getEvent: (sessionId) => 
    api.get(`/game/session/${sessionId}/event`),
  
  makeChoice: (eventId, choiceIndex) => 
    api.post(`/game/event/${eventId}/choose`, { choice_index: choiceIndex }),

  performAction: (sessionId, actionType) =>
    api.post(`/game/session/${sessionId}/action`, { action_type: actionType }),
};

// Advisor endpoints
export const advisorAPI = {
  getAdvice: (sessionId, recentDecision = null) => {
    const params = recentDecision ? { recent_decision: recentDecision } : {};
    return api.get(`/advisor/advice/${sessionId}`, { params });
  },
};

export default api;
