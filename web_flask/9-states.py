#!/usr/bin/python3
"""list the states by id"""

from flask import Flask, render_template
from models.state import State
from models import storage

app = Flask(__name__)


@app.route('/states/<id>', strict_slashes=False)
@app.route('/states', strict_slashes=False)
def states_list(id=None):
    """list all states in storage"""
    states = storage.all(State)
    if id:
        key = "State." + id
        return render_template('9-states.html', states=states, key=key)
    return render_template('7-states_list.html', states=states.values())


@app.teardown_appcontext
def close_connection(exception):
    """close the session"""
    storage.close()


if __name__ == "__main__":
    app.run('0.0.0.0', 5000)
