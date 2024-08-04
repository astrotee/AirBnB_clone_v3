#!/usr/bin/python3
"""list the states"""

from flask import Flask, render_template
from models.state import State
from models import storage

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """list all states in storage"""
    states = storage.all(State)
    sorted_states = [v for v in sorted(states.values(), key=lambda s: s.name)]
    return render_template('7-states_list.html', states=sorted_states)


@app.teardown_appcontext
def close_connection(exception):
    """close the session"""
    storage.close()


if __name__ == "__main__":
    app.run('0.0.0.0', 5000)
