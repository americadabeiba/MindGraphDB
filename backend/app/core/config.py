from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    # Database
    DATABASE_URL: str = "postgresql://postgres:ramitas16@postgres:5432/mental_health_db"
    
    # Neo4j
    NEO4J_URI: str = "bolt://neo4j:7687"
    NEO4J_USER: str = "neo4j"
    NEO4J_PASSWORD: str = "password123"
    
    # API
    API_HOST: str = "0.0.0.0"
    API_PORT: int = 8000
    DEBUG: bool = True
    
    # ML
    MODEL_PATH: str = "./models/depression_model.pkl"
    
    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()