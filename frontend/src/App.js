import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import Dashboard from './components/Dashboard';
import GraphVisualization from './components/GraphVisualization';
import ArticleSearch from './components/ArticleSearch';
import StudentAnalysis from './components/StudentAnalysis';
import PredictionForm from './components/PredictionForm';
import './styles/App.css';

function App() {
  return (
    <Router>
      <div className="app">
        {/* Sidebar Navigation */}
        <nav className="sidebar">
          <div className="logo">
            <h1>🧠 MindGraphDB</h1>
            <p>Mental Health Analytics</p>
          </div>
          
          <ul className="nav-links">
            <li>
              <Link to="/">
                <span className="icon">📊</span>
                Dashboard
              </Link>
            </li>
            <li>
              <Link to="/students">
                <span className="icon">👥</span>
                Student Analysis
              </Link>
            </li>
            <li>
              <Link to="/graph">
                <span className="icon">🕸️</span>
                Network Graph
              </Link>
            </li>
            <li>
              <Link to="/articles">
                <span className="icon">📚</span>
                Research Articles
              </Link>
            </li>
            <li>
              <Link to="/predict">
                <span className="icon">🔮</span>
                Prediction Tool
              </Link>
            </li>
          </ul>
          
          <div className="sidebar-footer">
            <p>v1.0.0</p>
            <p>© 2025 MindGraphDB</p>
          </div>
        </nav>

        {/* Main Content */}
        <main className="main-content">
          <Routes>
            <Route path="/" element={<Dashboard />} />
            <Route path="/students" element={<StudentAnalysis />} />
            <Route path="/graph" element={<GraphVisualization />} />
            <Route path="/articles" element={<ArticleSearch />} />
            <Route path="/predict" element={<PredictionForm />} />
          </Routes>
        </main>
      </div>
    </Router>
  );
}

export default App;