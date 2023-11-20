DROP DATABASE IF EXISTS hoteL;
CREATE DATABASE IF NOT EXISTS hotel; 

USE hotel;

DROP TABLE IF EXISTS hotel.person;
DROP TABLE IF EXISTS hotel.guest;
DROP TABLE IF EXISTS hotel.carrier;
DROP TABLE IF EXISTS hotel.employee;
DROP TABLE IF EXISTS hotel.hotel;
DROP TABLE IF EXISTS hotel.room;
DROP TABLE IF EXISTS hotel.billing;
DROP TABLE IF EXISTS hotel.reservation;

CREATE TABLE IF NOT EXISTS hotel.person (
	id INT NOT NULL AUTO_INCREMENT,
    person_name VARCHAR(256) NOT NULL,
	cpf CHAR(11) NOT NULL,
    rg VARCHAR(11) NOT NULL,
    birth_date DATE NOT NULL,
    UNIQUE(cpf),
    PRIMARY KEY(id)
);

SELECT * FROM person;

CREATE TABLE IF NOT EXISTS hotel.guest (
	id INT NOT NULL AUTO_INCREMENT,
    created_at DATETIME NOT NULL,
    FOREIGN KEY (id) REFERENCES hotel.person(id)
);

SELECT * FROM hotel.guest;

CREATE TABLE IF NOT EXISTS hotel.carrier (
	id TINYINT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    carrier_name VARCHAR(100) NOT NULL,
    carrier_description VARCHAR(512) 
);

SELECT * FROM hotel.carrier;

CREATE TABLE IF NOT EXISTS hotel.employee (
	id INT NOT NULL PRIMARY KEY,
    pay DECIMAL(10, 2) NOT NULL,
    hourly BOOL NOT NULL DEFAULT FALSE,
    created_at DATETIME NOT NULL,
    carrier_id TINYINT NOT NULL,
    FOREIGN KEY (id) REFERENCES hotel.person(id),
    FOREIGN KEY (carrier_id) REFERENCES hotel.carrier(id)
);

SELECT * FROM hotel.employee;

CREATE TABLE IF NOT EXISTS hotel.hotel(
	id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    hotel_name VARCHAR(100) NOT NULL,
    phone VARCHAR(20) NOT NULL,
    email VARCHAR(45) NOT NULL
);

SELECT * FROM hotel.hotel;

CREATE TABLE IF NOT EXISTS hotel.room (
	room_number SMALLINT NOT NULL,
    capacity TINYINT NOT NULL,
    tv BOOL NOT NULL DEFAULT FALSE,
    air BOOL NOT NULL DEFAULT FALSE,
    price DECIMAL(10, 2) NOT NULL,
    hotel_id INT NOT NULL,
    PRIMARY KEY(room_number, hotel_id),
    FOREIGN KEY (hotel_id) REFERENCES hotel.hotel(id)
);

SELECT * FROM hotel.room;


CREATE TABLE IF NOT EXISTS hotel.billing (
	id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    billing_datetime DATETIME NOT NULL DEFAULT NOW(),
    total_value DECIMAL(10, 2) NOT NULL
);

SELECT * FROM hotel.billing;

CREATE TABLE IF NOT EXISTS hotel.reservation (
	id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    reservation_datetime DATETIME NOT NULL,
    start_date DATETIME NOT NULL, 
    exit_date DATETIME NOT NULL,
    total_value DECIMAL(10, 2),
    guest_id INT NOT NULL,
    employee_id INT NOT NULL,
    billing_id INT,
    FOREIGN KEY (guest_id) REFERENCES hotel.guest(id),
    FOREIGN KEY (employee_id) REFERENCES hotel.employee(id),
    FOREIGN KEY (billing_id) REFERENCES hotel.billing(id)
);

SELECT * FROM hotel.reservation;

ALTER TABLE hotel.person ADD COLUMN phone VARCHAR(15) AFTER person_name;
# ADD TABLE COLUMNS AFTER CREATION