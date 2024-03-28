import pymongo

def show_users():
    # Connect to MongoDB
    client = pymongo.MongoClient("mongodb://localhost:27017")
    db = client["prity"]  
    collection = db["users"]

    # Retrieve all documents from  "users" collection
    for user in collection.find():
        print(user)

    # Close  MongoDB connection
    client.close()

if __name__ == "__main__":
    show_users()
