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

#Creating and adding new student
draco = {
    "student_id": "1010",
    "first_name": "Draco",
    "last_name": "Malfoy"
}
draco_inserted_id = db.students.insert_one(draco).inserted_id

#Displaying new student added
print("-- INSERT STATEMENTS --")
print(f"Inserted student record into the students collection with document_id {draco_inserted_id}\n")
student = db.students.find_one({"student_id": "1010"})
print("-- DISPLAYING STUDENT TEST DOC --")
print(f"Student ID: {student['student_id']}")
print(f"First Name: {student['first_name']}")
print(f"Last Name: {student['last_name']}")

#Deleting student
result = db.students.delete_one({"student_id": "1010"})

#Displaying entire collection of student records again
docs = db.students.find({})
print("\n-- DISPLAYING STUDENT DOCUMENTS FROM FIND() QUERY --\n")
for doc in docs:
    first = doc['first_name']
    last = doc['last_name']
    student_id = doc['student_id']
    print(f"Student ID: {student_id}")
    print(f"First Name: {first}")
    print(f"Last Name: {last}\n")

#End of program
input("End of program, press any key to exit...")

