CREATE DATABASE mamApp;
USE mamApp;

CREATE TABLE usuarios(
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre_usuario VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    edad VARCHAR(100),
    signo VARCHAR(100),
    comuna VARCHAR(100),
    descripcion TEXT,
    password_hash VARCHAR(500)
);