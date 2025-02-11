from bson import ObjectId
from datetime import datetime
import util.validate as validate
from models.group import Group
from config.database import get_db_connection
from services.bookmark_service import BookmarkService


class GroupService:
    def __init__(self):
        self.db_connection = get_db_connection()
        self.collection = self.db_connection.get_collection('GroupCollection')
        self.bookmark_service = BookmarkService()

    def find_all(self):
        cursor = self.collection.find()        
        results = cursor.to_list()
        validate.group_results(results)                    
        return results

    def find_by_id(self, id: str):
        validate.object_id(id)
        result = self.collection.find_one({'_id': ObjectId(id)})
        validate.group_result(result)   
        return result
        
    def find_by_title(self, title: str):
        cursor = self.collection.find({'title': title})
        results = cursor.to_list()
        validate.group_results(results)    
        return results

    def create(self, group: Group):
        new_group = self.collection.insert_one(group.model_dump())
        result = self.collection.find_one({'_id': new_group.inserted_id})
        return result
    
    def update(self, id: str, group: Group):
        validate.object_id(id)      
        group.__setattr__('updated_at', datetime.now())  
        update = self.collection.update_one(
            {'_id': ObjectId(id)},
            {'$set': group.model_dump()}
        )        
        validate.group_update(update)
        result = self.collection.find_one({'_id': ObjectId(id)})
        return result
    
    def delete(self, id: str):
        global bookmark_service
        validate.object_id(id)
        delete = self.collection.delete_one({'_id': ObjectId(id)})
        validate.group_delete(delete)
        self.bookmark_service.remove_bookmarks_from_group(id)