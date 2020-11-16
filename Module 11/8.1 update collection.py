'''import pymongo
conn=pymongo.MongoClient("mongodb://localhost:27017")
database=conn["Python"]
collection=database["user"]
query={"name":"alexa"}
newvalue={"$set":{"name":"Alexa David"}}
collection.update_one(query,newvalue)
for a in collection.find():
    print(a) '''
import pymongo
conn=pymongo.MongoClient("mongodb://localhost:27017")
database=conn["Python"]
collection=database["user"]
query={"name":{"$regex":"^b"}}
newvalue={"$set":{"name":"John David"}}
a=collection.update_many(query,newvalue)
print(a.modified_count,"Your collection to many is updated")