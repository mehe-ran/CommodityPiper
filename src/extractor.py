import random
from datetime import date
from sqlalchemy.orm import Session
from . import models, crud, schemas


# simulate fetching live spot prices from external market apis
def fetch_and_store_daily_market_data(db: Session):
    # get all tracked locations and commodities
    locations = crud.get_locations(db)
    commodities = crud.get_commodities(db)

    if not locations or not commodities:
        return {"error": "dimension tables must be populated first"}

    records_added = 0
    today = date.today()

    for loc in locations:
        for comm in commodities:
            # simulate a local price and exchange rate volatility
            base_price = random.uniform(200.0, 500.0)
            exchange_rate = random.uniform(0.8, 20.0)

            price_data = schemas.DailyPriceCreate(
                date=today,
                commodity_id=comm.id,
                location_id=loc.id,
                price_local=base_price * exchange_rate,
                exchange_rate_to_usd=exchange_rate
            )
            crud.create_daily_price(db, price_data)
            records_added += 1

    return {"message": f"successfully extracted and stored {records_added} market records"}