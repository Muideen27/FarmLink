#!/usr/bin/python3
""" holds class farmer"""
from models.base_model import BaseModel, Base
from models.product import Product
from os import getenv
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from flask_login import UserMixin
from flask_bcrypt import generate_password_hash, check_password_hash


class Farmer(UserMixin, BaseModel, Base):
    """class farmer"""
    __tablename__ = 'farmers'

    username = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    hashed_password = Column(String(100), nullable=False)
    location = Column(String(280), nullable=False)
    contact_information = Column(String(100), nullable=False)
    products = relationship('Product', backref='farmers')
    review = relationship('Review', backref='farmers')
    
    def __init__(self, username, hashed_password, email, location, contact_information):
        """Implemented hashed password"""
        super().__init__()
        self.username = username
        self.hashed_password = self.hash_password(hashed_password)
        self.email = email
        self.location = location
        self.contact_information = contact_information

    def hash_password(self, password):
        self.hashed_password = generate_password_hash(password)
        return self.hashed_password
    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)