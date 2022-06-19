#Connecting to the database
from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.b4zen.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech

# Collects inputs and generates a student document
def main():
    print("##########################\n# STUDENT DATA COLLECTOR #\n##########################")
    first = input("Enter student's first name: ")
    last = input("Enter student's last name: ")
    number = str(input("Enter student's ID number: "))
    new_student = {
        "first_name" : first,
        "last_name" : last,
        "student_id" : number
        }

    #inserts the new student and prints name and document ID
    id = db.students.insert_one(new_student).inserted_id
    print(f"Inserted student record {new_student['first_name']} {new_student['last_name']} into the " +
    f"students collection with document id {id}")

    choice = input("Add additional students? (Y/N): ")
    if choice == "Y" or choice == "y" or choice == "yes" or choice == "Yes":
        main()
    else:
        exit

main()