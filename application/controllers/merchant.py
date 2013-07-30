from application import app
from application import api
from application import mongo

from flask.ext import restful
from flask.ext.restful import abort

import json
from bson import json_util



def json_fmt(cursor):
    json_docs = []
    for doc in cursor:
        json_doc = json.dumps(doc, default=json_util.default)
        json_docs.append(json_doc)
    return json_docs


class Merchant(restful.Resource):
    def get(self):
        mongo.db.tests.save(test)
        return {
            'merchant': True
        }

class MerchantList(restful.Resource):
    def get(self):
        cursor = mongo.db.merchants.find()
        return json_fmt(cursor)

#
# name, street, city, state, zip, phone

api.add_resource(Merchant, '/merchant/<string:merchant_id>')
api.add_resource(MerchantList, '/merchants')



