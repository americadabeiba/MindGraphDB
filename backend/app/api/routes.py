from fastapi import APIRouter
from app.api.endpoints import students, articles, graphs

router = APIRouter()

router.include_router(students.router, prefix="/students", tags=["Students"])
router.include_router(articles.router, prefix="/articles", tags=["Articles"])
router.include_router(graphs.router, prefix="/graphs", tags=["Graphs"])