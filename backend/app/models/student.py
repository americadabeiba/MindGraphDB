from sqlalchemy import Column, Integer, String, Float
from app.core.database import Base

class Student(Base):
    __tablename__ = "students"
    
    id = Column(Integer, primary_key=True, index=True)
    gender = Column(String)
    age = Column(Float)
    city = Column(String)
    profession = Column(String)
    academic_pressure = Column(Float)
    work_pressure = Column(Float)
    cgpa = Column(Float)
    study_satisfaction = Column(Float)
    job_satisfaction = Column(Float)
    sleep_duration = Column(String)
    dietary_habits = Column(String)
    degree = Column(String)
    suicidal_thoughts = Column(String)
    work_study_hours = Column(Float)
    financial_stress = Column(Float)
    family_history = Column(String)
    depression = Column(Integer)