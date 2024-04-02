from pymongo import MongoClient

mongoUri = "mongodb://localhost:27017/notes"
conn = MongoClient(mongoUri)