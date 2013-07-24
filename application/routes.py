from application import api
from application.controllers.site import SiteResource
from application.controllers.merchant import Merchant

api.add_resource(SiteResource, '/')
