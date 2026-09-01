-- Criação da Tabela Clientes
CREATE TABLE Clientes (
    ID INTEGER PRIMARY KEY,
    nomeCliente VARCHAR(255),
    emailCliente VARCHAR(255)
);

-- Criação da Tabela Compras
CREATE TABLE Compras (
    CompraID INTEGER PRIMARY KEY,
    ClienteID INTEGER,
    NomeLivro VARCHAR(255),
    FOREIGN KEY (ClienteID) REFERENCES Clientes(ID)
);

-- 2. Inserção de Dados (Baseado nos dados visíveis no seu print)
INSERT INTO Clientes (ID, nomeCliente, emailCliente) VALUES
(1, 'Carlos Silva', 'carlos@email.com'),
(2, 'Ana Souza', 'ana@email.com'),
(3, 'Mariana Costa', 'mariana@email.com');

INSERT INTO Compras (CompraID, ClienteID, NomeLivro) VALUES
(101, 1, 'O Hobbit'),
(102, 1, '1984'),
(103, 2, 'Dom Casmurro'),
(104, 3, 'O Alquimista');

-- 3. Linhas de comando solicitadas para visualização nas abas 1 e 2
SELECT * FROM Clientes;
SELECT * FROM Compras;


SELECT Clientes.nomeCliente, Compras.NomeLivro
FROM Compras
INNER JOIN Clientes ON Compras.ClienteID = Clientes.ID;
