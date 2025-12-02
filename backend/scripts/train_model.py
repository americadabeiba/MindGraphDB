import sys
sys.path.append('/app')

import pandas as pd
from app.services.ml_service import MLService
from app.core.database import SessionLocal
from app.models.student import Student

def main():
    print("🚀 Starting model training...")
    
    # Get data from database
    db = SessionLocal()
    students = db.query(Student).all()
    
    # Convert to DataFrame
    data = []
    for s in students:
        data.append({
            'gender': s.gender,
            'age': s.age,
            'academic_pressure': s.academic_pressure,
            'work_pressure': s.work_pressure,
            'cgpa': s.cgpa,
            'study_satisfaction': s.study_satisfaction,
            'job_satisfaction': s.job_satisfaction,
            'sleep_duration': s.sleep_duration,
            'dietary_habits': s.dietary_habits,
            'suicidal_thoughts': s.suicidal_thoughts,
            'work_study_hours': s.work_study_hours,
            'financial_stress': s.financial_stress,
            'family_history': s.family_history,
            'depression': s.depression
        })
    
    df = pd.DataFrame(data)
    print(f"📊 Training on {len(df)} students")
    
    # Train model
    ml_service = MLService()
    results = ml_service.train(df)
    
    print(f"\n✅ Model trained!")
    print(f"   Accuracy: {results['accuracy']:.2%}")
    print(f"   Train size: {results['train_size']}")
    print(f"   Test size: {results['test_size']}")
    
    # Save model
    ml_service.save_model('/app/models/depression_model.pkl')
    print(f"\n💾 Model saved to /app/models/depression_model.pkl")
    
    db.close()

if __name__ == "__main__":
    main()