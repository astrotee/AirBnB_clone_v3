#!/usr/bin/python3
"""hbnb filters page"""

from flask import Flask, render_template
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.user import User
from models import storage

app = Flask(__name__)


@app.route('/hbnb', strict_slashes=False)
def hbnb_filters():
    """display filters page"""
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    places = storage.all(Place).values()
    users = storage.all(User)
    dict_places = []
    for place in places:
        place = place.to_dict()
        user = users["User."+place['user_id']]
        place['user'] = ' '.join([user.first_name, user.last_name])
        dict_places.append(place)
    return render_template('100-hbnb.html', states=states,
                           amenities=amenities, places=dict_places,
                           users=users)


@app.teardown_appcontext
def close_connection(exception):
    """close the session"""
    storage.close()


if __name__ == "__main__":
    app.run('0.0.0.0', 5000)
