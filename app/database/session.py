from sqlalchemy.orm import sessionmaker, DeclarativeBase
from app.database.database import engine

class Base(DeclarativeBase):
    pass

Session = sessionmaker(engine,autoflush=False,autocommit=False)

def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()
        