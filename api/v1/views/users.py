#!/usr/bin/python3
""" users api """
from flask import jsonify, abort, request
from api.v1.views import app_views
from models import storage
from models.user import User


@app_views.route('/users', methods=['GET'], strict_slashes=False)
def get_users():
    """ get users"""
    return jsonify([s.to_dict() for s in storage.all(User).values()])


@app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
def get_user(user_id=None):
    """ get user by id """
    user = storage.get(User, user_id)
    if user is None:
        abort(404)
    return jsonify(user.to_dict())


@app_views.route('/users', methods=['POST'], strict_slashes=False)
def create_users():
    """ create a user """
    data = request.get_json(silent=True)
    if not data:
        abort(400, description='Not a JSON')
    if 'email' not in data:
        abort(400, description='Missing email')
    if 'password' not in data:
        abort(400, description='Missing password')
    user = User(**data)
    user.save()
    return jsonify(user.to_dict()), 201


@app_views.route('/users/<user_id>', methods=['PUT'], strict_slashes=False)
def update_users(user_id=None):
    """ update a user """
    user = storage.get(User, user_id)
    if user is None:
        abort(404)
    data = request.get_json(silent=True)
    if not data:
        abort(400, description='Not a JSON')
    for k in data:
        if k not in ['id', 'email', 'created_at', 'updated_at']:
            setattr(user, k, data[k])
    storage.save()
    return jsonify(user.to_dict()), 200


@app_views.route('/users/<user_id>', methods=['DELETE'], strict_slashes=False
                 )
def del_users(user_id=None):
    """ delete a user """
    user = storage.get(User, user_id)
    if user is None:
        abort(404)
    storage.delete(user)
    storage.save()
    return {}, 200
