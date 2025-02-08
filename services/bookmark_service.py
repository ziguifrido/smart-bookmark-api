from config.database import get_db_connection

class BookmarkService:
    def __init__(self):
        self.db_connection = get_db_connection()
        self.collection = self.db_connection.get_collection('BookmarkCollection')
        
    def find_by_title(self, title: str):
        results = self.collection.find({"title": title})
        return results.to_list()

    def find_by_tag(self, tag: str):
        results = self.collection.find({"tag": tag})
        return results.to_list()
