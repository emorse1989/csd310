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

# Create join and list function to avoid code repetition
def PlayerList():
    cursor.execute(
    "SELECT  player_id, first_name, last_name, team_name " +
    "FROM player " +
    "INNER JOIN team " +
    "ON player.team_id=team.team_id;"
    )
    players = cursor.fetchall()
    for player in players:
        print(f"Player ID: {player[0]}")
        print(f"First Name: {player[1]}")
        print(f"Last Name: {player[2]}")
        print(f"Team Name: {player[3]}\n")

# Insert new player into the player table and display results
cursor.execute(
    "INSERT INTO player (player_id, first_name, last_name, team_id) " +
    "VALUES(7, 'Smeagol', 'Shire Folk', 1);"
)
print("-- DISPLAYING PLAYERS AFTER INSERT --\n")
PlayerList()

# Update added player and display results
cursor.execute(
    "UPDATE player " +
    "SET team_id = 2, first_name = 'Gollum', last_name = 'Ring Stealer' " +
    "WHERE first_name = 'Smeagol';"
)
print("-- DISPLAYING PLAYERS AFTER UPDATE --\n")
PlayerList()

# Delete added player and display results
cursor.execute(
    "DELETE FROM player WHERE first_name = 'Gollum';"
)
print("-- DISPLAYING PLAYERS AFTER DELETE --\n")
PlayerList()

# All done
db.close()
input("Press any key to continue...")