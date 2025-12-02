import React, { useState, useEffect } from 'react';
import { getCitiesDepression } from '../services/api';

function GraphVisualization() {
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchData();
  }, []);

  const fetchData = async () => {
    try {
      const response = await getCitiesDepression();
      setData(response.data);
      setLoading(false);
    } catch (error) {
      console.error('Error:', error);
      setLoading(false);
    }
  };

  if (loading) {
    return <div className="loading"><div className="spinner"></div></div>;
  }

  return (
    <div>
      <div className="dashboard-header">
        <h1>🕸️ Network Graph Analysis</h1>
        <p>Depression patterns across student networks</p>
      </div>

      <div className="card">
        <div className="card-header">
          <h3 className="card-title">City Network - Depression Cases</h3>
        </div>
        <div style={{ padding: '2rem' }}>
          {data.map((item, index) => (
            <div key={index} style={{ 
              marginBottom: '1rem', 
              padding: '1rem',
              background: 'var(--bg-light)',
              borderRadius: '8px',
              display: 'flex',
              justifyContent: 'space-between',
              alignItems: 'center'
            }}>
              <span>{item.city}</span>
              <span className="badge badge-danger">{item.depressed_count} cases</span>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}

export default GraphVisualization;