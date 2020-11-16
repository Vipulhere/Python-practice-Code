import pymongo
conn=pymongo.MongoClient("mongodb://localhost:27017")
database=conn["Python"]
collection=database["user"]
query={"age":{"$regex":"^16"}}
count=collection.delete_many(query)
print(count.deleted_count,"documents deleted")
for a in collection.find():
    print(a)

#collection.delete_many({})