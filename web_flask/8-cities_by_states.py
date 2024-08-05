#!/usr/bin/python3
"""list the cities by states"""

from flask import Flask, render_template
from models.state import State
from models import storage

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def states_list():
    """list all cities by states in storage"""
    states = storage.all(State)
    print(states)
    return render_template('8-cities_by_states.html', states=states.values())


@app.teardown_appcontext
def close_connection(exception):
    """close the session"""
    storage.close()


if __name__ == "__main__":
    app.run('0.0.0.0', 5000)
