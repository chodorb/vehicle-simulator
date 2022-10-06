from sqlalchemy import Column,Integer,String
from app.db import Base

class Vehicle(Base):
    __tablename__ = 'vehicle'
    
    id=Column(Integer,primary_key=True)
    name=Column(String)
    description=Column(String)