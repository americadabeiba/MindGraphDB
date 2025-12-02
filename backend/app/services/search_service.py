from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from sqlalchemy.orm import Session
from app.models.article import Article

class SearchService:
    def __init__(self):
        self.vectorizer = TfidfVectorizer(
            max_features=1000,
            stop_words='english',
            ngram_range=(1, 2)
        )
        self.tfidf_matrix = None
        self.articles = []
        self.is_fitted = False  # ⬅️ NUEVO
    
    def fit(self, db: Session):
        """Train TF-IDF on all articles"""
        articles = db.query(Article).all()
        
        if not articles:
            print("⚠️ No articles found in database")
            return False
        
        self.articles = articles
        
        # Combine text fields
        corpus = []
        for article in articles:
            text = f"{article.title or ''} {article.abstract or ''} {article.introduction or ''}"
            corpus.append(text)
        
        if corpus:
            self.tfidf_matrix = self.vectorizer.fit_transform(corpus)
            self.is_fitted = True  # ⬅️ NUEVO
            print(f"✅ TF-IDF trained on {len(corpus)} articles")
            return True
        
        return False
    
    def search(self, query: str, limit: int, db: Session):
        """Search articles using TF-IDF similarity"""
        # ⬅️ NUEVO: Auto-fit si no está entrenado
        if not self.is_fitted or self.tfidf_matrix is None:
            print("🔄 Training TF-IDF vectorizer...")
            success = self.fit(db)
            if not success:
                return []
        
        # Transform query
        query_vec = self.vectorizer.transform([query])
        
        # Calculate similarity
        similarities = cosine_similarity(query_vec, self.tfidf_matrix).flatten()
        
        # Get top results
        top_indices = similarities.argsort()[-limit:][::-1]
        
        results = []
        for idx in top_indices:
            if similarities[idx] > 0:
                article = self.articles[idx]
                results.append({
                    "id": article.id,
                    "title": article.title,
                    "authors": article.authors,
                    "year": article.publication_year,
                    "score": float(similarities[idx]),
                    "abstract": article.abstract[:300] + "..." if article.abstract else None
                })
        
        return results