#!/usr/bin/python3
"""hello, world with flask"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """root route"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """hbnb route"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text: str):
    """what about C?"""
    return f"C {text.replace('_', ' ')}"


@app.route('/python', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text: str):
    """what about python?"""
    return f"Python {text.replace('_', ' ')}"


if __name__ == "__main__":
    app.run('0.0.0.0', 5000)
