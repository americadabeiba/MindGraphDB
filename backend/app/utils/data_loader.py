import pandas as pd
from sqlalchemy.orm import Session
from app.models.student import Student
from app.models.article import Article
from app.core.database import Base, engine
from app.services.graph_service import GraphService

def load_students_to_postgres(csv_path: str, db: Session):
    """Load students CSV to PostgreSQL"""
    df = pd.read_csv(csv_path)
    
    # Clean column names
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('/', '_')
    
    # Rename problematic columns
    column_mapping = {
        'have_you_ever_had_suicidal_thoughts_?': 'suicidal_thoughts',
        'work_study_hours': 'work_study_hours',
        'family_history_of_mental_illness': 'family_history'
    }
    df.rename(columns=column_mapping, inplace=True)
    
    # Insert to database
    for _, row in df.iterrows():
        student = Student(
            id=int(row['id']),
            gender=row.get('gender'),
            age=float(row['age']) if pd.notna(row.get('age')) else None,
            city=row.get('city'),
            profession=row.get('profession'),
            academic_pressure=float(row['academic_pressure']) if pd.notna(row.get('academic_pressure')) else None,
            work_pressure=float(row['work_pressure']) if pd.notna(row.get('work_pressure')) else None,
            cgpa=float(row['cgpa']) if pd.notna(row.get('cgpa')) else None,
            study_satisfaction=float(row['study_satisfaction']) if pd.notna(row.get('study_satisfaction')) else None,
            job_satisfaction=float(row['job_satisfaction']) if pd.notna(row.get('job_satisfaction')) else None,
            sleep_duration=row.get('sleep_duration'),
            dietary_habits=row.get('dietary_habits'),
            degree=row.get('degree'),
            suicidal_thoughts=row.get('suicidal_thoughts'),
            work_study_hours=float(row['work_study_hours']) if pd.notna(row.get('work_study_hours')) else None,
            financial_stress=float(row['financial_stress']) if pd.notna(row.get('financial_stress')) else None,
            family_history=row.get('family_history'),
            depression=int(row['depression']) if pd.notna(row.get('depression')) else 0
        )
        db.merge(student)
    
    db.commit()
    print(f"✅ Loaded {len(df)} students to PostgreSQL")

def load_students_to_neo4j(csv_path: str):
    """Load students CSV to Neo4j"""
    df = pd.read_csv(csv_path)
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('/', '_')
    
    column_mapping = {
        'have_you_ever_had_suicidal_thoughts_?': 'suicidal_thoughts',
        'family_history_of_mental_illness': 'family_history'
    }
    df.rename(columns=column_mapping, inplace=True)
    
    graph_service = GraphService()
    
    for _, row in df.iterrows():
        # Create student node
        student_data = {
            "id": int(row['id']),
            "gender": row.get('gender', 'Unknown'),
            "age": float(row['age']) if pd.notna(row.get('age')) else 0,
            "cgpa": float(row['cgpa']) if pd.notna(row.get('cgpa')) else 0,
            "depression": int(row['depression']) if pd.notna(row.get('depression')) else 0,
            "suicidal_thoughts": row.get('suicidal_thoughts', 'Unknown')
        }
        graph_service.create_student_node(student_data)
        
        # Create relationships
        if pd.notna(row.get('city')):
            graph_service.create_city_relationship(int(row['id']), row['city'])
        
        if pd.notna(row.get('profession')):
            graph_service.create_profession_relationship(int(row['id']), row['profession'])
        
        if row.get('depression') == 1:
            graph_service.create_mental_condition_relationship(int(row['id']))
    
    print(f"✅ Loaded {len(df)} students to Neo4j")

def load_articles_to_postgres(csv_path: str, db: Session):
    """Load articles CSV to PostgreSQL"""
    df = pd.read_csv(csv_path, sep=';', encoding='utf-8')
    
    # Clean column names
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
    
    for _, row in df.iterrows():
        article = Article(
            title=row.get('item_title'),
            publication_title=row.get('publication_title'),
            doi=row.get('item_doi'),
            authors=row.get('authors'),
            publication_year=int(row['publication_year']) if pd.notna(row.get('publication_year')) else None,
            url=row.get('url'),
            content_type=row.get('content_type'),
            abstract=row.get('abstract'),
            introduction=row.get('introduction'),
            conclusion=row.get('conclusion'),
            number=int(row['number']) if pd.notna(row.get('number')) else None
        )
        db.add(article)
    
    db.commit()
    print(f"✅ Loaded {len(df)} articles to PostgreSQL")

def create_tables():
    """Create all database tables"""
    Base.metadata.create_all(bind=engine)
    print("✅ Database tables created")