from pydantic import BaseModel
from datetime import date

# base schemas for location and commodity
class LocationBase(BaseModel):
    country: str
    currency: str

class CommodityBase(BaseModel):
    name: str
    category: str

# response schemas that include the database id
class Location(LocationBase):
    id: int
    class Config:
        from_attributes = True

class Commodity(CommodityBase):
    id: int
    class Config:
        from_attributes = True

# schema for incoming daily price payload
class DailyPriceCreate(BaseModel):
    date: date
    commodity_id: int
    location_id: int
    price_local: float
    exchange_rate_to_usd: float

# response schema for daily price records
class DailyPrice(DailyPriceCreate):
    id: int
    price_usd: float
    class Config:
        from_attributes = True

# creation schemas inheriting base attributes
class LocationCreate(LocationBase):
    pass

class CommodityCreate(CommodityBase):
    pass