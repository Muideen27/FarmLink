#!/usr/bin/python3
""" holds class farmer"""
import models
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from models.user import User
from models.product import Product

class Farmer(User):
    if models.storage_t == "db":
        """class farmer"""
        __tablename__ = 'farmers'

        id = Column(String(60), ForeignKey('users.id'), primary_key=True)
        products = relationship(Product, back_populates='farmer')

        __mapper_args__ = {
            'polymorphic_identity': 'Farmer'
        }
