from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.article import Article
from app.services.search_service import SearchService

router = APIRouter()
search_service = SearchService()

@router.get("/")
async def get_articles(
    skip: int = 0,
    limit: int = 20,
    db: Session = Depends(get_db)
):
    """Get all articles with pagination"""
    articles = db.query(Article).offset(skip).limit(limit).all()
    return articles

@router.get("/search")
async def search_articles(
    query: str = Query(..., min_length=2),
    limit: int = 10,
    db: Session = Depends(get_db)
):
    """Search articles using TF-IDF"""
    results = search_service.search(query, limit, db)
    return results

@router.get("/{article_id}")
async def get_article(article_id: int, db: Session = Depends(get_db)):
    """Get specific article"""
    article = db.query(Article).filter(Article.id == article_id).first()
    if not article:
        raise HTTPException(status_code=404, detail="Article not found")
    return article