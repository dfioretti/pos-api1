from application import app
from application import api
from application import mongo
from flask.ext.restful import reqparse

from flask.ext import restful
from flask.ext.restful import abort

import json
from bson import json_util
from bson.objectid import ObjectId

parser = reqparse.RequestParser()
parser.add_argument('name', type=str)
parser.add_argument('street', type=str)
parser.add_argument('city', type=str)
parser.add_argument('state', type=str)
parser.add_argument('zip', type=str)
parser.add_argument('phone', type=str)



def to_json(data):
    return json.dumps(data, default=json_util.default)


class Merchant(restful.Resource):
    def get(self, merchant_id):
        app.logger.info(merchant_id)
        return to_json(mongo.db.merchants.find_one( { '_id' : ObjectId(merchant_id) } ))

    def put(self, merchant_id):
        args = parser.parse_args()
        mongo.db.merchants.update( { '_id' : ObjectId(merchant_id) } , { '$set' : args } )
        return to_json(mongo.db.merchants.find_one( { '_id' : ObjectId(merchant_id) } ))



class MerchantList(restful.Resource):
    def get(self):
        results = mongo.db.merchants.find()
        json_result = []
        for result in results:
            json_result.append(result)
        return to_json(json_result)

    def post(self):
        args = parser.parse_args()
        oid = mongo.db.merchants.insert(args)
        return to_json(mongo.db.merchants.find_one( { '_id' : oid } ))

#
# name, street, city, state, zip, phone

api.add_resource(Merchant, '/merchants/<string:merchant_id>')
api.add_resource(MerchantList, '/merchants')


#https://ep2013.europython.eu/conference/talks/developing-restful-web-apis-with-python-flask-and-mongodb

