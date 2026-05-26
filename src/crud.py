from sqlalchemy.orm import Session
from . import models, schemas

# fetch all locations from the dimension table
def get_locations(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Location).offset(skip).limit(limit).all()

# fetch all commodities from the dimension table
def get_commodities(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Commodity).offset(skip).limit(limit).all()

# insert a new daily price entry into the fact table
def create_daily_price(db: Session, price_schema: schemas.DailyPriceCreate):
    db_price = models.DailyPrice(
        date=price_schema.date,
        commodity_id=price_schema.commodity_id,
        location_id=price_schema.location_id,
        price_local=price_schema.price_local,
        exchange_rate_to_usd=price_schema.exchange_rate_to_usd,
        price_usd=price_schema.price_local / price_schema.exchange_rate_to_usd
    )
    db.add(db_price)
    db.commit()
    db.refresh(db_price)
    return db_price