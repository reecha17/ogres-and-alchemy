-- These are the Database Manipulation queries for a partially implemented Project Website
-- using the oanda database. 

-- get all Server IDS and names to populate servers page
SELECT * from Servers; 

-- get all Characters to populate a Characters page
SELECT * from Characters; 

-- get all Useres to populate a Users page
SELECT * from Users; 

-- get all Classes to populate a Classes page
SELECT * from Classes; 

-- get all Weapons to populate a Characters page
SELECT * from Weapons; 

-- add a new user
INSERT INTO Users (email, userName) VALUES (:emailInput, :userNameInput);

-- update a user
UPDATE Users 
SET email = :emailInput, userName = :userNameInput 
WHERE userID = :userIDInput;

-- delete a user
DELETE FROM Users WHERE userID = :userIDInput;

-- add a new server
INSERT INTO Servers (location) VALUES (:locationInput);

-- update a server name
UPDATE Servers 
SET location = :locationInput 
WHERE serverID = :serverIDInput;

-- delete a server
DELETE FROM Servers WHERE serverID = :serverIDInput;

-- add a new character
INSERT INTO Characters (characterName, level, userID, serverID, classID)
VALUES (:characterNameInput, :levelInput, :UserIDInput, :ServerIDInput, :classIDInput);

-- update a character
UPDATE Characters 
SET characterName = :characterNameInput, level = :levelInput, userID = :userIDInput, serverID = :serverIDInput, classID = :classIDInput 
WHERE characterID = :characterIDInput; 

-- delete a character
DELETE FROM Characters WHERE characterID = :characterIDInput;

-- add a new weapon
INSERT INTO Weapons (weaponName, dmg, hit_pct)
VALUES (:weaponNameInput, :dmgInput, :hit_pctInput);

-- update a weapon
UPDATE Weapons 
SET weaponName = :weaponNameInput, dmg = :dmgInput, hit_pct = :hit_pctInput
WHERE weaponID = :weaponIDInput; 

-- delete a weapon
DELETE FROM Weapons WHERE weaponID = :weaponIDInput;

-- add a new weapon to character's inventory
INSERT INTO Inventory (characterID, weaponID) 
VALUES (:characterIDInput, :weaponIDInput);

-- view a characters inventory
SELECT * FROM Inventory 
INNER JOIN Weapons on Inventory.weaponID = Weapons.weaponID
WHERE characterID = 2;

-- delete a weapon from inventory
DELETE FROM Inventory WHERE characterID = :characterIDInput AND weaponID = :weaponIDInput;

-- add a new class 
INSERT INTO Classes (className)
VALUES (:classNameInput)

-- update a class name
UPDATE Classes 
SET classname = :classNameInput
WHERE classID = :classIDInput;

-- view a user's characters
SELECT * FROM Characters 
INNER JOIN Users on Characters.userID = Users.userID
WHERE userID = :userIDInput;