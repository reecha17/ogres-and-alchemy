-- TABLE ENTRY

-- Users Table
CREATE OR REPLACE TABLE Users (
  `userID` INT NOT NULL AUTO_INCREMENT,
  `email` VARCHAR(145) NOT NULL,
  `userName` VARCHAR(25) NOT NULL,
  PRIMARY KEY (`userID`));

-- Servers Table
CREATE OR REPLACE TABLE Servers (
  `serverID` INT NOT NULL AUTO_INCREMENT,
  `location` VARCHAR(25) NOT NULL,
  PRIMARY KEY (`serverID`));

-- Classes Table
CREATE OR REPLACE TABLE Classes (
  `classID` INT NOT NULL AUTO_INCREMENT,
  `className` VARCHAR(16) NOT NULL,
  PRIMARY KEY (`classID`));
  
  -- Factions Table
CREATE OR REPLACE TABLE Factions (
  `factionID` INT NOT NULL AUTO_INCREMENT,
  `factionName` VARCHAR(16) NOT NULL,
  PRIMARY KEY (`factionID`));

-- Characters Table
CREATE OR REPLACE TABLE Characters (
  `characterID` INT NOT NULL AUTO_INCREMENT,
  `characterName` VARCHAR(16) NOT NULL,
  `level` INT NOT NULL DEFAULT 1,
  `userID` INT NOT NULL,
  `serverID` INT NOT NULL,
  `classID` INT NOT NULL,
  `factionID` INT,
  PRIMARY KEY (`characterID`, `userID`, `serverID`, `classID`),
  INDEX `fk_userID_idx` (`userID` ASC) VISIBLE,
  INDEX `fk_serverID_idx` (`serverID` ASC) VISIBLE,
  INDEX `fk_classID_idx` (`classID` ASC) VISIBLE,
  CONSTRAINT `fk_userID`
    FOREIGN KEY (`userID`)
    REFERENCES `Users` (`userID`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_serverID`
    FOREIGN KEY (`serverID`)
    REFERENCES `Servers` (`serverID`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_factionID`
    FOREIGN KEY (`factionID`)
    REFERENCES `Factions` (`factionID`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_classID`
    FOREIGN KEY (`classID`)
    REFERENCES `Classes` (`classID`)
    ON DELETE CASCADE
    ON UPDATE CASCADE);

-- Weapons Table
CREATE OR REPLACE TABLE Weapons (
  `weaponID` INT NOT NULL AUTO_INCREMENT,
  `weaponName` VARCHAR(50) NOT NULL,
  `damage` INT NOT NULL,
  `hit_pct` INT NOT NULL,
  PRIMARY KEY (`weaponID`));

-- Inventory Table
CREATE OR REPLACE TABLE Inventory (
  `characterID` INT NOT NULL,
  `weaponID` INT NOT NULL,
  PRIMARY KEY (`characterID`, `weaponID`),
  INDEX `fk_weaponID_idx` (`weaponID` ASC) VISIBLE,
  INDEX `fk_characterID_idx` (`characterID` ASC) VISIBLE,
  CONSTRAINT `fk_characterID`
    FOREIGN KEY (`characterID`)
    REFERENCES `Characters` (`characterID`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_weaponID`
    FOREIGN KEY (`weaponID`)
    REFERENCES `Weapons` (`weaponID`)
    ON DELETE CASCADE
    ON UPDATE CASCADE);

-- DATA ENTRY

INSERT INTO Users (email, userName)
VALUES ('joe12@aol.com','joecool'),
('bill64@hotmail.com','bill_dance'),
('tim2005@gmail.com','timturner'),
('abi@icloud.com','abigail17'),
('pat62@yahoo.com','patstar');

INSERT INTO Classes (className)
VALUES ('Warrior'),
('Paladin'),
('Mage'),
('Priest'),
('Druid');

INSERT INTO Weapons (weaponName, damage, hit_pct)
VALUES ('Kang the Destroyer', 100, 75),
('Bo Staff', 85, 65),
('Excalibur', 150, 50),
('Durendal', 75, 83),
('Morning Star', 62, 100);

INSERT INTO Servers (location)
VALUES ('Bleeding Hollow'),
('Lionheart'),
('Aegwynn');

INSERT INTO Characters (characterName, level, userID, serverID, classID, factionID)
VALUES ('Merlin', 16, 1, 1, 5, null),
('Ivanoff', 15, 2, 2, 1, 1),
('Arthur', 18, 3, 2, 2, 2),
('Gandalf', 21, 2, 2, 3, 1),
('Cristobal', 10, 4, 1, 4, null),
('Ragnar', 9, 5, 1, 1, 1),
('Evander', 17, 4, 3, 1, 2),
('Diante', 14, 5, 3, 2, 2);

INSERT INTO Inventory (characterID, weaponID)
VALUES (1, 2),
(2, 3),
(3, 3),
(4, 2),
(5, 2),
(6, 1),
(7, 4),
(8, 5);

INSERT INTO Factions (factionID, factionName)
VALUES
(1, 'Nuggets'),
(2, 'Heat'),
(3, 'BTS Army');