from sqlalchemy.orm import Session
from . import models, schemas

# fetch all locations from the dimension table
def get_locations(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Location).offset(skip).limit(limit).all()

# fetch all commodities from the dimension table
def get_commodities(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Commodity).offset(skip).limit(limit).all()