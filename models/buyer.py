#!/usr/bin/python3
""" holds class buyer"""
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Buyer(BaseModel, Base):
    """Buyer class"""
    __tablename__ = 'buyers'

    username = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    password = Column(String(100), nullable=False)
    location = Column(String(100), nullable=False)
    contact_information = Column(String(100), nullable=False)
    orders = relationship('Order', backref='buyers')
    review = relationship('Review', backref='buyers')

