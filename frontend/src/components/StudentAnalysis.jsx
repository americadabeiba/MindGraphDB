import React, { useState, useEffect } from 'react';
import { getStudents } from '../services/api';

function StudentAnalysis() {
  const [students, setStudents] = useState([]);
  const [loading, setLoading] = useState(true);
  const [filters, setFilters] = useState({
    depression: '',
    city: ''
  });

  useEffect(() => {
    fetchStudents();
  }, [filters]);

  const fetchStudents = async () => {
    try {
      setLoading(true);
      const params = {};
      if (filters.depression !== '') params.depression = filters.depression;
      if (filters.city) params.city = filters.city;
      
      const response = await getStudents(params);
      setStudents(response.data);
      setLoading(false);
    } catch (error) {
      console.error('Error:', error);
      setLoading(false);
    }
  };

  return (
    <div className="student-analysis">
      <div className="dashboard-header">
        <h1>👥 Student Analysis</h1>
        <p>Detailed view of individual student records</p>
      </div>

      {/* Filters */}
      <div className="card" style={{ marginBottom: '2rem' }}>
        <div className="card-header">
          <h3 className="card-title">🔍 Filters</h3>
        </div>
        <div style={{ display: 'flex', gap: '1rem', flexWrap: 'wrap' }}>
          <div className="form-group" style={{ flex: '1', minWidth: '200px' }}>
            <label>Depression Status</label>
            <select 
              value={filters.depression}
              onChange={(e) => setFilters({...filters, depression: e.target.value})}
            >
              <option value="">All</option>
              <option value="1">Depressed</option>
              <option value="0">Not Depressed</option>
            </select>
          </div>
          <div className="form-group" style={{ flex: '1', minWidth: '200px' }}>
            <label>City</label>
            <input 
              type="text"
              placeholder="Enter city name..."
              value={filters.city}
              onChange={(e) => setFilters({...filters, city: e.target.value})}
            />
          </div>
        </div>
      </div>

      {/* Students Table */}
      {loading ? (
        <div className="loading"><div className="spinner"></div></div>
      ) : (
        <div className="table-container">
          <div className="table-header">
            <h2>📋 Student Records ({students.length})</h2>
          </div>
          <table>
            <thead>
              <tr>
                <th>ID</th>
                <th>Gender</th>
                <th>Age</th>
                <th>City</th>
                <th>CGPA</th>
                <th>Academic Pressure</th>
                <th>Sleep</th>
                <th>Depression</th>
                <th>Suicidal Thoughts</th>
              </tr>
            </thead>
            <tbody>
              {students.map((student) => (
                <tr key={student.id}>
                  <td>{student.id}</td>
                  <td>{student.gender}</td>
                  <td>{student.age}</td>
                  <td>{student.city}</td>
                  <td>{student.cgpa}</td>
                  <td>
                    <span className={`badge ${student.academic_pressure > 3 ? 'badge-danger' : 'badge-success'}`}>
                      {student.academic_pressure}/5
                    </span>
                  </td>
                  <td>{student.sleep_duration}</td>
                  <td>
                    <span className={`badge ${student.depression === 1 ? 'badge-danger' : 'badge-success'}`}>
                      {student.depression === 1 ? 'Yes' : 'No'}
                    </span>
                  </td>
                  <td>
                    <span className={`badge ${student.suicidal_thoughts === 'Yes' ? 'badge-danger' : 'badge-success'}`}>
                      {student.suicidal_thoughts}
                    </span>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
}

export default StudentAnalysis;