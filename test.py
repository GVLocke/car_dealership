from functions import connect_to_mongo, search_users
from class_definitions import User
from bson import ObjectId

db = connect_to_mongo()
collection = db['user']

search = {'_id':ObjectId('643f9385079c3291b22ea08f')}
new_values = {'$set':{'password':'test3'}}
collection.update_one(search, new_values)