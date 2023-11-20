-- PROCEDURES --
/* 
Procedure para Atualizar o Salário dos Funcionários:
Esta procedure atualiza o salário de todos os funcionários com base em um aumento percentual fornecido como parâmetro.
*/
DELIMITER //
CREATE PROCEDURE UpdateEmployeeSalary(IN percent_increase FLOAT)
BEGIN
    UPDATE employee SET salary = salary * (1 + percent_increase/100);
END;
//
DELIMITER ;

/* 
Procedure para Registrar Reserva:
Esta procedure permite registrar uma reserva no banco de dados.
*/
DELIMITER //
CREATE PROCEDURE RegisterReservation(
    IN reserve_name VARCHAR(255),
    IN reserve_date DATETIME,
    IN customer_cpf CHAR(11),
    IN table_number INT,
    IN table_size INT
)
BEGIN
    INSERT INTO reserves (reserve_name, reserve_date, customer_person_cpf, restaurant_table_num, restaurant_table_size)
    VALUES (reserve_name, reserve_date, customer_cpf, table_number, table_size);
END;
//
DELIMITER ;

/* 
Essa procedure irá listar os nomes e CPFs de todos os funcionários com um salário superior a um valor especificado:
*/
DELIMITER //
CREATE PROCEDURE ListHighSalaryEmployees(IN min_salary FLOAT)
BEGIN
    SELECT person_name, cpf
    FROM person
    WHERE cpf IN (SELECT cpf FROM employee WHERE salary > min_salary);
END;
//
DELIMITER ;

-- FUNÇÕES --
/*
Função para Calcular o Valor Total do Pedido de um Cliente:
*/
DELIMITER //
CREATE FUNCTION CalculateTotalOrderValue(customer_cpf CHAR(11))
RETURNS FLOAT
BEGIN
    DECLARE total_value FLOAT;
    SELECT SUM(order_value) INTO total_value FROM orders WHERE customer_cpf = customer_cpf;
    RETURN total_value;
END;
//
DELIMITER ;

/*
Função para Encontrar o Fornecedor com o Maior Número de Transações:
*/
DELIMITER //
CREATE FUNCTION FindTopSupplier()
RETURNS VARCHAR(45)
BEGIN
    DECLARE top_supplier_name VARCHAR(45);
    SELECT supplier_name INTO top_supplier_name FROM supplier
    WHERE ID = (SELECT supplier_ID FROM restaurant_transactions
                GROUP BY supplier_ID
                ORDER BY COUNT(*) DESC
                LIMIT 1);
    RETURN top_supplier_name;
END;
//
DELIMITER ;

/* 
Função para Verificar a Disponibilidade de uma Mesa:
*/
DELIMITER //
CREATE FUNCTION IsTableAvailable(table_number INT)
RETURNS BOOLEAN
BEGIN
    DECLARE is_available BOOLEAN;
    SELECT NOT occupied INTO is_available FROM restaurant_table WHERE table_number = table_number;
    RETURN is_available;
END;
//
DELIMITER ;

-- TRIGGERS --
/*
Gatilho de Inserção (INSERT Trigger) para Registros de Pedidos:
*/
DELIMITER //
CREATE TRIGGER OrdersInsertTrigger
AFTER INSERT ON orders FOR EACH ROW
BEGIN
    UPDATE customer
    SET qntd_pedidos = qntd_pedidos + 1
    WHERE cpf = NEW.customer_cpf;
END;
//
DELIMITER ;

/*
Gatilho de Atualização (UPDATE Trigger) para Alterar o Status de um Pedido:
*/
DELIMITER //
CREATE TRIGGER OrdersUpdateTrigger
AFTER UPDATE ON orders FOR EACH ROW
BEGIN
    UPDATE orders
    SET last_payment = NOW()
    WHERE ID = NEW.ID;
END;
//
DELIMITER ;

/*
Gatilho de Exclusão (DELETE Trigger) para Remover Reservas Associadas a Clientes Excluídos:
*/
DELIMITER //
CREATE TRIGGER CustomerDeleteTrigger
AFTER DELETE ON customer FOR EACH ROW
BEGIN
    DELETE FROM reserves WHERE customer_person_cpf = OLD.cpf;
END;
//
DELIMITER ;






