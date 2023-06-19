#!/usr/bin/python3
""" holds class Review"""
import models
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from models.user import User
from models.product import Product

class Review(BaseModel, Base):
    """Representation of Review"""
    if models.storage_t == 'db':
        __tablename__ = 'reviews'
        rating = Column(Float)
        comment = Column(String)
        user_id = Column(String(60), ForeignKey('users.id'))
        product_id = Column(String(60), ForeignKey('products.id'))

        user = relationship(User, backref='reviews')
        product = relationship(Product, backref='reviews')
