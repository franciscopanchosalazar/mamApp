CREATE DATABASE mamApp;
USE mamApp;

CREATE TABLE usuarios(
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre_usuario VARCHAR(100) UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    edad VARCHAR(100),
    signo VARCHAR(100),
    comuna VARCHAR(100),
    descripcion TEXT,
    contraseña_encriptada VARCHAR(500) NOT NULL
);

ALTER TABLE usuarios
ADD latitud DECIMAL(10,8) NULL;

ALTER TABLE usuarios
ADD longitud DECIMAL(11,8) NULL;