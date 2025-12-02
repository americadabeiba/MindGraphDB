-- Create extensions
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Students table already created by SQLAlchemy, but we can add indexes
CREATE INDEX IF NOT EXISTS idx_students_depression ON students(depression);
CREATE INDEX IF NOT EXISTS idx_students_city ON students(city);
CREATE INDEX IF NOT EXISTS idx_students_profession ON students(profession);

-- Articles indexes
CREATE INDEX IF NOT EXISTS idx_articles_year ON articles(publication_year);
CREATE INDEX IF NOT EXISTS idx_articles_title ON articles USING gin(to_tsvector('english', title));