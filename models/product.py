#!/usr/bin/python3
""" holds class Products"""
import models
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Product(BaseModel, Base):
    """class products"""
    if models.storage_t == "db":
        __tablename__ = 'products'
        farmer_id = Column(String(60), ForeignKey('farmers.id'))
        name = Column(String)
        description = Column(String)
        quantity = Column(Integer)
        price = Column(Integer)
        location = Column(String)
        availability_status = Column(String)
        farmer = relationship('Farmer', back_populates='products')
