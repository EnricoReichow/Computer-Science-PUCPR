-- | Criação dos Usuários | --

CREATE USER IF NOT EXISTS 'clientes'@'localhost';
CREATE USER IF NOT EXISTS 'admin'@'localhost' identified by 'PizzaBoa';
CREATE USER IF NOT EXISTS 'garcom'@'localhost' identified by 'GarcomBom';
CREATE USER IF NOT EXISTS 'caixa'@'localhost' identified by 'CaixaBom';
CREATE USER IF NOT EXISTS 'chef'@'localhost' identified by 'CozinheiroBom';
CREATE USER IF NOT EXISTS 'gerente'@'localhost' identified by 'GerenteBom';

-- | Criação dos Papéis(Roles) | --

CREATE ROLE IF NOT EXISTS 'admin', 'gerente', 'funcionarios', 'clientes';

-- | Garantindo Privilégios para todas as Roles | --

-- Administrador do Banco de Dados, habilidade de modificar todos bancos de dados do servidor
GRANT ALL ON *.* TO 'admin' WITH GRANT OPTION;

-- Habilidade de resolver problemas de dados ou alterar valores relacionados a pizzaria (Ex: Promoções, Dado inserido errado no cadastro, novo fornecedor)
GRANT SELECT, UPDATE, INSERT, DELETE ON pizcaria.* TO 'gerente' WITH GRANT OPTION;

-- Habilidade de modificar novos clientes, pedidos e reservas
GRANT SELECT, UPDATE, INSERT, DELETE ON pizcaria.reserves TO 'funcionarios';
GRANT SELECT, INSERT ON pizcaria.customer TO 'funcionarios';
GRANT SELECT, INSERT ON pizcaria.person TO 'funcionarios';
GRANT SELECT, UPDATE, INSERT ON pizcaria.orders TO 'funcionarios';
GRANT INSERT ON pizcaria.restaurant_transactions TO 'funcionarios';

-- Habilidade de ver seus dados cadastrados, reservas, pedidos e sabores disponíveis
GRANT SELECT ON pizcaria.customer TO 'clientes';
GRANT SELECT ON pizcaria.menu TO 'clientes';
GRANT SELECT ON pizcaria.reserves TO 'clientes';
GRANT SELECT ON pizcaria.restaurant_transactions TO 'clientes';

-- | Garantindo as Roles para os Users | -- 

GRANT 'admin' TO 'admin'@'localhost';
GRANT 'gerente' TO 'gerente'@'localhost';
GRANT 'funcionarios' TO 'garcom'@'localhost', 'caixa'@'localhost', 'chef'@'localhost';
GRANT 'clientes' TO 'clientes'@'localhost';


