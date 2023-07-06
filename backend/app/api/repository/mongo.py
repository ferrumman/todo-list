import os
from pymongo import MongoClient

mongo_uri = f"mongodb://{os.getenv('MONGO_HOST')}:{os.getenv('MONGO_PORT')}"

mongodb_client = MongoClient(mongo_uri)
database = mongodb_client[os.getenv("DB_NAME")]
print("Connected to the MongoDB database!")




class Mongo:
    mongodb_client = None
    database = None

    def __init__(self):
        try:
            mongo_uri = f"mongodb://{os.getenv('MONGO_HOST')}:{os.getenv('MONGO_PORT')}"

            self.mongodb_client = MongoClient(mongo_uri)

            self.database = mongodb_client[os.getenv("DB_NAME")]
            print("Connected to the MongoDB database!")
        except Exception as e:
            print("Error ", e)

    def insert_one(self, collection, data, options=None):
        print('Insert some values')
        database[collection].insert_one(data)


def get_mongo_client():
    return Mongo()
