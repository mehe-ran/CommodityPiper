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

# fetch daily prices with optional commodity or location filtering
def get_daily_prices(db: Session, commodity_id: int = None, location_id: int = None, skip: int = 0, limit: int = 100):
    query = db.query(models.DailyPrice)
    if commodity_id:
        query = query.filter(models.DailyPrice.commodity_id == commodity_id)
    if location_id:
        query = query.filter(models.DailyPrice.location_id == location_id)
    return query.offset(skip).limit(limit).all()

# insert a new location into the dimension table
def create_location(db: Session, location: schemas.LocationCreate):
    db_location = models.Location(country=location.country, currency=location.currency)
    db.add(db_location)
    db.commit()
    db.refresh(db_location)
    return db_location

# insert a new commodity into the dimension table
def create_commodity(db: Session, commodity: schemas.CommodityCreate):
    db_commodity = models.Commodity(name=commodity.name, category=commodity.category)
    db.add(db_commodity)
    db.commit()
    db.refresh(db_commodity)
    return db_commodity