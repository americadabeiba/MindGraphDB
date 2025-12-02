from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import router
from app.core.config import settings
from app.services.ml_service import MLService

app = FastAPI(
    title="MindGraphDB API",
    description="API for Mental Health Analysis with Graphs and ML",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://frontend:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(router, prefix="/api/v1")

@app.on_event("startup")
async def startup_event():
    """Initialize services on startup"""
    print("🚀 Starting MindGraphDB API...")
    print(f"📚 Docs available at: http://localhost:8000/docs")

@app.get("/")
async def root():
    return {
        "message": "MindGraphDB API",
        "version": "1.0.0",
        "docs": "/docs",
        "endpoints": {
            "students": "/api/v1/students",
            "articles": "/api/v1/articles",
            "graphs": "/api/v1/graphs"
        }
    }

@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "database": "connected",
        "neo4j": "connected"
    }