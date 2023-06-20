#!/usr/bin/python3
""" holds class Review"""
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String, ForeignKey, Float
from sqlalchemy.orm import relationship

class Review(BaseModel, Base):
    """Representation of Review"""
    __tablename__ = 'reviews'
    rating = Column(Float)
    comment = Column(String(100), nullable=False)
    buyer_id = Column(String(60), ForeignKey('buyers.id'))
    farmer_id = Column(String(60), ForeignKey('farmers.id'))

