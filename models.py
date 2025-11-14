from sqlalchemy import Column, Integer, String, Float
from database import Base

class Bus(Base):
    __tablename__ = "buses"

    id = Column(Integer, primary_key=True, index=True)
    route = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)
