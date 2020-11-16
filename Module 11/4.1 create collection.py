import pymongo
conn=pymongo.MongoClient("mongodb://localhost:27017")
database=conn['Python']
collection=database.list_collection_names()
print(database.list_collection_names())
if "user" in collection:
    print("The collection is exist")