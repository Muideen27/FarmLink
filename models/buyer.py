#!/usr/bin/python3
""" holds class buyer"""
import models
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy import Column, Integer, String, Enum, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from user import User
from order import Order

Base = declarative_base()

class Buyer(User):
    """Buyer class"""
    if models.storage_t == "db":
        __tablename__ = 'buyers'

        id = Column(String(60), ForeignKey('users.id'), primary_key=True)
        orders = relationship('Order', back_populates='buyer')

        __mapper_args__ = {
            'polymorphic_identity': 'Buyer'
        }
