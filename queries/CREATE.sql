CREATE database kuluars;
use kuluars;

CREATE TABLE restaurants(id mediumint not null auto_increment, 
primary key (id),
name_of_restaurant varchar(255),
description_of_restaurant varchar(1024),
localisation varchar(255));

use kuluars;

CREATE TABLE users(id mediumint not null auto_increment,
primary key(id),
hashed_pwd varchar(255),
email varchar(255) unique
);

use kuluars;

CREATE TABLE reviews (id mediumint not null auto_increment,
 primary key(id),
 stars INT, 
 review VARCHAR(1024),
 restaurant_id mediumint NOT NULL,
 fk_user mediumint NOT NULL, 
 FOREIGN KEY (restaurant_id)
        REFERENCES restaurants(id), 
 FOREIGN KEY(fk_user) REFERENCES users(id));