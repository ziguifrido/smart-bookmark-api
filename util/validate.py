from bson import ObjectId
from util.error import bad_request, not_found

def object_id(id: str):
    try:
        ObjectId(id)
    except:
        bad_request('Invalid ObjectId')        
     
# --------------- Bookmark ---------------
def bookmark_result(result):
    if not result:
        not_found('No Bookmark found')
        
def bookmark_results(results):
    if len(results) == 0:
        not_found('No Bookmark found')
        
def bookmark_update(update):
    if update.modified_count == 0:
        not_found('Bookmark not found')

def bookmark_delete(delete):
    if delete.deleted_count == 0: 
        not_found('Bookmark not found')
        
# ---------------- Group ----------------
def group_result(result):
    if not result:
        not_found('No Group found')
        
def group_results(results):
    if len(results) == 0:
        not_found('No Group found')
        
def group_update(update):
    if update.modified_count == 0:
        not_found('Group not found')

def group_delete(delete):
    if delete.deleted_count == 0: 
        not_found('Group not found')