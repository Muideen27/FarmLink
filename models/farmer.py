#!/usr/bin/python3
""" holds class farmer"""
import models
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from models.product import Product

class Farmer(BaseModel, Base):
    if models.storage_t == "db":
        """class farmer"""
        __tablename__ = 'farmers'

        username = Column(String)
        email = Column(String)
        password = Column(String)
        profile_picture = Column(String)
        location = Column(String)
        contact_information = Column(String)
        products = relationship('product', backref='farmer')
