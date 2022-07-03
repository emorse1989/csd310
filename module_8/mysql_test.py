# Import mysql commands to connect to server
import mysql.connector
from mysql.connector import errorcode

# Connection settings
config = {
    "user": "pysports_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}

# Attempt to connect to the MySQL server using provided config settings
# Includes error handling
try:
    db = mysql.connector.connect(**config)

    print(f"\nDatabase user {config['user']} connected to MySQL on host {config['host']} with database {config['database']}.")

    input("\n\nPress any key to continue...")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("The specified database does not exist")

    else:
        print(err)

finally:
    db.close()