from pymongo import MongoClient

url = 'mongodb+srv://admin:admin@cluster0.b4zen.mongodb.net/?retryWrites=true&w=majority'
client = MongoClient(url)
db = client.pytech
print("**************************\n* Pytech Collection List *\n**************************\n")
print(db.list_collection_names())
input("\nPress enter to exit program...")
exit