from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

engine = create_engine(os.getenv("DATABASE_URL"))
SessionLocal = sessionmaker(bind=engine)
