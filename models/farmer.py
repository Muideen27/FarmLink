#!/usr/bin/python3
""" holds class farmer"""
from models.base_model import BaseModel
from models.product import Product
from os import getenv
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class Farmer(BaseModel, Base):
    """class farmer"""
    __tablename__ = 'farmers'

    username = Column(String)
    email = Column(String)
    password = Column(String)
    location = Column(String)
    contact_information = Column(String)
    products = relationship('Product', backref='farmers')
    review = relationship('Review', backref='farmers')

