from flask import Flask, jsonify, request
from functools import wraps
from flask.ext.pymongo import PyMongo
from flask.ext.restful import Resource, Api, reqparse
import json
from bson import json_util

# app configuration
app = Flask(__name__)

api = Api(app=app, prefix='/api/v1')

mongo = PyMongo(app)


def json_fmt(cursor):
    json_docs = []
    for doc in cursor:
        json_doc = json.dumps(doc, default=json_util.default)
        json_docs.append(json_doc)
    return json_docs

# build auth
def basic_authetication():
    return True

def authenticate(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not getattr(func, 'authenticated', True):
            return func(*args, **kwargs)
        acct = basic_authetication()
        if acct:
            return func(*args, **kwargs)
        abort(401)
    return wrapper

class Merchant(Resource):
    def get(self, merchant_id):
        return mongo.db.merchants.find_one( { 'merchant_id' : merchant_id } )

    def delete(self, merchant_id):
        mongo.db.merchants.remove( { 'merchant_id' : merchant_id } )

    def put(self, merchant_id):
        args = parser.parse_args()
        merchant = { 'merchant' : args['merchant'] }
        mongo.db.merchants.save( merchant )

class MerchantList(Resource):
    def get(self):
        cursor = mongo.db.merchants.find()
        return json_fmt(cursor)

# test code
class APIRunning(Resource):
    method_decorators = [authenticate]
    def get(self):
        # for reference
        app.logger.info('informing')
        app.logger.warning('warning')
        app.logger.error('error')
        return { 'running' : 'yes' }



api.add_resource( APIRunning, '/' )
api.add_resource( Merchant, '/merchant/<string:merchant_id>' )
api.add_resource( MerchantList, '/merchants' )



# raw flask (test code)
@app.route('/')
def index():
    return "Flask Running..."

@app.route('/db-test')
def test():
    test = { 'first' : 'uno', 'second' : 'dos', 'third' : 'tres' }
    mongo.db.tests.save(test)
    return "Success!"


if __name__ == '__main__':
    app.run(debug = True, port=5001)

# resource
# http://stackoverflow.com/questions/739654/how-can-i-make-a-chain-of-function-decorators-in-python
# https://github.com/twilio/flask-restful/issues/18 multiple files blueprint
