from pymongo import MongoClient

def get_database():
 
   CONNECTION_STRING = "mongodb://atlas-sql-66ae7d91c1322b1c6a52f9a1-3mudn.a.query.mongodb.net/sample_mflix?ssl=true&authSource=admin"
 
   client = MongoClient(CONNECTION_STRING)
 
   return client['sample_mflix']