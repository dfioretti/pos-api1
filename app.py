#!../env/flask/bin/python
from flask import Flask, jsonify
from flask.ext.pymongo import PyMongo


app = Flask(__name__)
mongo = PyMongo(app)


@app.route('/')
def index():
    return "Hello, World!"

@app.route('/test')
def test():
    test = { 'first' : 'uno', 'second' : 'dos', 'third' : 'tres' }
    mongo.db.tests.save(test)


if __name__ == '__main__':
    app.run(debug = True)
