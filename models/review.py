#!/usr/bin/python3
""" holds class Review"""
import models
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from user import User
from product import Product

class Review(BaseModel, Base):
    """Representation of Review"""
    if models.storage_t == 'db':
        __tablename__ = 'reviews'

        user_id = Column(String(60), ForeignKey('users.id'))
        product_id = Column(String(60), ForeignKey('products.id'))
        rating = Column(Float)
        comment = Column(String)

        user = relationship(User, backref='reviews')
        product = relationship(Product, backref='reviews')
