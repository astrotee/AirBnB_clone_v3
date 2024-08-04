#!/usr/bin/python3
"""This module defines a class to manage database storage for hbnb clone"""
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models.amenity import Amenity
from models.base_model import Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class DBStorage:
    """This class manages storage of hbnb models in database"""
    __engine = None
    __session = None

    def __init__(self) -> None:
        user = os.getenv("HBNB_MYSQL_USER", "hbnb_dev")
        password = os.getenv("HBNB_MYSQL_PWD", "hbnb_dev_pwd")
        host = os.getenv("HBNB_MYSQL_HOST", "localhost")
        database = os.getenv("HBNB_MYSQL_DB", "hbnb_dev_db")
        environment = os.getenv("HBNB_ENV", "dev")
        self.__engine = create_engine(
                f"mysql+mysqldb://{user}:{password}@{host}/{database}",
                pool_pre_ping=True)
        if environment == "test":
            Base.metadata.drop_all()

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        records = dict()
        tables: list

        if cls:
            tables = [cls]
        else:
            tables = [User, State, City, Place, Review, Amenity]
        for c in tables:
            objs = self.__session.query(c).all()
            records.update({f"{o.__class__.__name__}.{o.id}": o for o in objs})
        return records

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.__session.add(obj)

    def delete(self, obj=None):
        """Deletes an object from storage dictionary"""
        if obj:
            self.__session.delete(obj)

    def save(self):
        """Saves storage dictionary to file"""
        self.__session.commit()

    def reload(self):
        """Loads storage dictionary from file"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        self.__session = scoped_session(session_factory)()

    def close(self):
        """close the session"""
        self.__session.close()
