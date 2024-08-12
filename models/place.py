#!/usr/bin/python3
""" Place Module for HBNB project """
from sqlalchemy import Column, Float, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship
from models.amenity import Amenity
from models.base_model import Base, BaseModel
from models.review import Review
from models import storage_type

if storage_type == 'db':
    place_amenity = Table('place_amenity', Base.metadata,
                          Column('place_id', ForeignKey('places.id'),
                                 primary_key=True, nullable=False),
                          Column('amenity_id', ForeignKey('amenities.id'),
                                 primary_key=True, nullable=False),
                          )


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    if storage_type == "db":
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, default=0, nullable=False)
        number_bathrooms = Column(Integer, default=0, nullable=False)
        max_guest = Column(Integer, default=0, nullable=False)
        price_by_night = Column(Integer, default=0, nullable=False)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        reviews = relationship('Review', backref='place',
                               cascade="all, delete, delete-orphan")
        amenities = relationship('Amenity', backref='place_amenities',
                                 secondary=place_amenity, viewonly=False)
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            """the FileStorage relationship between Place and Review"""
            from models import storage
            cs = storage.all(Review)
            return [c for c in cs.values() if c.place_id == self.id]

        @property
        def amenities(self):
            """returns the list of Amenity instances linked to the Place"""
            from models import storage
            cs = storage.all(Amenity)
            return [c for c in cs.values() if c.id in self.amenity_ids]

        @amenities.setter
        def amenities(self, obj):
            """returns the list of Amenity instances linked to the Place"""
            if isinstance(obj, Amenity) and obj.id not in self.amenity_ids:
                self.amenity_ids.append(obj.id)
