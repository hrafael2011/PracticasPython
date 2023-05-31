

CREATE DATABASE IF NOT EXISTS cursopythondb

USE cursopythondb

CREATE TABLE usuarios(
    id          int auto_increment not null,
    nombre      varchar(100),
    apellidos   varchar(150),
    email       varchar(200) not null,
    pass        varchar (200) not null,
    fecha       date not null
    CONSTRAINT pk_usuarios PRIMARY KEY(id),
    CONSTRAINT uq_email UNIQUE(email)
)ENGINE=InnoDB;

CREATE TABLE notas(
    id          int auto_increment not null,
    usuario_Id  int not null,
    titulo      varchar(200) not null,
    descripcion text,
    fecha       date,
    CONSTRAINT pk_notas PRIMARY KEY(id),
    CONSTRAINT fk_nota_usuario FOREIGN KEY(usuario_Id) REFERENCES usurios(id)
)ENGINE=InnoDB;