#!/usr/bin/python3
""" Write a script that starts a Flask web application
"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """/: display “Hello HBNB!”"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """/hbnb: display “HBNB”"""
    return 'HBNB'


@app.route('/c/<var>', strict_slashes=False)
def c(var):
    """/c/<text>: display “C ” followed by the value of the text variable
    (replace underscore _ symbols with a space )"""
    return str(f"C {var.replace('_', ' ')}")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
