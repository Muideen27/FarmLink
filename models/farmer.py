#!/usr/bin/python3
""" holds class farmer"""
from models.base_model import BaseModel, Base
from models.product import Product
from os import getenv
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

class Farmer(BaseModel, Base):
    """class farmer"""
    __tablename__ = 'farmers'

    username = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    password = Column(String(100), nullable=False)
    confirm_password = Column(String(100), nullable=False)
    image = Column(String(100))
    location = Column(String(280), nullable=False)
    contact_information = Column(String(100), nullable=False)
    products = relationship('Product', backref='farmers')
    review = relationship('Review', backref='farmers')

