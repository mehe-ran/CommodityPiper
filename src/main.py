from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from typing import List
from . import models, schemas, crud
from .database import engine, get_db

# create database tables
models.Base.metadata.create_all(bind=engine)

# initialize the fastapi application
app = FastAPI(
    title="CommodityPiper API",
    description="Data pipeline for international commodity trading",
    version="1.0.0"
)

# root health check endpoint
@app.get("/")
def read_root():
    return {"status": "healthy", "pipeline": "commoditypiper active"}

# endpoint to fetch locations
@app.get("/locations/", response_model=List[schemas.Location])
def read_locations(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_locations(db, skip=skip, limit=limit)

# endpoint to fetch commodities
@app.get("/commodities/", response_model=List[schemas.Commodity])
def read_commodities(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_commodities(db, skip=skip, limit=limit)

# endpoint to ingest daily market price data
@app.post("/prices/", response_model=schemas.DailyPrice)
def create_price_record(price: schemas.DailyPriceCreate, db: Session = Depends(get_db)):
    return crud.create_daily_price(db=db, price_schema=price)

# endpoint to query historical daily price records
@app.get("/prices/", response_model=List[schemas.DailyPrice])
def read_daily_prices(
    commodity_id: int = None,
    location_id: int = None,
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    return crud.get_daily_prices(db, commodity_id=commodity_id, location_id=location_id, skip=skip, limit=limit)