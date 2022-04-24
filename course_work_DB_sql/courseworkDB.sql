create database if not exists course_work;

use course_work;

create table if not exists User (
    userID INT NOT NULL auto_increment PRIMARY KEY UNIQUE,
    userName varchar(20) NOT NULL UNIQUE
);

create table if not exists Admin (
    adminID INT NOT NULL auto_increment PRIMARY KEY UNIQUE,
    adminEmail varchar(30) NULL,
    adminName varchar(20) NOT NULL UNIQUE
);

create table if not exists Place (
    placeID INT NOT NULL auto_increment PRIMARY KEY UNIQUE ,
    averageCheck int NULL,
    placeDogFriendly bool NULL ,
    placePhoto varchar(200) NULL,
    placeURL varchar(500) NULL ,
    placeDescription varchar(10000) NULL ,
    placeName varchar(50) NOT NULL UNIQUE ,
    adminID int NULL,
    CONSTRAINT place_admin_fk
    FOREIGN KEY (adminID) REFERENCES Admin (adminID) ON DELETE SET NULL ON UPDATE cascade
);

create table if not exists Favourite (
    userID INT NOT NULL auto_increment,
    placeID INT NOT NULL,
    CONSTRAINT favourite_user_fk
    FOREIGN KEY (userID) REFERENCES User (userID) ON DELETE cascade ON UPDATE cascade,
    CONSTRAINT favourite_place_fk
    FOREIGN KEY (placeID) REFERENCES Place (placeID) ON DELETE cascade ON UPDATE cascade,
    PRIMARY KEY (userID, placeID)
);

create table if not exists Cuisine (
    cuisineID INT NOT NULL auto_increment UNIQUE ,
    cuisineName varchar(50) NOT NULL UNIQUE
#     CHECK (cuisineName = 'итальянская' or cuisineName = 'завтраки' or cuisineName = 'перекусы'
#         or cuisineName = 'кофе' or cuisineName = 'американская' or cuisineName = 'корейская'
#         or cuisineName = 'азиатская' or cuisineName = 'многопрофильное заведение'
#         or cuisineName = 'европейская' or cuisineName = 'мексиканская' or cuisineName = 'коктейли'
#         or cuisineName = 'грузинская' or cuisineName = 'авторская' or cuisineName = 'кондитерская'
#         or cuisineName = 'чай' or cuisineName = 'спешелти' or cuisineName = 'китайская'
#         or cuisineName = 'японская' or cuisineName = 'смешанная' or cuisineName = 'вьетнамская'
#         or cuisineName = 'тайская' or cuisineName = 'паназиатская' or cuisineName = 'средиземноморская'
#         or cuisineName = 'фьюжн' or cuisineName = 'морская')
);

create table if not exists Metro (
    metroID INT NOT NULL auto_increment UNIQUE ,
    metroName varchar(50) NOT NULL UNIQUE
);

create table if not exists Address (
    addressID INT NOT NULL auto_increment UNIQUE ,
    addressName varchar(200) NOT NULL UNIQUE
);

create table if not exists Atmosphere (
    atmosphereID INT NOT NULL auto_increment UNIQUE ,
    atmosphereName varchar(100) NOT NULL UNIQUE
);

create table if not exists Leisure (
    leisureID INT NOT NULL auto_increment UNIQUE ,
    leisureName varchar(100) NOT NULL UNIQUE
);

create table if not exists Fit (
    fitID INT NOT NULL auto_increment UNIQUE ,
    fitName varchar(100) NOT NULL UNIQUE
);

create table if not exists Format (
    formatID INT NOT NULL auto_increment UNIQUE ,
    formatName varchar(50) NOT NULL UNIQUE
);

create table if not exists PlaceCuisines (
    cuisineID int NOT NULL,
    placeID int NOT NULL ,
    CONSTRAINT place_cuisines_place_fk
    FOREIGN KEY (placeID) REFERENCES Place (placeID) ON DELETE cascade ON UPDATE cascade,
    CONSTRAINT place_cuisines_cuisine_fk
    FOREIGN KEY (cuisineID) REFERENCES Cuisine (cuisineID) ON DELETE cascade ON UPDATE cascade,
    PRIMARY KEY (cuisineID, placeID)
);

