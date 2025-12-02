// Create constraints
CREATE CONSTRAINT student_id IF NOT EXISTS FOR (s:Student) REQUIRE s.id IS UNIQUE;
CREATE CONSTRAINT city_name IF NOT EXISTS FOR (c:City) REQUIRE c.name IS UNIQUE;
CREATE CONSTRAINT profession_name IF NOT EXISTS FOR (p:Profession) REQUIRE p.name IS UNIQUE;

// Create indexes
CREATE INDEX student_depression IF NOT EXISTS FOR (s:Student) ON (s.depression);
CREATE INDEX student_age IF NOT EXISTS FOR (s:Student) ON (s.age);