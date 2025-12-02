from app.core.database import Neo4jConnection

class GraphService:
    def __init__(self):
        self.neo4j = Neo4jConnection()
    
    def create_student_node(self, student_data: dict):
        """Create a student node in Neo4j"""
        query = """
        CREATE (s:Student {
            id: $id,
            gender: $gender,
            age: $age,
            cgpa: $cgpa,
            depression: $depression,
            suicidal_thoughts: $suicidal_thoughts
        })
        RETURN s
        """
        return self.neo4j.query(query, student_data)
    
    def create_city_relationship(self, student_id: int, city: str):
        """Create student-city relationship"""
        query = """
        MATCH (s:Student {id: $student_id})
        MERGE (c:City {name: $city})
        MERGE (s)-[:LIVES_IN]->(c)
        """
        self.neo4j.query(query, {"student_id": student_id, "city": city})
    
    def create_profession_relationship(self, student_id: int, profession: str):
        """Create student-profession relationship"""
        query = """
        MATCH (s:Student {id: $student_id})
        MERGE (p:Profession {name: $profession})
        MERGE (s)-[:HAS_PROFESSION]->(p)
        """
        self.neo4j.query(query, {"student_id": student_id, "profession": profession})
    
    def create_mental_condition_relationship(self, student_id: int):
        """Create relationship to mental condition"""
        query = """
        MATCH (s:Student {id: $student_id})
        WHERE s.depression = 1
        MERGE (m:MentalCondition {type: 'Depression'})
        MERGE (s)-[:SUFFERS_FROM]->(m)
        """
        self.neo4j.query(query, {"student_id": student_id})
    
    def get_student_network(self, student_id: int):
        """Get network around a student"""
        query = """
        MATCH (s:Student {id: $student_id})-[r]-(n)
        RETURN s, type(r) as relationship, n
        """
        return self.neo4j.query(query, {"student_id": student_id})
    
    def get_depression_by_city(self):
        """Get depression statistics by city"""
        query = """
        MATCH (s:Student)-[:LIVES_IN]->(c:City)
        WITH c.name as city, 
             count(s) as total,
             sum(CASE WHEN s.depression = 1 THEN 1 ELSE 0 END) as depressed
        RETURN city, total, depressed,
               round(toFloat(depressed) / total * 100, 2) as depression_rate
        ORDER BY depression_rate DESC
        """
        return self.neo4j.query(query)
    
    def get_depression_by_profession(self):
        """Get depression statistics by profession"""
        query = """
        MATCH (s:Student)-[:HAS_PROFESSION]->(p:Profession)
        WITH p.name as profession, 
             count(s) as total,
             sum(CASE WHEN s.depression = 1 THEN 1 ELSE 0 END) as depressed
        RETURN profession, total, depressed,
               round(toFloat(depressed) / total * 100, 2) as depression_rate
        ORDER BY depression_rate DESC
        """
        return self.neo4j.query(query)
    
    def run_pagerank(self):
        """Run PageRank algorithm on the graph"""
        query = """
        CALL gds.pageRank.stream('student-graph')
        YIELD nodeId, score
        RETURN gds.util.asNode(nodeId).id AS student_id, score
        ORDER BY score DESC
        LIMIT 20
        """
        return self.neo4j.query(query)
    
    def get_communities(self):
        """Detect communities in the graph"""
        query = """
        CALL gds.louvain.stream('student-graph')
        YIELD nodeId, communityId
        RETURN communityId, collect(gds.util.asNode(nodeId).id) as members
        ORDER BY size(members) DESC
        """
        return self.neo4j.query(query)