create table if not exists PlaceMetros (
    metroID int NOT NULL,
    placeID int NOT NULL ,
    CONSTRAINT place_metros_place_fk
    FOREIGN KEY (placeID) REFERENCES Place (placeID) ON DELETE cascade ON UPDATE cascade,
    CONSTRAINT place_metros_metro_fk
    FOREIGN KEY (metroID) REFERENCES Metro (metroID) ON DELETE cascade ON UPDATE cascade,
    PRIMARY KEY (metroID, placeID)
);

create table if not exists PlaceAddresses (
    addressID int NOT NULL,
    placeID int NOT NULL ,
    CONSTRAINT place_addresses_place_fk
    FOREIGN KEY (placeID) REFERENCES Place (placeID) ON DELETE cascade ON UPDATE cascade,
    CONSTRAINT place_addresses_address_fk
    FOREIGN KEY (addressID) REFERENCES Address (addressID) ON DELETE cascade ON UPDATE cascade,
    PRIMARY KEY (addressID, placeID)
);

create table if not exists PlaceAtmospheres (
    atmosphereID int NOT NULL,
    placeID int NOT NULL ,
    CONSTRAINT place_atmospheres_place_fk
    FOREIGN KEY (placeID) REFERENCES Place (placeID) ON DELETE cascade ON UPDATE cascade,
    CONSTRAINT place_atmospheres_atmosphere_fk
    FOREIGN KEY (atmosphereID) REFERENCES Atmosphere (atmosphereID) ON DELETE cascade ON UPDATE cascade,
    PRIMARY KEY (atmosphereID, placeID)
);

create table if not exists PlaceLeisures (
    leisureID int NOT NULL,
    placeID int NOT NULL ,
    CONSTRAINT place_leisures_place_fk
    FOREIGN KEY (placeID) REFERENCES Place (placeID) ON DELETE cascade ON UPDATE cascade,
    CONSTRAINT place_leisures_leisure_fk
    FOREIGN KEY (leisureID) REFERENCES Leisure (leisureID) ON DELETE cascade ON UPDATE cascade,
    PRIMARY KEY (leisureID, placeID)
);

create table if not exists PlaceFits (
    fitID int NOT NULL,
    placeID int NOT NULL ,
    CONSTRAINT place_fits_place_fk
    FOREIGN KEY (placeID) REFERENCES Place (placeID) ON DELETE cascade ON UPDATE cascade,
    CONSTRAINT place_fits_fit_fk
    FOREIGN KEY (fitID) REFERENCES Fit (fitID) ON DELETE cascade ON UPDATE cascade,
    PRIMARY KEY (fitID, placeID)
);

create table if not exists PlaceFormats (
    formatID int NOT NULL,
    placeID int NOT NULL ,
    CONSTRAINT place_format_place_fk
    FOREIGN KEY (placeID) REFERENCES Place (placeID) ON DELETE cascade ON UPDATE cascade,
    CONSTRAINT place_format_format_fk
    FOREIGN KEY (formatID) REFERENCES Format (formatID) ON DELETE cascade ON UPDATE cascade,
    PRIMARY KEY (formatID, placeID)
);

INSERT INTO User (userID, userName) VALUES (UUID_TO_BIN(UUID()), 'sluolp');

SELECT COUNT(userID) FROM User WHERE userName = 'sluolp';

DELETE FROM User where userName = 'sluolp';
DELETE FROM Admin where adminName = 'sluolp';
DELETE FROM Place where true;
DELETE FROM Address where true;
DELETE FROM PlaceAddresses where true;
DELETE FROM Metro where true;
DELETE FROM PlaceMetros where true;
DELETE FROM User where userName = 'shulpina_al';
DELETE FROM Admin where adminName = 'shulpina_al';

UPDATE Admin SET adminEmail = 'xui' WHERE adminName = 'sluolp';

INSERT INTO Place (placeID, adminID) VALUES (UUID_TO_BIN(UUID()), (SELECT adminID FROM Admin WHERE adminName = 'sluolp'));

Update Place set placeDogFriendly = true WHERE placeName = 'xui';

SELECT DISTINCT metroName FROM Metro ORDER BY metroName