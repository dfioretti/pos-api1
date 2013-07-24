from application import app

from flask.ext import restful
from flask.ext.restful import abort

class Merchant(restful.Resource):
    def get(self):
        return {
            'merchant': True
        }



