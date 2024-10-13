from flask import Flask, render_template, redirect, url_for, request
import os
import database.db_connector as db

app = Flask(__name__)
app.config['SECRET_KEY'] = 'my_secret'
db_connection = db.connect_to_database()

# Get functions
def get_users(): 
    query = "SELECT * FROM Users;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    return cursor.fetchall()

def get_servers():
    query = "SELECT * FROM Servers;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    return cursor.fetchall()

def get_classes():
    query = "SELECT * FROM Classes;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    return cursor.fetchall()

def get_factions():
    query = "SELECT * FROM Factions;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    return cursor.fetchall()

def get_characters():
    query = "SELECT * FROM Characters;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    return cursor.fetchall()

def get_weapons():
    query = "SELECT * FROM Weapons;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    return cursor.fetchall()

def get_inventory():
    query = "SELECT * FROM Inventory;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    return cursor.fetchall()

# Routes 
@app.route('/', methods=['GET'])
def index():
    return render_template("main.html")

# Users
@app.route('/users', methods=['GET','POST'])
def users():
    users = get_users()
    return render_template("users.html", users=users)

@app.route('/create_user', methods=['POST'])
def create_user():
    query = f"INSERT INTO Users (email, userName) VALUES ('{str(request.form['email'])}', '{str(request.form['userName'])}');"
    db.execute_query(db_connection=db_connection, query=query)
    return redirect(url_for("users"))

@app.route('/edit_user/<int:id>', methods=['GET'])
def edit_user(id):
    users = get_users()
    userInfo = [user for user in users if user['userID'] == id][0]
    return render_template("edit_user.html", id=id, userInfo=userInfo)

@app.route('/update_user', methods=['POST'])
def update_user():
    query = f"UPDATE Users SET userName = '{str(request.form['userName'])}', email = '{str(request.form['email'])}' WHERE userID = {str(request.form['userID'])};"
    db.execute_query(db_connection=db_connection, query=query)
    return redirect(url_for("users"))

@app.route('/delete_user/<int:id>', methods=['GET'])
def delete_user(id):
    query = "DELETE FROM Users WHERE userID = " + str(id) + ";"
    db.execute_query(db_connection=db_connection, query=query)
    return redirect(url_for("users"))

# Servers
@app.route('/servers', methods=['GET'])
def servers():
    servers = get_servers()
    return render_template("servers.html", servers=servers)

@app.route('/create_server', methods=['POST'])
def create_server():
    query = f"INSERT INTO Servers (location) VALUES ('{str(request.form['location'])}');"
    db.execute_query(db_connection=db_connection, query=query)
    return redirect(url_for("servers"))

@app.route('/edit_server/<int:id>', methods=['GET'])
def edit_server(id):
    servers = get_servers()
    serverInfo = [server for server in servers if server['serverID'] == id][0]
    return render_template("edit_server.html", id=id, serverInfo=serverInfo)

@app.route('/update_server', methods=['POST'])
def update_server():
    query = f"UPDATE Servers SET location = '{str(request.form['location'])}' WHERE serverID = {str(request.form['serverID'])};"
    db.execute_query(db_connection=db_connection, query=query)
    return redirect(url_for("servers"))

@app.route('/delete_server/<int:id>', methods=['GET'])
def delete_server(id):
    query = "DELETE FROM Servers WHERE serverID = " + str(id) + ";"
    db.execute_query(db_connection=db_connection, query=query)
    return redirect(url_for("servers"))

# Weapons
@app.route('/weapons', methods=['GET'])
def weapons():
    weapons = get_weapons()
    return render_template("weapons.html", weapons=weapons)

@app.route('/create_weapon', methods=['POST'])
def create_weapon():
    query = f"INSERT INTO Weapons (weaponName, damage, hit_pct) VALUES ('{str(request.form['weaponName'])}', {str(request.form['damage'])}, {str(request.form['hit_pct'])});"
    db.execute_query(db_connection=db_connection, query=query)
    return redirect(url_for("weapons"))

@app.route('/edit_weapon/<int:id>', methods=['GET'])
def edit_weapon(id):
    weapons = get_weapons()
    weaponInfo = [weapon for weapon in weapons if weapon['weaponID'] == id][0]
    return render_template("edit_weapon.html", id=id, weaponInfo=weaponInfo)

@app.route('/update_weapon', methods=['POST'])
def update_weapon():
    query = f"UPDATE Weapons SET weaponName = '{str(request.form['weaponName'])}', damage = {str(request.form['damage'])}, hit_pct = {str(request.form['hit_pct'])} WHERE weaponID = {str(request.form['weaponID'])};"
    db.execute_query(db_connection=db_connection, query=query)
    return redirect(url_for("weapons"))

@app.route('/delete_weapon/<int:id>', methods=['GET'])
def delete_weapon(id):
    query = "DELETE FROM Weapons WHERE weaponID = " + str(id) + ";"
    db.execute_query(db_connection=db_connection, query=query)
    return redirect(url_for("weapons"))

# Classes
@app.route('/classes', methods=['GET'])
def classes():    
    classes = get_classes()
    return render_template("classes.html", classes=classes)

@app.route('/create_class', methods=['POST'])
def create_class():
    query = f"INSERT INTO Classes (className) VALUES ('{str(request.form['className'])}');"
    db.execute_query(db_connection=db_connection, query=query)
    return redirect(url_for("classes"))

@app.route('/edit_class/<int:id>', methods=['GET'])
def edit_class(id):
    classes = get_classes()
    classInfo = [characterClass for characterClass in classes if characterClass['classID'] == id][0]
    return render_template("edit_class.html", classes=classes, classInfo=classInfo)

