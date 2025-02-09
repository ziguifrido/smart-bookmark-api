from bson import ObjectId
import util.validate as validate
from util.error import not_found
from models.bookmark import Bookmark
from config.database import get_db_connection

class BookmarkService:
    def __init__(self):
        self.db_connection = get_db_connection()
        self.collection = self.db_connection.get_collection('BookmarkCollection')
        
    def find_by_id(self, id: str):
        validate.object_id(id)
        result = self.collection.find_one({"_id": ObjectId(id)})        
        if not result:
            not_found("No Bookmark found")            
        return result
        
    def find_all(self):
        results = self.collection.find()        
        if not results:
            not_found("No Bookmark found")                    
        return results.to_list()
        
    def find_by_title(self, title: str):
        results = self.collection.find({"title": title})
        if not results:
            not_found("No Bookmark found")    
        return results.to_list()
    
    def find_by_group(self, group: str):
        results = self.collection.find({"group": group})
        if not results:
            not_found("No Bookmark found")    
        return results.to_list()

    def find_by_tag(self, tag: str):
        results = self.collection.find({"tags": tag})
        if not results:
            not_found("No Bookmark found")    
        return results.to_list()

    def create(self, bookmark: Bookmark):
        new_bookmark = self.collection.insert_one(bookmark.model_dump())
        result = self.collection.find_one({"_id": new_bookmark.inserted_id})
        return result
    
    def update(self, id: str, bookmark: Bookmark):
        validate.object_id(id)        
        update = self.collection.update_one(
            {"_id": ObjectId(id)},
            {"$set": bookmark.model_dump()}
        )        
        if update.modified_count == 0:
            not_found("Bookmark not found")        
        result = self.collection.find_one({"_id": ObjectId(id)})
        return result
    
    def delete(self, id: str):
        validate.object_id(id)
        result = self.collection.delete_one({"_id": ObjectId(id)})
        if result.deleted_count == 0:
            not_found("Bookmark not found")
         
