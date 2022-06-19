# Connecting to the database
from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.b4zen.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech

# Function to list all records
def list_students():
    docs = db.students.find({})
    print("\n-- DISPLAYING STUDENT DOCUMENTS FROM FIND() QUERY --\n")
    for doc in docs:
        first = doc['first_name']
        last = doc['last_name']
        student_id = doc['student_id']
        print(f"Student ID: {student_id}")
        print(f"First Name: {first}")
        print(f"Last Name: {last}\n")
        
# Search records by student ID number
def search_by_id():
    query = input("Please enter the student's ID number: ")
    doc = db.students.find_one({'student_id':query})
    print(f"\n-- DISPLAYING STUDENT RECORD FOR ID NUMBER: {query} --\n")
    first = doc['first_name']
    last = doc['last_name']
    student_id = doc['student_id']
    print(f"Student ID: {student_id}")
    print(f"First Name: {first}")
    print(f"Last Name: {last}\n")

# Main Menu
def main():
    print("******************************\n" + 
          "* STUDENT COLLECTION QUERIES *\n" + 
          "******************************\n" +
          "* 1) LIST ALL STUDENTS       *\n" +
          "* 2) SEARCH BY STUDENT ID    *\n" +
          "* 3) EXIT PROGRAM            *\n" +
          "******************************\n")
    choice = input("PLEASE ENTER SELECTION: ")
    if choice == "1":
        list_students()
        main()
    elif choice == "2":
        search_by_id()
        main()
    elif choice == "3":
        exit
    else:
        print("INPUT NOT RECOGNIZED")
        main()

main()


