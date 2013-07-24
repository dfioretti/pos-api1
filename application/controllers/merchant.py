from application import app
from application import api

from flask.ext import restful
from flask.ext.restful import abort

class Merchant(restful.Resource):
    def get(self):
        return {
            'merchant': True
        }

api.add_resource(Merchant, '/merchant')



