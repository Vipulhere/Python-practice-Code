import pymongo
conn=pymongo.MongoClient("mongodb://localhost:27017/")
database=conn["Python"]
collection=database["user"]
for find in collection.find():
    print(find)