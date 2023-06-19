#!/usr/bin/python3
""" holds class users"""
import models
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, Integer, String, Enum, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(BaseModel, Base):
    """Representation of user"""
    if models.storage_t == "db":
        __tablename__ = 'users'
        username = Column(String)
        email = Column(String)
        password = Column(String)
        role = Column(Enum('Buyer', 'Farmer'))
        profile_picture = Column(String)
        location = Column(String)
        contact_information = Column(String)
        products = relationship('Product', back_populates='farmer')
        orders = relationship('Order', back_populates='buyer')
        reviews = relationship('Review', back_populates='user')
