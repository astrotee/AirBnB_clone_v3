#!/usr/bin/python3
""" api index """
from flask import jsonify
from api.v1.views import app_views
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


@app_views.route('/status', strict_slashes=False)
def status():
    """ check the status of the api """
    return jsonify({'status': 'OK'})


@app_views.route('/stats', strict_slashes=False)
def stats():
    """ get stats about the stored objects """
    classes = [Amenity, City, Place, Review, State, User]

    num_obj = {}
    for cls in classes:
        num_obj[cls.__tablename__] = storage.count(cls)
    return jsonify(num_obj)
