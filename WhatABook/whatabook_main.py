# Import mysql commands to connect to server
import mysql.connector
from time import sleep

# Connection settings
config = {
    "user": "whatabook_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "whatabook",
    "raise_on_warnings": True
}

# Opening connection to send queries
db = mysql.connector.connect(**config)

# Creating a global variable for the SQL cursor command
cursor = db.cursor()

# Main Menu UI 
def main_menu():
    print("*******************************")
    print("* -- What A Book Main Menu -- *")
    print("*******************************")
    print("* 1) View Available Books     *")
    print("* 2) View Store Locations     *")
    print("* 3) My Account               *")
    print("* 4) Exit Program             *")
    print("*******************************")
    main_choose_option()
    main_menu()

# Selects a Menu option - reruns menu if invalid input
def main_choose_option():
    choice = input("\nPlease select an option (1-4): ")
    if choice == '1':
        list_books()
    elif choice == '2':
        list_locations()
    elif choice == '3':
        validate_user()
    elif choice == '4':
        input("\nThank you for using What A Book! Press enter to exit.")
        db.close()
        exit()    
    else:
        print("\nInput not recognized. Please try again.\n")
        sleep(1)

# Retrieves book list and cycles through books
def list_books():
    cursor.execute(
        "SELECT * FROM book;"
    )
    books = cursor.fetchall()
    print(" -- DISPLAYING AVAILABLE BOOKS --\n")
    for book in books:
        print(f"Book ID: {book[0]}")
        print(f"Book Name: {book[1]}")
        print(f"Book Author: {book[3]}")
        print(f"Book Description: {book[2]}")
        input("\nPress enter to continue.\n")
    input("List complete. Press enter to return to main menu.\n")

# Lists store locations
def list_locations():
    cursor.execute(
        "SELECT * FROM store;"
    )
    locations = cursor.fetchall()
    print(" -- DISPLAYING STORE LOCATIONS --\n")
    for location in locations:
        print(f"Store ID: {location[0]}")
        print(f"Store Address: {location[1]}\n")
    input("Press enter to return to main menu.\n")

# Requests and validates user id, then loads menu
def validate_user():
    cursor.execute(
        "SELECT user_id FROM user;"
    )
    id_list = str(cursor.fetchall())
    user_id = input("\nPlease enter your user ID number: ")
    if user_id in id_list:
        cursor.execute(
            f"SELECT first_name, last_name FROM user WHERE user_id = {user_id};"
        )
        name = cursor.fetchall()
        print(f"\nWelcome back {name[0][0]} {name[0][1]}!\n")
        sleep(1)
        user_menu(user_id)
    else:
        print("User Not Found. Returning to main menu.")
        sleep(1)
        main_menu()

# Displays user menu
def user_menu(user_id):
    print("***************************")
    print("* -- USER ACCOUNT MENU -- *")
    print("***************************")
    print("* 1) View Wishlist        *")
    print("* 2) Add Book to Wishlist *")
    print("* 3) Return to Main Menu  *")
    print("***************************")
    user_choose_option(user_id)

# Accepts and interprets user menu inputs
def user_choose_option(user_id):
    choice = input("\nPlease select an option (1-3): ")
    if choice == "1":
        wishlist(user_id)
        user_menu(user_id)
    elif choice == "2":
        books_not_in_wishlist(user_id)
    elif choice == "3":
        main_menu()
    else:
        print("Input not recognized. Please try again.")
        sleep(1)
        user_menu(user_id)

# Displays the user's wishlist items
def wishlist(user_id):
    cursor.execute(
        "SELECT user.first_name, user.last_name, book.book_id, book.book_name, book.author, " +
        "book.details FROM((wishlist INNER JOIN user ON wishlist.user_id = user.user_id) " +
        f"INNER JOIN book ON wishlist.book_id = book.book_id) WHERE user.user_id = {user_id};"
    )
    wishes = cursor.fetchall()
    print(f"\n -- {wishes[0][0]} {wishes[0][1]}'s Wishlist -- \n")
    for wish in wishes:
        print(f"Book ID: {wish[2]}")
        print(f"Book Name: {wish[3]}")
        print(f"Book Author: {wish[4]}")
        print(f"Book Description: {wish[5]}")
        input("\nPress enter to continue.\n")
    input("List complete. Press enter to return to user menu.\n")

# Takes parameters from books_not_in_wishlist and adds new row to wishlist table
def add_book_to_wishlist(user_id, book_id):
    cursor.execute(
        "INSERT INTO wishlist (user_id, book_id) " +
        f"VALUES ({user_id}, {book_id});"
    )
    cursor.execute("COMMIT;")   
    cursor.execute(
        f"SELECT book_name FROM book WHERE book_id = {book_id};"
    )
    book = cursor.fetchone()
    print(f"\nAdded {book[0]} to your wishlist!\n")
    user_menu(user_id)

# Lists books to add to wishlist, then has user pick a book
def books_not_in_wishlist(user_id):
    cursor.execute(
        "SELECT * FROM book " 
        f"WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = {user_id});"
        )
    books = cursor.fetchall()
    print("\n -- BOOKS NOT IN WISHLIST -- \n")
    for book in books:
        print(f"Book ID: {book[0]}")
        print(f"Book Name: {book[1]}")
        print(f"Book Author: {book[3]}")
        print(f"Book Description: {book[2]}")
        input("\nPress enter to continue.\n")
    book_id = input("Please enter the book ID of the book you want to add to your wishlist: ")
    for book in books:
        if book_id == str(book[0]):
            add_book_to_wishlist(user_id, book_id)
    print("Book ID Not Found. Returning to user menu.")
    sleep(1)
    user_menu(user_id)
   
# Launches the main menu!  
main_menu()