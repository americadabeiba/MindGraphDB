import axios from 'axios';

const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000';

const api = axios.create({
  baseURL: `${API_URL}/api/v1`,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Students
export const getStudents = (params = {}) => 
  api.get('/students/', { params });

export const getStudent = (id) => 
  api.get(`/students/${id}`);

export const getStudentStats = () => 
  api.get('/students/stats/overview');

export const getStatsByCity = () => 
  api.get('/students/stats/by_city');

export const getStatsByProfession = () => 
  api.get('/students/stats/by_profession');

export const predictDepression = (data) => 
  api.post('/students/predict', data);

// Articles
export const getArticles = (params = {}) => 
  api.get('/articles/', { params });

export const searchArticles = (query, limit = 10) => 
  api.get('/articles/search', { params: { query, limit } });

export const getArticle = (id) => 
  api.get(`/articles/${id}`);

// Graphs
export const getStudentNetwork = (limit = 50) => 
  api.get('/graphs/students/network', { params: { limit } });

export const getCitiesDepression = () => 
  api.get('/graphs/cities/depression');

export default api;