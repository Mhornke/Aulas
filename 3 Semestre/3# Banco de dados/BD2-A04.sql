-- SLIDES AULA
DROP SCHEMA IF EXISTS aula04;
CREATE SCHEMA IF NOT EXISTS aula04;
USE aula04;

-- Criando a tabela produto
DROP TABLE IF EXISTS produto;

CREATE TABLE IF NOT EXISTS produto (
  codigo      CHAR(3),
  descricao   VARCHAR(50) NOT NULL,
  qtd_estoque INT(11) NOT NULL,
  CHECK (qtd_estoque > 0),
  PRIMARY KEY (codigo)
);

-- Inserindo na tabela produto
INSERT INTO produto (codigo, descricao, qtd_estoque) VALUES ('001', 'Feijão', 10);
INSERT INTO produto (codigo, descricao, qtd_estoque) VALUES ('002', 'Arroz', 5);
INSERT INTO produto (codigo, descricao, qtd_estoque) VALUES ('003', 'Farinha', 15);
SELECT * FROM produto ;

-- Criando a tabela itensVenda
DROP TABLE IF EXISTS itensVenda;

CREATE TABLE IF NOT EXISTS itensVenda (
  id             INT,
  venda          INT,
  produto_codigo CHAR(3) NOT NULL,
  qtd_vendida    INT(11) NOT NULL,
  PRIMARY KEY (id),
  CONSTRAINT fk_itensVenda_produto
    FOREIGN KEY (produto_codigo) REFERENCES produto (codigo)
);

-- Criando trigger que será executada após as inclusões
DELIMITER $$

CREATE TRIGGER trg_itensvenda_AI AFTER INSERT
ON itensVenda
FOR EACH ROW
BEGIN
    UPDATE produto SET produto.qtd_estoque = produto.qtd_estoque - NEW.qtd_vendida WHERE produto.codigo = NEW.produto_codigo;
END$$

DELIMITER ;

-- Criando trigger que será executada após as exclusões
DELIMITER $$

CREATE TRIGGER trg_itensvenda_AD AFTER DELETE
ON itensVenda
FOR EACH ROW
BEGIN
    UPDATE produto SET produto.qtd_estoque = produto.qtd_estoque + OLD.qtd_vendida WHERE produto.codigo = OLD.produto_codigo;
END$$

DELIMITER ;

-- Inserindo vendas
SELECT * FROM produto;
INSERT INTO itensVenda VALUES (1, 1, '003',2);
INSERT INTO itensVenda VALUES (2, 1, '001',3);
INSERT INTO itensVenda VALUES (3, 1, '002',1);
INSERT INTO itensVenda VALUES (4, 2, '002',1);
INSERT INTO itensVenda VALUES (5, 2, '003',4);
INSERT INTO itensVenda VALUES (6, 2, '001',3);
INSERT INTO itensVenda VALUES (7, 3, '001',1);
INSERT INTO itensVenda VALUES (8, 3, '002',2);
SELECT * FROM produto;

-- Excluindo vendas
DELETE FROM itensVenda WHERE id = 1;
SELECT * FROM produto;

-- DESAFIO

/* 1 – Criar um gatilho/trigger para atualizar o campo qtd_estoque na tabela produtos 
sempre que for feita uma atualização/update na tabela itensvenda. */
DELIMITER $$ -- delimitador ( substitui o delimitador ";" por "$$" para fazer a procedure)
  CREATE PROCEDURE SP_AtualizaEstoque(var_idProduto INT, var_qtdComprada INT, var_vlrUnitario DECIMAL(9, 2))
  -- declarção da procedure que aceita 3 parametros 
BEGIN -- inicio do bloco de procedimento
  DECLARE var_contador INT (11);

  SELECT COUNT(*) INTO var_contador FROM estoque WHERE idProduto = var_idProduto;

  IF var_contador > 0 THEN
    UPDATE estoque SET qtd = qtd + var_qtdComprada, vlrUnitario = var_vlrUnitario
    WHERE idProduto = var_idProduto;
    ELSE
      INSERT INTO estoque (idProduto, qtd, vlrUnitario) VALUES (var_idProduto, var_qtdComprada, var_vlrUnitario);

    END IF;
  END $$
  DELIMITER ;  















/* 2 – Criar uma tabela chamada log. 
Esta tabela deve ter os campos: produto_cod, nomeAnterior, nomeNovo e dataHora. 
A tabela log deverá armazenar as alterações que forem feitas 
no campo descricao da tabela produto. */