@app.route('/update_class', methods=['POST'])
def update_class():
    query = f"UPDATE Classes SET className = '{str(request.form['className'])}' WHERE classID = {str(request.form['classID'])};"
    db.execute_query(db_connection=db_connection, query=query)
    return redirect(url_for("classes"))

@app.route('/delete_class/<int:id>', methods=['GET'])
def delete_class(id):
    query = "DELETE FROM Classes WHERE classID = " + str(id) + ";"
    db.execute_query(db_connection=db_connection, query=query)
    return redirect(url_for("classes"))

# Characters
@app.route('/characters', methods=['GET'])
def characters():
    characters = get_characters()
    users = get_users()
    servers = get_servers()
    classes = get_classes()
    factions = get_factions()
    return render_template("characters.html", characters=characters, users=users, servers=servers, classes=classes, factions=factions)

@app.route('/characters/<int:id>', methods=['GET'])
def character_page(id):
    characters = get_characters()
    weapons = get_weapons()
    inventory = get_inventory()
    users = get_users()
    servers = get_servers()
    classes = get_classes()
    factions = get_factions()
    characterInfo = [character for character in characters if character['characterID'] == id][0]
    return render_template("character_page.html", inventory=inventory, characterInfo=characterInfo, weapons=weapons, users=users, servers=servers, classes=classes, factions=factions)

@app.route('/create_character', methods=['POST'])
def create_character():
    query = f"INSERT INTO Characters (characterName, level, userID, serverID, classID, factionID) VALUES ('{str(request.form['characterName'])}', {str(request.form['level'])}, {str(request.form['userID'])}, {str(request.form['serverID'])}, {str(request.form['classID'])}, {str(request.form['factionID'])});"
    db.execute_query(db_connection=db_connection, query=query)
    return redirect(url_for("characters"))

@app.route('/update_character', methods=['POST'])
def update_character():
    query = f"UPDATE Characters SET characterName = '{str(request.form['characterName'])}', level = '{str(request.form['level'])}', userID = '{str(request.form['userID'])}', serverID = '{str(request.form['serverID'])}', classID = '{str(request.form['classID'])}', factionID = {str(request.form['factionID'])} WHERE characterID = {str(request.form['characterID'])};"
    db.execute_query(db_connection=db_connection, query=query)
    return redirect(url_for("characters"))

@app.route('/edit_character/<int:id>', methods=['GET'])
def edit_character(id):
    characters = get_characters()
    users = get_users()
    servers = get_servers()
    classes = get_classes()
    factions = get_factions()
    characterInfo = [character for character in characters if character['characterID'] == id][0]
    return render_template("edit_character.html", id=id, characters=characters, characterInfo=characterInfo, users=users, servers=servers, classes=classes, factions=factions)

@app.route('/delete_character/<int:id>', methods=['GET'])
def delete_character(id):
    query = "DELETE FROM Characters WHERE characterID = " + str(id) + ";"
    db.execute_query(db_connection=db_connection, query=query)
    return redirect(url_for("characters"))

@app.route('/search_characters', methods=['POST'])
def search_characters():
    query = f"SELECT characterID FROM Characters WHERE characterName = '{str(request.form['search_term'])}';"
    try:
        results = db.execute_query(db_connection=db_connection, query=query).fetchall()
        id = results[0]['characterID']
        return redirect(url_for("characters") + "/" + str(id))
    except:
        print('No Character Found.')
    
# Inventory
@app.route('/inventory', methods=['GET','POST'])
def inventory():
    inventory = get_inventory()
    weapons = get_weapons()
    characters = get_characters()
    return render_template("inventory.html", inventory=inventory, weapons=weapons, characters=characters)

@app.route('/create_inventory', methods=['POST'])
def create_inventory():
    query = f"INSERT INTO Inventory (characterID, weaponID) VALUES ({str(request.form['characterID'])}, {str(request.form['weaponID'])});"
    try: 
        db.execute_query(db_connection=db_connection, query=query)
    except: 
        print(f'Duplicate entry: {query}')
    return redirect(url_for("inventory"))

@app.route('/delete_inventory', methods=['GET'])
def delete_inventory():
    characterID = request.args.get('characterID', None)
    weaponID = request.args.get('weaponID', None)
    if characterID and weaponID: 
        query = "DELETE FROM Inventory WHERE characterID = " + str(characterID) + " and weaponID = " + str(weaponID) + ";"
        db.execute_query(db_connection=db_connection, query=query)
    return redirect(url_for("inventory"))

# Factions
@app.route('/factions', methods=['GET','POST'])
def factions():
    factions = get_factions()
    return render_template("factions.html", factions=factions)

@app.route('/create_faction', methods=['POST'])
def create_faction():
    query = f"INSERT INTO Factions (factionName) VALUES ('{str(request.form['factionName'])}');"
    db.execute_query(db_connection=db_connection, query=query)
    return redirect(url_for("factions"))

@app.route('/edit_faction/<int:id>', methods=['GET'])
def edit_faction(id):
    factions = get_factions()
    factionInfo = [faction for faction in factions if faction['factionID'] == id][0]
    return render_template("edit_faction.html", factions=factions, factionInfo=factionInfo)

@app.route('/update_faction', methods=['POST'])
def update_faction():
    query = f"UPDATE Factions SET factionName = '{str(request.form['factionName'])}' WHERE factionID = {str(request.form['factionID'])};"
    db.execute_query(db_connection=db_connection, query=query)
    return redirect(url_for("factions"))

@app.route('/delete_faction/<int:id>', methods=['GET'])
def delete_faction(id):
    query = "DELETE FROM Factions WHERE factionID = " + str(id) + ";"
    db.execute_query(db_connection=db_connection, query=query)
    return redirect(url_for("factions"))

# Listener
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 9113))
    app.run(port=port, debug=True)
