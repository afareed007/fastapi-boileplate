from sqlalchemy.orm import Session
from app.models import SessionLocal

# Dependency for database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
