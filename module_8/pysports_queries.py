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

# Testing connection and reporting errors
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

# Opening connection to send queries
db = mysql.connector.connect(**config)

# Creating an alias for the cursor command
cursor = db.cursor()

# Query team table data
cursor.execute("SELECT team_id, team_name, mascot FROM team")
teams = cursor.fetchall()

# Format and print queried data
print("-- DISPLAYING TEAM RECORDS --\n")
for team in teams:
    print(f"Team ID: {team[0]}")
    print(f"Team Name: {team[1]}")
    print(f"Team Mascot: {team[2]}\n")

# Query player table data
cursor.execute("SELECT player_id, first_name, last_name FROM player")
players = cursor.fetchall()

#Format and print queried data
print("-- DISPLAYING PLAYER RECORDS --\n")
for player in players:
    print(f"Player ID: {player[0]}")
    print(f"First Name: {player[1]}")
    print(f"Last Name: {player[2]}\n")

input("Press any key to continue...")

# Close connection 
db.close()