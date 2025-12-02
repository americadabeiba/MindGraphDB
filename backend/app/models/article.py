from sqlalchemy import Column, Integer, String, Text
from app.core.database import Base

class Article(Base):
    __tablename__ = "articles"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(Text)
    publication_title = Column(Text)
    doi = Column(String)
    authors = Column(Text)
    publication_year = Column(Integer)
    url = Column(Text)
    content_type = Column(String)
    abstract = Column(Text)
    introduction = Column(Text)
    conclusion = Column(Text)
    number = Column(Integer)