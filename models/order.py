#!/usr/bin/python3
""" holds class order"""
from models.base_model import BaseModel
from os import getenv
from sqlalchemy import Column, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Order(BaseModel, Base):
    """class order"""
    __tablename__ = 'orders'
    buyer_id = Column(String(60), ForeignKey('buyers.id'))
    product_id = Column(String(60), ForeignKey('products.id'))
    total_price = Column(Float)
    payment_status = Column(String)
