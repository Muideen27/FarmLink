#!/usr/bin/python3
""" holds class buyer"""
from models.base_model import BaseModel
from os import getenv
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Buyer(BaseModel, Base):
    """Buyer class"""
    __tablename__ = 'buyers'

    username = Column(String)
    email = Column(String)
    password = Column(String)
    location = Column(String)
    contact_information = Column(String)
    orders = relationship('Order', backref='buyers')
    review = relationship('Review', backref='buyers')

