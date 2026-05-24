from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base


# location dimension table for tracking different markets
class Location(Base):
    __tablename__ = "locations"

    id = Column(Integer, primary_key=True, index=True)
    country = Column(String, index=True)
    currency = Column(String)


# commodity dimension table for different metals
class Commodity(Base):
    __tablename__ = "commodities"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    category = Column(String)


# central fact table for daily pricing and forex rates
class DailyPrice(Base):
    __tablename__ = "daily_prices"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date, index=True)
    commodity_id = Column(Integer, ForeignKey("commodities.id"))
    location_id = Column(Integer, ForeignKey("locations.id"))

    # pricing details
    price_local = Column(Float)
    exchange_rate_to_usd = Column(Float)
    price_usd = Column(Float)

    # relationships for easy querying later
    commodity = relationship("Commodity")
    location = relationship("Location")