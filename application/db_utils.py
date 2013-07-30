import json
from bson import json_util
from bson.objectid import ObjectId

def to_json(data):
    return json.dumps(data, default=json_util.default)


