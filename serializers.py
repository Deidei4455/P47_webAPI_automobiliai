from pydantic import BaseModel
import datetime


class CarsSchema(BaseModel):
    id: int
    make: str
    model: str
    color: str
    year: int
    price: float
    fuel_type: str
    date_created: datetime.datetime

    class Config:
        from_attributes = True
