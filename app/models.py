from sqlalchemy import Column, ForeignKey,Integer,String, JSON
from sqlalchemy.orm import relationship
from app.db import Base

class User(Base):
    __tablename__ = 'user'

    id=Column(Integer, primary_key=True)
    login=Column(String)
    password=Column(String)


class Vehicle(Base):
    __tablename__ = 'vehicle'
    
    id=Column(Integer,primary_key=True)
    name=Column(String)
    description=Column(String)
    user_id = relationship(Integer, ForeignKey('user.id'))

class Area(Base):
    __tablename__ = 'area'
    
    id=Column(Integer, primary_key=True)
    name = Column(String)
    border_points = Column(JSON)
    user_id = relationship(Integer, ForeignKey('user.id'))