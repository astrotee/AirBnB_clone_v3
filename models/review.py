#!/usr/bin/python3
""" Review module for the HBNB project """
from sqlalchemy import Column, ForeignKey, String
from models.base_model import Base, BaseModel
from models import storage_type


class Review(BaseModel, Base):
    """ Review classto store review information """
    __tablename__ = 'reviews'
    if storage_type == "db":
        place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        text = Column(String(1024),  nullable=False)
    else:
        place_id = ""
        user_id = ""
        text = ""
