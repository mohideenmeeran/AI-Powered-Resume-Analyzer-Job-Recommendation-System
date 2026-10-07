CREATE_ANALYSES_TABLE = """
CREATE TABLE IF NOT EXISTS analyses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    file_name TEXT NOT NULL,
    candidate_name TEXT,
    resume_score REAL,
    skills TEXT,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP
);
"""