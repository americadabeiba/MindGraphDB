import sys
sys.path.append('/app')

from app.core.database import SessionLocal, Base, engine
from app.utils.data_loader import (
    create_tables,
    load_students_to_postgres,
    load_students_to_neo4j,
    load_articles_to_postgres
)

def main():
    print("🚀 Starting data loading process...")
    
    # Create tables
    print("\n1️⃣ Creating database tables...")
    create_tables()
    
    # Get database session
    db = SessionLocal()
    
    try:
        # Load students to PostgreSQL
        print("\n2️⃣ Loading students to PostgreSQL...")
        load_students_to_postgres('/app/data/raw/Student Depression Dataset.csv', db)
        
        # Load students to Neo4j
        print("\n3️⃣ Loading students to Neo4j...")
        load_students_to_neo4j('/app/data/raw/Student Depression Dataset.csv')
        
        # Load articles
        print("\n4️⃣ Loading articles to PostgreSQL...")
        load_articles_to_postgres('/app/data/raw/articles.csv', db)
        
        print("\n✅ All data loaded successfully!")
        
    except Exception as e:
        print(f"\n❌ Error loading data: {e}")
        raise
    finally:
        db.close()

if __name__ == "__main__":
    main()