import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from dotenv import load_dotenv

# load environment variables from .env file
load_dotenv()

# fetch database url or use default local postgres connection
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@localhost/commoditypiper")

# create the sqlalchemy engine for postgres
engine = create_engine(DATABASE_URL)

# create a configured session class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# base class for our database models
Base = declarative_base()

# dependency to yield a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()