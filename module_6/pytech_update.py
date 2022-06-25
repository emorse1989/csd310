#Connecting to the database
from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.b4zen.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech

#Listing students in collection
docs = db.students.find({})
print("\n-- DISPLAYING STUDENT DOCUMENTS FROM FIND() QUERY --\n")
for doc in docs:
    first = doc['first_name']
    last = doc['last_name']
    student_id = doc['student_id']
    print(f"Student ID: {student_id}")
    print(f"First Name: {first}")
    print(f"Last Name: {last}\n")

#Editing student name for student_id 1007
result = db.students.update_one({"student_id" : "1007"}, {"$set": {"last_name": "Styles"}})

#Displaying edited student info
print("-- DISPLAYING STUDENT DOCUMENT 1007 --")
query = db.students.find_one({'student_id': '1007'})
print(f"Student ID: {query['student_id']}")
print(f"First Name: {query['first_name']}")
print(f"Last Name: {query['last_name']}\n")

#End of program
input("End of program, press any key to exit...")