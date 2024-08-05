#!/usr/bin/python3
"""hbnb filters page"""

from flask import Flask, render_template
from models.state import State
from models.amenity import Amenity
from models import storage

app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """display filters page"""
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    return render_template('10-hbnb_filters.html', states=states,
                           amenities=amenities)


@app.teardown_appcontext
def close_connection(exception):
    """close the session"""
    storage.close()


if __name__ == "__main__":
    app.run('0.0.0.0', 5000)
