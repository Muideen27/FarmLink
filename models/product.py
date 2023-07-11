#!/usr/bin/python3
""" holds class Products"""
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, Integer, String, ForeignKey, Float, Text
from sqlalchemy.orm import relationship

class Product(BaseModel, Base):
    """class products"""
    __tablename__ = 'products'
    farmer_id = Column(String(60), ForeignKey('farmers.id'))
    name = Column(String(100), nullable=False)
    description = Column(Text, nullable=False)
    quantity = Column(Integer)
    price = Column(Float)
    location = Column(String(100), nullable=False)
    availability_status = Column(String(100), nullable=False)

