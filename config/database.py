import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv('.env.local')

MONGODB_URL = os.getenv("MONGODB_URL")

client = MongoClient(MONGODB_URL)
db_connection = client['SmartBookmark']

def get_db_connection():
    return db_connection
