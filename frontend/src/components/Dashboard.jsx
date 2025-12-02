import React, { useState, useEffect } from 'react';
import { BarChart, Bar, LineChart, Line, PieChart, Pie, Cell, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';
import { getStudentStats, getStatsByCity, getStatsByProfession } from '../services/api';

const COLORS = ['#9b87f5', '#d8b4fe', '#f0abfc', '#c4b5fd', '#7c5cdb'];

function Dashboard() {
  const [stats, setStats] = useState(null);
  const [cityData, setCityData] = useState([]);
  const [professionData, setProfessionData] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchData();
  }, []);

  const fetchData = async () => {
    try {
      const [statsRes, cityRes, professionRes] = await Promise.all([
        getStudentStats(),
        getStatsByCity(),
        getStatsByProfession()
      ]);

      setStats(statsRes.data);
      setCityData(cityRes.data.slice(0, 10)); // Top 10 cities
      setProfessionData(professionRes.data);
      setLoading(false);
    } catch (error) {
      console.error('Error fetching data:', error);
      setLoading(false);
    }
  };

  if (loading) {
    return (
      <div className="loading">
        <div className="spinner"></div>
      </div>
    );
  }

  return (
    <div className="dashboard">
      <div className="dashboard-header">
        <h1>Mental Health Analytics Dashboard</h1>
        <p>Comprehensive overview of student mental health data</p>
      </div>

      {/* Stats Cards */}
      <div className="stats-grid">
        <div className="stat-card">
          <div className="icon">👥</div>
          <h3>Total Students</h3>
          <div className="value">{stats?.total_students || 0}</div>
          <div className="trend">Complete dataset</div>
        </div>

        <div className="stat-card">
          <div className="icon">😔</div>
          <h3>Depression Cases</h3>
          <div className="value">{stats?.depressed_count || 0}</div>
          <div className="trend negative">{stats?.depression_rate || 0}% rate</div>
        </div>

        <div className="stat-card">
          <div className="icon">📊</div>
          <h3>Average CGPA</h3>
          <div className="value">{stats?.avg_cgpa || 0}</div>
          <div className="trend">Academic performance</div>
        </div>

        <div className="stat-card">
          <div className="icon">⚠️</div>
          <h3>Suicidal Thoughts</h3>
          <div className="value">{stats?.suicidal_thoughts_count || 0}</div>
          <div className="trend negative">{stats?.suicidal_rate || 0}% rate</div>
        </div>
      </div>

      {/* Charts */}
      <div className="charts-grid">
        {/* Depression by City */}
        <div className="chart-card">
          <h2>📍 Depression Rate by City (Top 10)</h2>
          <ResponsiveContainer width="100%" height={300}>
            <BarChart data={cityData}>
              <CartesianGrid strokeDasharray="3 3" stroke="rgba(155, 135, 245, 0.1)" />
              <XAxis dataKey="city" stroke="#8b7fa8" />
              <YAxis stroke="#8b7fa8" />
              <Tooltip 
                contentStyle={{ 
                  background: '#2a2235', 
                  border: '1px solid #9b87f5',
                  borderRadius: '8px'
                }}
              />
              <Legend />
              <Bar dataKey="rate" fill="#9b87f5" name="Depression Rate (%)" />
            </BarChart>
          </ResponsiveContainer>
        </div>

        {/* Depression by Profession */}
        <div className="chart-card">
          <h2>💼 Depression Rate by Profession</h2>
          <ResponsiveContainer width="100%" height={300}>
            <PieChart>
              <Pie
                data={professionData}
                dataKey="depressed"
                nameKey="profession"
                cx="50%"
                cy="50%"
                outerRadius={100}
                label={(entry) => `${entry.profession}: ${entry.rate}%`}
              >
                {professionData.map((entry, index) => (
                  <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
                ))}
              </Pie>
              <Tooltip 
                contentStyle={{ 
                  background: '#2a2235', 
                  border: '1px solid #9b87f5',
                  borderRadius: '8px'
                }}
              />
            </PieChart>
          </ResponsiveContainer>
        </div>
      </div>

      {/* City Table */}
      <div className="table-container">
        <div className="table-header">
          <h2>🌆 Detailed Statistics by City</h2>
        </div>
        <table>
          <thead>
            <tr>
              <th>City</th>
              <th>Total Students</th>
              <th>Depressed</th>
              <th>Rate</th>
              <th>Status</th>
            </tr>
          </thead>
          <tbody>
            {cityData.map((city, index) => (
              <tr key={index}>
                <td>{city.city}</td>
                <td>{city.total}</td>
                <td>{city.depressed}</td>
                <td>{city.rate}%</td>
                <td>
                  <span className={`badge ${city.rate > 50 ? 'badge-danger' : city.rate > 30 ? 'badge-warning' : 'badge-success'}`}>
                    {city.rate > 50 ? 'High Risk' : city.rate > 30 ? 'Moderate' : 'Low Risk'}
                  </span>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default Dashboard;