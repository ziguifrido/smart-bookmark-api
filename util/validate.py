from bson import ObjectId
from util.error import bad_request

def object_id(id: str):
    try:
        ObjectId(id)
    except:
        bad_request("Invalid ObjectId")
