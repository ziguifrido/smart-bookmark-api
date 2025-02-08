from bson import json_util
import json

def list_to_json(data):
    return json.loads(json_util.dumps(data))
