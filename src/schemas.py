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