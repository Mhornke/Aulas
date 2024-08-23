-- SLIDES AULA
DROP SCHEMA IF EXISTS aula05;
CREATE SCHEMA IF NOT EXISTS aula05;
USE aula05;

-- Tabela PRODUTO
CREATE TABLE produto (
  id INT(11) AUTO_INCREMENT,
  status CHAR(1) NOT NULL DEFAULT 'A',
  descricao VARCHAR(50),
  estoqueMinimo INT(11),
  estoqueMaximo INT(11),
  PRIMARY KEY (id)
);

INSERT INTO produto (descricao, estoqueMinimo, estoqueMaximo)
VALUES
("PENDRIVE", 10, 100),
("MOUSE", 10, 100),
("IOGURTE", 5, 50),
("TEQUILA", 5, 40),
("PRESUNTO", 5, 20);

-- Tabela PRODUTOENTRADA (compra)
CREATE TABLE produtoEntrada (
  id INT(11) AUTO_INCREMENT,
  idProduto INT(11),
  qtd INT(11),
  vlrUnitario DECIMAL(9,2) NULL DEFAULT 0.00,
  entradaData DATE,
  PRIMARY KEY (id)
);

-- Tabela ESTOQUE
CREATE TABLE estoque (
  id INT(11) AUTO_INCREMENT,
  idProduto INT(11),
  qtd INT(11),
  vlrUnitario DECIMAL(9,2) NULL DEFAULT 0.00,
  PRIMARY KEY (id)
);

-- Tabela PRODUTOSAIDA (venda)
CREATE TABLE produtoSaida (
  id INT(11) AUTO_INCREMENT,
  idProduto INT(11),
  qtd INT(11),
  saidaData DATE,
  vlrUnitario DECIMAL(9,2) NULL DEFAULT 0.00,
  PRIMARY KEY (id)
);

-- Procedure ATUALIZAESTOQUE
DELIMITER $$
  CREATE PROCEDURE SP_AtualizaEstoque(var_idProduto INT, var_qtdComprada INT, var_vlrUnitario DECIMAL(9,2))
BEGIN
    DECLARE var_contador INT(11);

    SELECT COUNT(*) INTO var_contador FROM estoque WHERE idProduto = var_idProduto;

    IF var_contador > 0 THEN
        UPDATE estoque SET qtd=qtd + var_qtdComprada, vlrUnitario= var_vlrUnitario
        WHERE idProduto = var_idProduto;
    ELSE
        INSERT INTO estoque (idProduto, qtd, vlrUnitario) VALUES (var_idProduto, var_qtdComprada, var_vlrUnitario);
    END IF;
END $$
DELIMITER ;

-- Trigger trg_produtoEntrada_AI (INCLUSÃO de compra)
DELIMITER $$
CREATE TRIGGER trg_produtoEntrada_AI AFTER INSERT ON produtoEntrada
FOR EACH ROW
BEGIN
      CALL SP_AtualizaEstoque (NEW.idProduto, NEW.qtd, NEW.vlrUnitario);
END $$
DELIMITER ;

-- Trigger trg_produtoEntrada_AU (ALTERAÇÃO de compra)
DELIMITER $$
CREATE TRIGGER trg_produtoEntrada_AU AFTER UPDATE ON produtoEntrada
FOR EACH ROW
BEGIN
      CALL SP_AtualizaEstoque (NEW.idProduto, NEW.qtd - OLD.qtd, NEW.vlrUnitario);
END $$
DELIMITER ;

-- Trigger trg_produtoEntrada_AD (EXCLUSÃO de compra)
DELIMITER $$
CREATE TRIGGER trg_produtoEntrada_AD AFTER DELETE ON produtoEntrada
FOR EACH ROW
BEGIN
      CALL SP_AtualizaEstoque (OLD.idProduto, OLD.qtd * -1, OLD.vlrUnitario);
END $$
DELIMITER ;

-- Trigger trg_produtoSaida_AI (INCLUSÃO de venda)
DELIMITER $$
CREATE TRIGGER trg_produtoSaida_AI AFTER INSERT ON produtoSaida
FOR EACH ROW
BEGIN
      CALL SP_AtualizaEstoque (NEW.idProduto, NEW.qtd * -1, NEW.vlrUnitario);
END $$
DELIMITER ;

-- Trigger trg_produtoSaida_AU (ALTERAÇÃO de venda)
DELIMITER $$
CREATE TRIGGER trg_produtoSaida_AU AFTER UPDATE ON produtoSaida
FOR EACH ROW
BEGIN
      CALL SP_AtualizaEstoque (NEW.idProduto, OLD.qtd - NEW.qtd, NEW.vlrUnitario);
END $$
DELIMITER ;

-- Trigger trg_produtoSaida_AD (EXCLUSÃO de venda)
DELIMITER $$
CREATE TRIGGER trg_produtoSaida_AD AFTER DELETE ON produtoSaida
FOR EACH ROW
BEGIN
      CALL SP_AtualizaEstoque (OLD.idProduto, OLD.qtd, OLD.vlrUnitario);
END $$
DELIMITER ;






