CREATE DATABASE IF NOT EXISTS dev_burguer;
use dev_burguer;

CREATE TABLE IF NOT EXISTS produtos (
	codigo INT AUTO_INCREMENT PRIMARY KEY,
    produto VARCHAR(200),
    descricao VARCHAR(200),
    preco FLOAT,
    destaque VARCHAR(20),
    foto VARCHAR(255),
    disponibilidade VARCHAR(20)
    );

CREATE TABLE IF NOT EXISTS usuarios (
    nome VARCHAR(100) DEFAULT "ANONIMO",
    usuario VARCHAR(100) NOT NULL PRIMARY KEY,
    senha VARCHAR(255) NOT NULL
	);
    
CREATE TABLE IF NOT EXISTS carrinhos (
	cod_carrinho INT AUTO_INCREMENT PRIMARY KEY,
	usuario VARCHAR(100),
	data DATETIME DEFAULT CURRENT_TIMESTAMP,
	finalizado BOOL,
	CONSTRAINT fk_carrinho_usuario FOREIGN KEY (usuario) REFERENCES usuarios(usuario)
	);

CREATE TABLE IF NOT EXISTS itens_carrinhos(
	cod_item_carrinho INT AUTO_INCREMENT PRIMARY KEY,
    cod_carrinho INT,
    cod_produto INT,
    quantidade INT DEFAULT 1,
    CONSTRAINT fk_itenscarrinho_carrinhos FOREIGN KEY (cod_carrinho) REFERENCES carrinhos(cod_carrinho),
    CONSTRAINT fk_itenscarrinho_itens FOREIGN KEY (cod_produto) REFERENCES produtos(codigo)
	);