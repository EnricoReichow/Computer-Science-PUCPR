DROP DATABASE IF EXISTS pizzaria;

CREATE DATABASE IF NOT EXISTS pizzaria;

USE pizzaria;

DROP TABLE IF EXISTS person;
DROP TABLE IF EXISTS restaurant_table;
DROP TABLE IF EXISTS menu;
DROP TABLE IF EXISTS supplier;
DROP TABLE IF EXISTS customer;
DROP TABLE IF EXISTS reserves;
DROP TABLE IF EXISTS employee;
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS pizzas;
DROP TABLE IF EXISTS restaurant_transactions;

CREATE TABLE IF NOT EXISTS person (
	cpf CHAR(11) NOT NULL UNIQUE,
	person_name VARCHAR(256) NOT NULL,
    email VARCHAR(45) NOT NULL UNIQUE,
    phone_number VARCHAR(20) NOT NULL,
    PRIMARY KEY (cpf)
);

CREATE TABLE IF NOT EXISTS restaurant_table (
	table_number INT UNSIGNED NOT NULL,
    size INT UNSIGNED NOT NULL,
    reserved BOOLEAN NOT NULL,
    occupied BOOLEAN NOT NULL,
    PRIMARY KEY(table_number)
);

CREATE TABLE IF NOT EXISTS menu (
	flavor VARCHAR(20) NOT NULL,
    flavor_value FLOAT UNSIGNED NOT NULL,
	PRIMARY KEY (flavor)
);

CREATE TABLE IF NOT EXISTS supplier (
	ID INT UNIQUE NOT NULL AUTO_INCREMENT,
    supplier_name VARCHAR(45) NOT NULL,
    email VARCHAR(45) NOT NULL,
    phone VARCHAR(20) NOT NULL,
    address VARCHAR(90) NOT NULL,
    supplier_description VARCHAR(255) NOT NULL,
    PRIMARY KEY (ID)
);

CREATE TABLE IF NOT EXISTS customer (
	reg_date DATETIME NOT NULL,
    qntd_pedidos INT UNSIGNED NOT NULL,
    cpf CHAR(11) NOT NULL,
    PRIMARY KEY(cpf),
    FOREIGN KEY (cpf) REFERENCES person(cpf)
);

CREATE TABLE IF NOT EXISTS reserves (
	reserve_name VARCHAR(255) NOT NULL,
    reserve_date DATETIME NOT NULL,
    customer_person_cpf CHAR(11) NOT NULL,
    restaurant_table_num INT UNSIGNED NOT NULL,
    restaurant_table_size INT UNSIGNED NOT NULL,
    PRIMARY KEY(customer_person_cpf),
    FOREIGN KEY (customer_person_cpf) REFERENCES customer(cpf),
    FOREIGN KEY (restaurant_table_num) REFERENCES restaurant_table(table_number)
);

CREATE TABLE IF NOT EXISTS employee (
	employee_role VARCHAR(45) NOT NULL,
    bank_agency VARCHAR(4) NOT NULL,
    bank_num VARCHAR(11) NOT NULL,
    salary FLOAT UNSIGNED NOT NULL,
    workload INT UNSIGNED NOT NULL,
    last_payment DATE,
    cpf CHAR(11) NOT NULL,
    PRIMARY KEY(cpf),
    FOREIGN KEY (cpf) REFERENCES person(cpf)
);

CREATE TABLE IF NOT EXISTS orders (
	ID INT UNIQUE NOT NULL AUTO_INCREMENT,
    restaurant_table INT UNSIGNED NOT NULL,
    order_value INT UNSIGNED NOT NULL,
    order_status VARCHAR(15) NOT NULL,
    creted_at DATETIME NOT NULL,
    new_client BOOLEAN NOT NULL,
    customer_cpf CHAR(11) NOT NULL,
    employee_cpf CHAR(11) NOT NULL,
    PRIMARY KEY(id),
    FOREIGN KEY (customer_cpf) REFERENCES customer(cpf),
    FOREIGN KEY (employee_cpf) REFERENCES employee(cpf)
);

CREATE TABLE IF NOT EXISTS pizzas (
	comments VARCHAR(255),
    quantity INT UNSIGNED NOT NULL,
    flavor VARCHAR(20) NOT NULL,
    orders_ID INT NOT NULL,
    FOREIGN KEY (orders_ID) REFERENCES orders(ID)
);

CREATE TABLE IF NOT EXISTS restaurant_transactions (
	transaction_ID INT UNSIGNED UNIQUE NOT NULL,
    entry_exit VARCHAR(10) NOT NULL,
    transaction_descrip VARCHAR(255),
    transaction_date DATETIME NOT NULL,
    payment_methos VARCHAR(45) NOT NULL,
	orders_ID INT,
    supplier_ID INT,
    employee_cpf CHAR(11),
    FOREIGN KEY (orders_ID) REFERENCES orders(ID),
    FOREIGN KEY (supplier_ID) REFERENCES supplier(ID),
    FOREIGN KEY (employee_cpf) REFERENCES employee(cpf)
);
















