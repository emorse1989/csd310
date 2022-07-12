# Import mysql commands to connect to server
import mysql.connector

# Connection settings
config = {
    "user": "pysports_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}

# Opening connection to send queries
db = mysql.connector.connect(**config)

# Creating an alias for the cursor command
cursor = db.cursor()

# Sending INNER JOIN request to server
cursor.execute(
    "SELECT  player_id, first_name, last_name, team_name " +
    "FROM player " +
    "INNER JOIN team " +
    "ON player.team_id=team.team_id;"
)

# Format and print join results
inner_joins = cursor.fetchall()
print("-- DISPLAYING PLAYER RECORDS --\n")
for inner_join in inner_joins:
    print(f"Player ID: {inner_join[0]}")
    print(f"First Name: {inner_join[1]}")
    print(f"Last Name: {inner_join[2]}")
    print(f"Team Name: {inner_join[3]}\n")

# All done
db.close()
input("Press any key to continue...")