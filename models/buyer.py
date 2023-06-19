#!/usr/bin/python3
""" holds class buyer"""
import models
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from models.order import Order

Base = declarative_base()

class Buyer(BaseModel, Base):
    """Buyer class"""
    if models.storage_t == "db":
        __tablename__ = 'buyers'

        username = Column(String)
        email = Column(String)
        password = Column(String)
        profile_picture = Column(String)
        location = Column(String)
        contact_information = Column(String)
        orders = relationship('Order', backref='buyer')

