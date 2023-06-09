from pymongo import MongoClient

# mongodb://localhost:27017/

def get_db_handle():
    db_name = 'ecommerce-mongo'
    port = 27017
    client = MongoClient(host='localhost', port=port)
    db_handle = client[db_name]
    return db_handle, client