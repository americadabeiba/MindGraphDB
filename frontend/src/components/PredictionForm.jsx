import React, { useState } from 'react';
import { predictDepression } from '../services/api';

function PredictionForm() {
  const [formData, setFormData] = useState({
    gender: 'Male',
    age: 25,
    academic_pressure: 3,
    work_pressure: 2,
    cgpa: 7.5,
    study_satisfaction: 3,
    job_satisfaction: 3,
    sleep_duration: '7-8 hours',
    dietary_habits: 'Moderate',
    suicidal_thoughts: 'No',
    work_study_hours: 5,
    financial_stress: 2,
    family_history: 'No'
  });

  const [prediction, setPrediction] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    try {
      const response = await predictDepression(formData);
      setPrediction(response.data);
    } catch (error) {
      console.error('Error:', error);
      alert('Prediction failed. Make sure the model is trained.');
    }
    setLoading(false);
  };

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: isNaN(value) ? value : parseFloat(value)
    }));
  };

  return (
    <div className="prediction-form">
      <div className="dashboard-header">
        <h1>🔮 Depression Risk Prediction</h1>
        <p>ML-powered assessment using Naive Bayes classifier</p>
      </div>

      <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '2rem' }}>
        {/* Form */}
        <div className="card">
          <div className="card-header">
            <h3 className="card-title">Student Information</h3>
          </div>
          <form onSubmit={handleSubmit}>
            <div className="form-group">
              <label>Gender</label>
              <select name="gender" value={formData.gender} onChange={handleChange}>
                <option>Male</option>
                <option>Female</option>
              </select>
            </div>

            <div className="form-group">
              <label>Age</label>
              <input type="number" name="age" value={formData.age} onChange={handleChange} />
            </div>

            <div className="form-group">
              <label>Academic Pressure (1-5)</label>
              <input type="number" name="academic_pressure" min="0" max="5" step="0.1" value={formData.academic_pressure} onChange={handleChange} />
            </div>

            <div className="form-group">
              <label>Work Pressure (1-5)</label>
              <input type="number" name="work_pressure" min="0" max="5" step="0.1" value={formData.work_pressure} onChange={handleChange} />
            </div>

            <div className="form-group">
              <label>CGPA</label>
              <input type="number" name="cgpa" min="0" max="10" step="0.1" value={formData.cgpa} onChange={handleChange} />
            </div>

            <div className="form-group">
              <label>Study Satisfaction (1-5)</label>
              <input type="number" name="study_satisfaction" min="0" max="5" step="0.1" value={formData.study_satisfaction} onChange={handleChange} />
            </div>

            <div className="form-group">
              <label>Job Satisfaction (1-5)</label>
              <input type="number" name="job_satisfaction" min="0" max="5" step="0.1" value={formData.job_satisfaction} onChange={handleChange} />
            </div>

            <div className="form-group">
              <label>Sleep Duration</label>
              <select name="sleep_duration" value={formData.sleep_duration} onChange={handleChange}>
                <option>Less than 5 hours</option>
                <option>5-6 hours</option>
                <option>7-8 hours</option>
                <option>More than 8 hours</option>
              </select>
            </div>

            <div className="form-group">
              <label>Dietary Habits</label>
              <select name="dietary_habits" value={formData.dietary_habits} onChange={handleChange}>
                <option>Healthy</option>
                <option>Moderate</option>
                <option>Unhealthy</option>
              </select>
            </div>

            <div className="form-group">
              <label>Suicidal Thoughts</label>
              <select name="suicidal_thoughts" value={formData.suicidal_thoughts} onChange={handleChange}>
                <option>Yes</option>
                <option>No</option>
              </select>
            </div>

            <div className="form-group">
              <label>Work/Study Hours per Day</label>
              <input type="number" name="work_study_hours" min="0" max="24" step="0.5" value={formData.work_study_hours} onChange={handleChange} />
            </div>

            <div className="form-group">
              <label>Financial Stress (1-5)</label>
              <input type="number" name="financial_stress" min="0" max="5" step="0.1" value={formData.financial_stress} onChange={handleChange} />
            </div>

            <div className="form-group">
              <label>Family History of Mental Illness</label>
              <select name="family_history" value={formData.family_history} onChange={handleChange}>
                <option>Yes</option>
                <option>No</option>
              </select>
            </div>

            <button type="submit" className="btn btn-primary" disabled={loading} style={{ width: '100%' }}>
              {loading ? 'Analyzing...' : '🔮 Predict Depression Risk'}
            </button>
          </form>
        </div>

        {/* Results */}
        <div>
          {prediction ? (
            <div className="card">
              <div className="card-header">
                <h3 className="card-title">Prediction Results</h3>
              </div>
              <div style={{ textAlign: 'center', padding: '2rem' }}>
                <div style={{ 
                  fontSize: '5rem', 
                  marginBottom: '1rem'
                }}>
                  {prediction.prediction === 1 ? '😔' : '😊'}
                </div>
                <h2 style={{ 
                  fontSize: '2rem', 
                  marginBottom: '1rem',
                  color: prediction.prediction === 1 ? 'var(--danger)' : 'var(--success)'
                }}>
                  {prediction.prediction === 1 ? 'High Risk Detected' : 'Low Risk'}
                </h2>
                
                <div style={{ 
                  display: 'grid', 
                  gap: '1rem', 
                  marginTop: '2rem',
                  textAlign: 'left'
                }}>
                  <div style={{ 
                    padding: '1rem', 
                    background: 'var(--bg-light)', 
                    borderRadius: '12px'
                  }}>
                    <div style={{ color: 'var(--text-muted)', marginBottom: '0.5rem' }}>
                      Depression Probability
                    </div>
                    <div style={{ 
                      fontSize: '2rem', 
                      fontWeight: 'bold',
                      color: 'var(--danger)'
                    }}>
                      {(prediction.probability.depression * 100).toFixed(1)}%
                    </div>
                  </div>
                  
                  <div style={{ 
                    padding: '1rem', 
                    background: 'var(--bg-light)', 
                    borderRadius: '12px'
                  }}>
                    <div style={{ color: 'var(--text-muted)', marginBottom: '0.5rem' }}>
                      No Depression Probability
                    </div>
                    <div style={{ 
                      fontSize: '2rem', 
                      fontWeight: 'bold',
                      color: 'var(--success)'
                    }}>
                      {(prediction.probability.no_depression * 100).toFixed(1)}%
                    </div>
                  </div>
                </div>

                {prediction.prediction === 1 && (
                  <div style={{ 
                    marginTop: '2rem', 
                    padding: '1rem', 
                    background: 'rgba(248, 113, 113, 0.1)',
                    borderRadius: '12px',
                    borderLeft: '4px solid var(--danger)'
                  }}>
                    <p style={{ color: 'var(--danger)', fontWeight: 'bold' }}>
                      ⚠️ Recommendation
                    </p>
                    <p style={{ color: 'var(--text-secondary)', marginTop: '0.5rem' }}>
                      This student may benefit from professional mental health support. 
                      Consider reaching out to campus counseling services.
                    </p>
                  </div>
                )}
              </div>
            </div>
          ) : (
            <div className="card" style={{ textAlign: 'center', padding: '3rem' }}>
              <div style={{ fontSize: '3rem', marginBottom: '1rem' }}>🤖</div>
              <h3>Ready for Prediction</h3>
              <p style={{ color: 'var(--text-muted)' }}>
                Fill out the form and click predict to get an AI-powered assessment
              </p>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}

export default PredictionForm;