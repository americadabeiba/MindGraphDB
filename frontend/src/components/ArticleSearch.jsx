import React, { useState } from 'react';
import { searchArticles } from '../services/api';

function ArticleSearch() {
  const [query, setQuery] = useState('');
  const [results, setResults] = useState([]);
  const [loading, setLoading] = useState(false);
  const [searched, setSearched] = useState(false);

  const handleSearch = async (e) => {
    e.preventDefault();
    if (!query.trim()) return;

    setLoading(true);
    try {
      const response = await searchArticles(query);
      setResults(response.data);
      setSearched(true);
    } catch (error) {
      console.error('Error:', error);
    }
    setLoading(false);
  };

  return (
    <div className="article-search">
      <div className="dashboard-header">
        <h1>📚 Research Articles</h1>
        <p>Search scientific literature using TF-IDF ranking</p>
      </div>

      {/* Search Bar */}
      <form onSubmit={handleSearch} className="search-bar">
        <input
          type="text"
          placeholder="Search for articles (e.g., 'depression treatment', 'student mental health')..."
          value={query}
          onChange={(e) => setQuery(e.target.value)}
        />
        <button type="submit" className="btn btn-primary">
          🔍 Search
        </button>
      </form>

      {/* Results */}
      {loading ? (
        <div className="loading"><div className="spinner"></div></div>
      ) : searched ? (
        <div>
          <div style={{ marginBottom: '1rem', color: 'var(--text-muted)' }}>
            Found {results.length} articles
          </div>
          <div style={{ display: 'grid', gap: '1rem' }}>
            {results.map((article) => (
              <div key={article.id} className="card">
                <div className="card-header">
                  <h3 className="card-title">{article.title}</h3>
                  <span className="badge badge-primary">
                    Score: {(article.score * 100).toFixed(1)}%
                  </span>
                </div>
                <div className="card-content">
                  <p style={{ marginBottom: '0.75rem' }}>
                    <strong>Authors:</strong> {article.authors || 'N/A'}
                  </p>
                  <p style={{ marginBottom: '0.75rem' }}>
                    <strong>Year:</strong> {article.year || 'N/A'}
                  </p>
                  {article.abstract && (
                    <p style={{ 
                      color: 'var(--text-secondary)', 
                      lineHeight: '1.6',
                      marginTop: '1rem',
                      padding: '1rem',
                      background: 'var(--bg-light)',
                      borderRadius: '8px'
                    }}>
                      {article.abstract}
                    </p>
                  )}
                </div>
              </div>
            ))}
          </div>
        </div>
      ) : (
        <div className="card" style={{ textAlign: 'center', padding: '3rem' }}>
          <div style={{ fontSize: '3rem', marginBottom: '1rem' }}>🔍</div>
          <h3>Start Your Search</h3>
          <p style={{ color: 'var(--text-muted)' }}>
            Enter keywords to find relevant research articles
          </p>
        </div>
      )}
    </div>
  );
}

export default ArticleSearch;