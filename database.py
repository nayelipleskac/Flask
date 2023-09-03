import pymongo

class Database: 
    DB = None
    users = [
    {'name': 'Anne'},
    {'name': 'Bob'},
    {'name': 'Nayeli'}]

    @staticmethod
    def initialize():
        client = pymongo.MongoClient('mongob://127.0.0.1:27017')
        Database.DB = client.mydb
    
    @staticmethod
    def insert_record(doc):
        Database.DB.users.insert_one(doc)
    @staticmethod 
    #static list of users
    #waiting to be called from app.py
    def get_users():
        print('list of users: ')
        print(users)
      
        