from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent

DATA_DIR = BASE_DIR / "data"
UPLOAD_DIR = BASE_DIR / "uploads"
MODEL_DIR = BASE_DIR / "models_cache"

DB_PATH = BASE_DIR / "resume_analyzer.db"

SKILLS_FILE = DATA_DIR / "skills.json"
JOBS_FILE = DATA_DIR / "jobs.csv"
LEARNING_FILE = DATA_DIR / "learning_resources.json"

EMBEDDING_MODEL = "all-MiniLM-L6-v2"

DATA_DIR.mkdir(exist_ok=True)
UPLOAD_DIR.mkdir(exist_ok=True)
MODEL_DIR.mkdir(exist_ok=True)