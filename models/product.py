#!/usr/bin/python3
""" holds class Products"""
from models.base_model import BaseModel
from os import getenv
from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Product(BaseModel, Base):
    """class products"""
    __tablename__ = 'products'
    farmer_id = Column(String(60), ForeignKey('farmers.id'))
    name = Column(String)
    description = Column(String)
    quantity = Column(Integer)
    price = Column(Float)
    location = Column(String)
    availability_status = Column(String)

