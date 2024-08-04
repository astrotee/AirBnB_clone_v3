#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, String
from models.base_model import Base, BaseModel
from models import storage_type


class Amenity(BaseModel, Base):
    __tablename__ = 'amenities'
    if storage_type == "db":
        name = Column(String(128), nullable=False)
    else:
        name = ""
