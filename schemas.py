from pydantic import BaseModel

class BusBase(BaseModel):
    route : str
    latitude : float
    longitude : float

class BusCreate(BusBase):
    pass

class Bus(BusBase):
    id : int

    class Config:
        from_attributes = True

class BusLocationUpdate(BaseModel):
    latitude : float
    longitude : float