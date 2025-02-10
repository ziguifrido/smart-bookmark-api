from bson import ObjectId
from datetime import datetime
import util.validate as validate
from util.error import not_found
from models.group import Group
from config.database import get_db_connection


class GroupService:
    def __init__(self):
        self.db_connection = get_db_connection()
        self.collection = self.db_connection.get_collection('GroupCollection')

    def find_by_id(self, id: str):
        validate.object_id(id)
        result = self.collection.find_one({"_id": ObjectId(id)})        
        if not result:
            not_found("No Group found")            
        return result
        
    def find_all(self):
        results = self.collection.find()        
        if not results:
            not_found("No Group found")                    
        return results.to_list()
        
    def find_by_title(self, title: str):
        results = self.collection.find({"title": title})
        if not results:
            not_found("No Group found")    
        return results.to_list()

    def create(self, group: Group):
        new_group = self.collection.insert_one(group.model_dump())
        result = self.collection.find_one({"_id": new_group.inserted_id})
        return result
    
    def update(self, id: str, group: Group):
        validate.object_id(id)      
        group.__setattr__('updated_at', datetime.now())  
        update = self.collection.update_one(
            {"_id": ObjectId(id)},
            {"$set": group.model_dump()}
        )        
        if update.modified_count == 0:
            not_found("Group not found")        
        result = self.collection.find_one({"_id": ObjectId(id)})
        return result
    
    def delete(self, id: str):
        validate.object_id(id)
        result = self.collection.delete_one({"_id": ObjectId(id)})
        if result.deleted_count == 0:
            not_found("Group not found")