#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from models import storage_type
from models.base_model import Base, BaseModel
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    if storage_type == "db":
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state",
                              cascade="all, delete, delete-orphan")
    else:
        name = ''

        @property
        def cities(self):
            """get cities that belong to that state"""
            from models import storage
            cs = storage.all(City)
            return [c for c in cs if cs.state_id == self.id]
