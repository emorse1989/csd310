#Connecting to the database
from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.b4zen.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech

#Generating student data
harry = {
    "first_name" : "Harry",
    "last_name" : "Potter",
    "student_id" : "1007"
}

ron = {
    "first_name" : "Ronald",
    "last_name" : "Weasley",
    "student_id" : "1008"
}

hermione = {
    "first_name" : "Hermione",
    "last_name" : "Granger",
    "student_id" : "1009"
}

#list for looping purposes
students = [harry, ron, hermione]

print("-- INSERT STATEMENTS --")

#inserts each student and prints name and document ID
for student in students:
    id = db.students.insert_one(student).inserted_id
    print(f"Inserted student record {student['first_name']} {student['last_name']} into the students" +
    f" collection with document id {id}")
