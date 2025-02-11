from bson import ObjectId
from datetime import datetime
import util.validate as validate
from models.bookmark import Bookmark
from config.database import get_db_connection

class BookmarkService:
    def __init__(self):
        self.db_connection = get_db_connection()
        self.collection = self.db_connection.get_collection('BookmarkCollection')
     
    def find_by_id(self, id: str):
        validate.object_id(id)
        result = self.collection.find_one({'_id': ObjectId(id)})        
        validate.bookmark_result(result)            
        return result
        
    def find_all(self):
        results = self.collection.find()        
        validate.bookmark_results(results)                    
        return results.to_list()
        
    def find_by_title(self, title: str):
        results = self.collection.find({'title': title})
        validate.bookmark_results(results)    
        return results.to_list()
    
    def find_by_group_id(self, group_id: str):
        validate.object_id(group_id)
        results = self.collection.find({'group_id': group_id})
        validate.bookmark_results(results)
        return results.to_list()

    def find_by_tag(self, tag: str):
        results = self.collection.find({'tags': tag})
        validate.bookmark_results(results)
        return results.to_list()

    def create(self, bookmark: Bookmark):
        new_bookmark = self.collection.insert_one(bookmark.model_dump())
        result = self.collection.find_one({'_id': new_bookmark.inserted_id})
        return result
    
    def update(self, id: str, bookmark: Bookmark):
        validate.object_id(id)      
        bookmark.__setattr__('updated_at', datetime.now())  
        update = self.collection.update_one(
            {'_id': ObjectId(id)},
            {'$set': bookmark.model_dump()}
        )        
        validate.bookmark_update(update)        
        result = self.collection.find_one({'_id': ObjectId(id)})
        return result
    
    def delete(self, id: str):
        validate.object_id(id)
        delete = self.collection.delete_one({'_id': ObjectId(id)})
        validate.bookmark_delete(delete)
            
    def add_bookmark_to_group(self, id: str, group_id: str):
        validate.object_id(id)
        validate.object_id(group_id)
        update = self.collection.update_one(
            {'_id': ObjectId(id)},
            {'$set': {
                'group_id': group_id,
                'updated_at': datetime.now()
            }}
        )
        validate.bookmark_update(update)
        result = self.collection.find_one({'_id': ObjectId(id)})
        return result
    
    def remove_bookmarks_from_group(self, group_id: str):
        validate.object_id(group_id)
        self.collection.update_many(
            {'group_id': group_id},
            {'$set': {
                'group_id': None,
                'updated_at': datetime.now()
            }}
        )

         
