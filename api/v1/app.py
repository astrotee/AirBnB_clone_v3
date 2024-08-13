#!/usr/bin/python3
""" api Flask app """
from os import environ
from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views

app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def close(error):
    """close the storage session"""
    storage.close()


@app.errorhandler(404)
def page_not_found(error):
    """ handle 404 errors """
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    app.run(environ.get('HBNB_API_HOST', '0.0.0.0'),
            environ.get('HBNB_API_PORT', '5000'), threaded=True)
