import json
from bson import json_util

def list_to_json(data):
    return json.loads(json_util.dumps(data))

def model_to_json(data):
    return json.loads(json.dumps(data, indent=4, default=str))
