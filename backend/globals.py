from pymongo import MongoClient

mongo = MongoClient("mongodb://tester:tester@ds135519.mlab.com:35519/aliere_prod")
db = mongo.aliere_prod
