#!/usr/bin/python3
""" holds class order"""
import models
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Order(BaseModel, Base):
    """class order"""
    if models.storage_t == "db":
        __tablename__ = 'orders'
        buyer_id = Column(String(60), ForeignKey('buyers.id'))
        product_id = Column(String(60), ForeignKey('products.id'))
        quantity = Column(Integer)
        total_price = Column(Integer)
        payment_status = Column(String)

        buyer = relationship('Buyer', back_populates='orders')
        product = relationship('Product')
