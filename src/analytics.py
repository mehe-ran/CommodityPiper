from sqlalchemy.orm import Session
from . import models


# calculate the price spread between two markets for a specific commodity
def calculate_market_spread(db: Session, commodity_id: int, location_a_id: int, location_b_id: int):
    # get latest usd prices for both locations
    price_a = db.query(models.DailyPrice).filter(
        models.DailyPrice.commodity_id == commodity_id,
        models.DailyPrice.location_id == location_a_id
    ).order_by(models.DailyPrice.date.desc()).first()

    price_b = db.query(models.DailyPrice).filter(
        models.DailyPrice.commodity_id == commodity_id,
        models.DailyPrice.location_id == location_b_id
    ).order_by(models.DailyPrice.date.desc()).first()

    if not price_a or not price_b:
        return {"error": "insufficient data to calculate spread"}

    spread_usd = abs(price_a.price_usd - price_b.price_usd)

    return {
        "commodity_id": commodity_id,
        "location_a_id": location_a_id,
        "location_b_id": location_b_id,
        "spread_usd": round(spread_usd, 2)
    }