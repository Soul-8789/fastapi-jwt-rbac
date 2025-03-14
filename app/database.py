from sqlmodel import SQLModel, create_engine
# from app.config import DATABASE_URL
from app.security.config import DATABASE_URL
engine = create_engine(DATABASE_URL, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
