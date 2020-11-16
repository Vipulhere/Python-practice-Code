'''
import pymongo
conn=pymongo.MongoClient("mongodb://localhost:27017/")
database=conn["Python"]
print(conn.list_database_names())
list=conn.list_database_names()
if "Python" in list:
    print("The database is already exist")'''
import pymongo
from pymongo import MongoClient

conn=MongoClient("localhost",27017)
database=conn["Python1"]
print("Database is created and connected successfully")
