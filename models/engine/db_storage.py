#!/usr/bin/python3
"""
Contains the class DBStorage
"""

import models
from models.base_model import BaseModel, Base
from models.product import Product
from models.order import Order
from models.farmer import Farmer
from models.buyer import Buyer
from models.review import Review
from os import getenv
from sqlalchemy import create_engine, text
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.orm.exc import NoResultFound
from flask_bcrypt import check_password_hash


classes = {"Product": Product, "Order": Order,
           "Review": Review, "Farmer": Farmer, "Buyer": Buyer}


class DBStorage:
    """interaacts with the MySQL database"""
    __engine = None
    __session = None

    def __init__(self):
        """Instantiate a DBStorage object"""
        HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
        HBNB_ENV = getenv('HBNB_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(HBNB_MYSQL_USER,
                                             HBNB_MYSQL_PWD,
                                             HBNB_MYSQL_HOST,
                                             HBNB_MYSQL_DB))
        if HBNB_ENV == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session"""
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return (new_dict)

    def new(self, obj):
        """add the object to the current database session"""
        obj.hashed_password = obj.hash_password(obj.hashed_password)
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.remove()

    def get(self, cls, id):
        """
        Returns the object based on the class name and its ID, or
        None if not found
        """
        if cls not in classes.values():
            return None

        all_cls = models.storage.all(cls)
        for value in all_cls.values():
            if value.id == id:
                if isinstance(value, Farmer) or isinstance(value, Buyer):
                    value.password = value.hashed_password
                return value
        return None
    
    def count(self, cls=None):
        """
        count the number of objects in storage
        """
        all_class = classes.values()

        if not cls:
            count = 0
            for clas in all_class:
                count += len(models.storage.all(clas).values())
        else:
            count = len(models.storage.all(cls).values())

        return count

    def check_duplicate_email(self, email, class_name):
        """
            check for duplicate email
        """
        cls = classes.get(class_name)
        if cls:
            exists = self.__session.query(cls).filter_by(email=email).first()
            return exists is not None
        else:
            raise ValueError(f"Invalid class name: {class_name}")
        
    def authenticate_user(self, email, password, user_type):
        """
            Authenticate a user of the specified type (Farmer or Buyer)
            based on the provided username and password.
            Return the user object if authentication is successful, otherwise return None.
        """
        if user_type == 'Farmer':
            user_cls = Farmer
        elif user_type == 'Buyer':
            user_cls = Buyer
        else:
            raise ValueError(f"Invalid user type: {user_type}")
        
        email = email.strip()
        password = password.strip()

        try:
            # Find the user by username in the database
            user = self.__session.query(user_cls).filter_by(email=email).first()
        except NoResultFound:
            None
        
        if user:
            # Check if the user exists and the password matches
            if (user.email and user.email == email) or (user.hashed_password and check_password_hash(user.hashed_password, password.strip())):
                
                print("Authentication successful")
                return user
                
        print("Authentication failed")
        return None
    
    def get_number_by_name(self, farmer_id, name):
        """
        Retrieve the number based on the product name and farmer ID
        """
        query = text(f"SELECT COUNT(*) FROM products WHERE farmer_id = '{farmer_id}' AND name = '{name}';")
        result = self.__session.execute(query).scalar()
        if result is not None:
            return result
        return None