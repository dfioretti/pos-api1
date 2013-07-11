from flask import Flask, jsonify, request
from flask.ext.pymongo import PyMongo
from flask.ext.restful import Resource, Api

# app configuration
app = Flask(__name__)

api = Api(app)

mongo = PyMongo(app)

class HelloWorld(Resource):
    def get(self):
        return { 'hello' : 'world' }

api.add_resource(HelloWorld, '/api')



@app.route('/')
def index():
    return "Hello, World!"

@app.route('/test')
def test():
    test = { 'first' : 'uno', 'second' : 'dos', 'third' : 'tres' }
    mongo.db.tests.save(test)


if __name__ == '__main__':
    app.run(debug = True, port=5001)
