from fastapi import APIRouter, Depends
from app.core.database import get_neo4j

router = APIRouter()

@router.get("/students/network")
async def get_student_network(limit: int = 50):
    """Get student network from Neo4j"""
    neo4j = get_neo4j()
    
    query = f"""
    MATCH (s:Student)-[r]->(n)
    RETURN s, r, n
    LIMIT {limit}
    """
    
    results = neo4j.query(query)
    return {"nodes": len(results), "data": results}

@router.get("/cities/depression")
async def get_cities_depression():
    """Get depression rate by city"""
    neo4j = get_neo4j()
    
    query = """
    MATCH (s:Student)-[:LIVES_IN]->(c:City)
    WHERE s.depression = 1
    RETURN c.name as city, count(s) as depressed_count
    ORDER BY depressed_count DESC
    """
    
    results = neo4j.query(query)
    return results