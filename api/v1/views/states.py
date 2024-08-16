#!/usr/bin/python3
""" states api """
from flask import jsonify, abort, request
from api.v1.views import app_views
from models import storage
from models.state import State


@app_views.route('/states/<state_id>', methods=['GET', 'DELETE', 'PUT'],
                 strict_slashes=False)
@app_views.route('/states', methods=['GET', 'POST'], strict_slashes=False)
def get_states(state_id=None):
    """ get states"""
    if state_id:
        state = storage.get(State, state_id)
        if state is None:
            abort(404)
        if request.method == 'GET':
            return jsonify(state.to_dict())
        elif request.method == 'DELETE':
            storage.delete(state)
            storage.save()
            return {}, 200
    if request.method == 'GET':
        return jsonify([s.to_dict() for s in storage.all(State).values()])
    elif request.method == 'POST':
        data = request.get_json(silent=True)
        if not data:
            abort(400, description='Not a JSON')
        if 'name' not in data:
            abort(400, description='Missing name')
        state = State(**data)
        state.save()
        return jsonify(state.to_dict()), 201
    elif request.method == 'PUT':
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
