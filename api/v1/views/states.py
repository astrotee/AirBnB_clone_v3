#!/usr/bin/python3
""" states api """
from flask import jsonify, abort, request
from api.v1.views import app_views
from models import storage
from models.state import State


@app_views.route('/states', methods=['GET'], strict_slashes=False)
def get_states():
    """ get states"""
    return jsonify([s.to_dict() for s in storage.all(State).values()])


@app_views.route('/states/<state_id>', methods=['GET'], strict_slashes=False)
def get_state(state_id=None):
    """ get state by id """
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    return jsonify(state.to_dict())


@app_views.route('/states', methods=['POST'], strict_slashes=False)
def create_states():
    """ create a state """
    data = request.get_json(silent=True)
    if not data:
        abort(400, description='Not a JSON')
    if 'name' not in data:
        abort(400, description='Missing name')
    state = State(**data)
    state.save()
    return jsonify(state.to_dict()), 201


@app_views.route('/states/<state_id>', methods=['PUT'], strict_slashes=False)
def update_states(state_id=None):
    """ update a state """
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    data = request.get_json(silent=True)
    if not data:
        abort(400, description='Not a JSON')
    for k in data:
        if k not in ['id', 'created_at', 'updated_at']:
            setattr(state, k, data[k])
    storage.save()
    return jsonify(state.to_dict()), 200


@app_views.route('/states/<state_id>', methods=['DELETE'], strict_slashes=False
                 )
def del_states(state_id=None):
    """ delete a state """
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    storage.delete(state)
    storage.save()
    return {}, 200
