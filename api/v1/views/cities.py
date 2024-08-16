#!/usr/bin/python3
""" cities api """
from flask import jsonify, abort, request
from api.v1.views import app_views
from models import storage
from models.state import State
from models.city import City


@app_views.route('/states/<state_id>/cities', methods=['GET'],
                 strict_slashes=False)
def get_state_cities(state_id):
    """ get cities"""
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    return jsonify([s.to_dict() for s in storage.all(City).values()
                    if s.state_id == state.id
                    ]
                   )


@app_views.route('/cities/<city_id>', methods=['GET'], strict_slashes=False)
def get_city(city_id=None):
    """ get city by id """
    city = storage.get(City, city_id)
    if city is None:
        abort(404)
    return jsonify(city.to_dict())


@app_views.route('/states/<state_id>/cities', methods=['POST'],
                 strict_slashes=False)
def create_cities(state_id=None):
    """ create a city """
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    data = request.get_json(silent=True)
    if not data:
        abort(400, description='Not a JSON')
    if 'name' not in data:
        abort(400, description='Missing name')
    city = City(**data)
    city.state_id = state.id
    city.save()
    return jsonify(city.to_dict()), 201


@app_views.route('/cities/<city_id>', methods=['PUT'], strict_slashes=False)
def update_cities(city_id=None):
    """ update a city """
    city = storage.get(City, city_id)
    if city is None:
        abort(404)
    data = request.get_json(silent=True)
    if not data:
        abort(400, description='Not a JSON')
    for k in data:
        if k not in ['id', 'state_id', 'created_at', 'updated_at']:
            setattr(city, k, data[k])
    storage.save()
    return jsonify(city.to_dict()), 200


@app_views.route('/cities/<city_id>', methods=['DELETE'], strict_slashes=False
                 )
def del_cities(city_id=None):
    """ delete a city """
    city = storage.get(City, city_id)
    if city is None:
        abort(404)
    storage.delete(city)
    storage.save()
    return {}, 200
