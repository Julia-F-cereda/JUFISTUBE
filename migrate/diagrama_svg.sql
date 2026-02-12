CREATE DATABASE IF NOT EXISTS jufisTube;
USE jufisTube;

CREATE TABLE IF NOT EXISTS genero (
 nome_genero VARCHAR(30) NOT NULL PRIMARY KEY ,
 icone VARCHAR(100),
 cor VARCHAR(10)
);


CREATE TABLE IF NOT EXISTS musica (
 codigo INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
 cantor VARCHAR(50),
 genero VARCHAR(50),
 duração TIME(6),
 nome VARCHAR(50),
 url_image VARCHAR(255),
 nome_genero VARCHAR(30),
 CONSTRAINT fk_musica_genero FOREIGN KEY (nome_genero) REFERENCES genero (nome_genero)
);

