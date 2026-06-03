from fastapi import FastAPI, Depends, HTTPException, status, BackgroundTasks
from sqlalchemy.orm import Session
from typing import List
from . import models, schemas, crud, extractor, analytics, auth
from .database import engine, get_db

# create database tables
models.Base.metadata.create_all(bind=engine)

# initialize the fastapi application
app = FastAPI(
    title="CommodityPiper API",
    description="Data pipeline for international commodity trading",
    version="1.1.0"
)

# dependency to check database for valid token
def get_current_client(api_key: str = Depends(auth.verify_api_key), db: Session = Depends(get_db)):
    token_record = crud.validate_token(db, api_key)
    if not token_record:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="invalid api key")
    return token_record

# root health check endpoint
@app.get("/")
def read_root():
    return {"status": "healthy", "pipeline": "commoditypiper active"}

# endpoint to generate a new api key for a client
@app.post("/auth/generate")
def generate_key(client_name: str, db: Session = Depends(get_db)):
    new_token = auth.generate_api_token()
    crud.create_api_token(db, client_name, new_token)
    return {"client": client_name, "api_key": new_token, "message": "store this securely"}

# public read endpoints
@app.get("/locations/", response_model=List[schemas.Location])
def read_locations(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_locations(db, skip=skip, limit=limit)

@app.get("/commodities/", response_model=List[schemas.Commodity])
def read_commodities(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_commodities(db, skip=skip, limit=limit)

@app.get("/prices/", response_model=List[schemas.DailyPrice])
def read_daily_prices(commodity_id: int = None, location_id: int = None, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_daily_prices(db, commodity_id=commodity_id, location_id=location_id, skip=skip, limit=limit)

@app.get("/analytics/spread")
def get_market_spread(commodity_id: int, location_a_id: int, location_b_id: int, db: Session = Depends(get_db)):
    return analytics.calculate_market_spread(db, commodity_id, location_a_id, location_b_id)

# secured write endpoints (require api key)
@app.post("/locations/", response_model=schemas.Location, dependencies=[Depends(get_current_client)])
def create_location(location: schemas.LocationCreate, db: Session = Depends(get_db)):
    return crud.create_location(db=db, location=location)

@app.post("/commodities/", response_model=schemas.Commodity, dependencies=[Depends(get_current_client)])
def create_commodity(commodity: schemas.CommodityCreate, db: Session = Depends(get_db)):
    return crud.create_commodity(db=db, commodity=commodity)

@app.post("/prices/", response_model=schemas.DailyPrice, dependencies=[Depends(get_current_client)])
def create_price_record(price: schemas.DailyPriceCreate, db: Session = Depends(get_db)):
    return crud.create_daily_price(db=db, price_schema=price)

@app.post("/extract/", dependencies=[Depends(get_current_client)])
def trigger_data_extraction(background_tasks: BackgroundTasks, db: Session = Depends(get_db)):
    # offload the heavy scraping task to the background
    background_tasks.add_task(extractor.fetch_and_store_daily_market_data, db)
    return {"status": "accepted", "message": "extraction pipeline triggered in background"}

@app.get("/analytics/moving-average")
def get_moving_average(commodity_id: int, location_id: int, days: int = 7, db: Session = Depends(get_db)):
    return analytics.calculate_moving_average(db, commodity_id, location_id, days)

@app.get("/analytics/volatility")
def get_market_volatility(commodity_id: int, location_id: int, days: int = 30, db: Session = Depends(get_db)):
    return analytics.calculate_volatility(db, commodity_id, location_id, days)