#!/usr/bin/python3
""" holds class Review"""
from models.base_model import BaseModel
from os import getenv
from sqlalchemy import Column, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from models.buyer import Buyer
from models.farmer import Farmer

Base = declarative_base()

class Review(BaseModel, Base):
    """Representation of Review"""
    __tablename__ = 'reviews'
    rating = Column(Float)
    comment = Column(String)
    buyer_id = Column(String(60), ForeignKey('buyers.id'))
    farmer_id = Column(String(60), ForeignKey('farmers.id'))

