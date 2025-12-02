from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import List, Optional
from pydantic import BaseModel
from app.core.database import get_db
from app.models.student import Student
from app.services.ml_service import MLService

router = APIRouter()
ml_service = MLService()

# Load model at startup
try:
    ml_service.load_model('/app/models/depression_model.pkl')
except:
    print("⚠️ Model not found. Train it first with: python scripts/train_model.py")

class StudentCreate(BaseModel):
    gender: str
    age: float
    academic_pressure: float
    work_pressure: float
    cgpa: float
    study_satisfaction: float
    job_satisfaction: float
    sleep_duration: str
    dietary_habits: str
    suicidal_thoughts: str
    work_study_hours: float
    financial_stress: float
    family_history: str

@router.get("/")
async def get_all_students(
    skip: int = 0,
    limit: int = 100,
    depression: Optional[int] = None,
    city: Optional[str] = None,
    db: Session = Depends(get_db)
):
    """Get all students with filters"""
    query = db.query(Student)
    
    if depression is not None:
        query = query.filter(Student.depression == depression)
    
    if city:
        query = query.filter(Student.city == city)
    
    students = query.offset(skip).limit(limit).all()
    return students

@router.get("/stats/overview")
async def get_statistics(db: Session = Depends(get_db)):
    """Get general statistics"""
    total = db.query(Student).count()
    depressed = db.query(Student).filter(Student.depression == 1).count()
    
    avg_cgpa = db.query(func.avg(Student.cgpa)).scalar()
    avg_age = db.query(func.avg(Student.age)).scalar()
    
    suicidal = db.query(Student).filter(Student.suicidal_thoughts == 'Yes').count()
    
    return {
        "total_students": total,
        "depressed_count": depressed,
        "depression_rate": round(depressed / total * 100, 2) if total > 0 else 0,
        "avg_cgpa": round(avg_cgpa, 2) if avg_cgpa else 0,
        "avg_age": round(avg_age, 2) if avg_age else 0,
        "suicidal_thoughts_count": suicidal,
        "suicidal_rate": round(suicidal / total * 100, 2) if total > 0 else 0
    }

@router.get("/stats/by_city")
async def get_stats_by_city(db: Session = Depends(get_db)):
    """Get depression statistics by city"""
    results = db.query(
        Student.city,
        func.count(Student.id).label('total'),
        func.sum(Student.depression).label('depressed')
    ).group_by(Student.city).all()
    
    stats = []
    for city, total, depressed in results:
        if city:
            stats.append({
                "city": city,
                "total": total,
                "depressed": depressed or 0,
                "rate": round((depressed or 0) / total * 100, 2)
            })
    
    return sorted(stats, key=lambda x: x['rate'], reverse=True)

@router.get("/stats/by_profession")
async def get_stats_by_profession(db: Session = Depends(get_db)):
    """Get depression statistics by profession"""
    results = db.query(
        Student.profession,
        func.count(Student.id).label('total'),
        func.sum(Student.depression).label('depressed')
    ).group_by(Student.profession).all()
    
    stats = []
    for profession, total, depressed in results:
        if profession:
            stats.append({
                "profession": profession,
                "total": total,
                "depressed": depressed or 0,
                "rate": round((depressed or 0) / total * 100, 2)
            })
    
    return sorted(stats, key=lambda x: x['rate'], reverse=True)

@router.post("/predict")
async def predict_depression(student: StudentCreate):
    """Predict depression for a new student"""
    try:
        prediction = ml_service.predict(student.dict())
        return prediction
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction error: {str(e)}")

@router.get("/{student_id}")
async def get_student(student_id: int, db: Session = Depends(get_db)):
    """Get specific student by ID"""
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student