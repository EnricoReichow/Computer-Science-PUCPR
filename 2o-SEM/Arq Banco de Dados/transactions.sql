-- | Fazendo as transactions | --

-- | commit | --

START TRANSACTION;
INSERT INTO pizcaria.person (name, email) VALUES ('João', 'joao@email.com');
INSERT INTO pizcaria.customer (person_id, phone) VALUES (LAST_INSERT_ID(), '123-456-7890');
COMMIT;

START TRANSACTION;
INSERT INTO pizcaria.orders (customer_id, order_date, total_amount) VALUES (1, NOW(), 30.50);
COMMIT;

START TRANSACTION;
INSERT INTO pizcaria.orders (customer_id, order_date, total_amount) VALUES (2, NOW(), 45.75);
COMMIT;

START TRANSACTION;
INSERT INTO pizcaria.person (name, email) VALUES ('Pedro', 'pedro@email.com');
INSERT INTO pizcaria.customer (person_id, phone) VALUES (LAST_INSERT_ID(), '333-222-1111');
COMMIT;

-- | rollback normal | --

START TRANSACTION;
INSERT INTO pizcaria.orders (customer_id, order_date, total_amount) VALUES (1, NOW(), 'Erro'); -- Erro intencional pra usar o rollback aqui
ROLLBACK;

START TRANSACTION;
UPDATE pizcaria.customer SET phone = 'celulinhonovo' WHERE customer_id = 1; -- Erro intencional pra usar o rolbac
ROLLBACK;

START TRANSACTION;
INSERT INTO pizcaria.orders (customer_id, order_date, total_amount) VALUES (2, NOW(), 'Erro'); -- p rollback
ROLLBACK;

START TRANSACTION;
INSERT INTO pizcaria.person (name, email) VALUES ('Lucas', 'lucasFadinhaLinda@email.com');
INSERT INTO pizcaria.customer (person_id, phone) VALUES (LAST_INSERT_ID(), 'Erro'); -- pra usar rollback
ROLLBACK;

-- | rollback com save point | --

START TRANSACTION;
SAVEPOINT sp1;
INSERT INTO pizcaria.person (name, email) VALUES ('Maria', 'maria@example.com');
INSERT INTO pizcaria.customer (person_id, phone) VALUES (LAST_INSERT_ID(), '987-654-3210');
ROLLBACK TO SAVEPOINT sp1;

START TRANSACTION;
SAVEPOINT sp1;
INSERT INTO pizcaria.person (name, email) VALUES ('Carlos', 'carlos@example.com');
INSERT INTO pizcaria.customer (person_id, phone) VALUES (LAST_INSERT_ID(), '111-222-3333');
SAVEPOINT sp2;
INSERT INTO pizcaria.person (name, email) VALUES ('Laura', 'laura@example.com');
INSERT INTO pizcaria.customer (person_id, phone) VALUES (LAST_INSERT_ID(), '444-555-6666');
ROLLBACK TO SAVEPOINT sp1;