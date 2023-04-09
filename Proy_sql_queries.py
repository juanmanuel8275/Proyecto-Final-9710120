DDL_QUERY =  '''
CREATE TABLE IF NOT EXISTS lenguaje(
    id_lenguaje INT PRIMARY KEY,
    lenguaje VARCHAR(50) UNIQUE
);

CREATE TABLE IF NOT EXISTS genero(
    id_genero INT PRIMARY KEY,
    genero VARCHAR(50) UNIQUE
);

CREATE TABLE IF NOT EXISTS Editorial(
    id_editorial INT PRIMARY KEY,
    editorial VARCHAR(50) UNIQUE
);

CREATE TABLE IF NOT EXISTS autor(
    id_autor INT PRIMARY KEY,
    autor VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS libros(
    id_libro INT PRIMARY KEY,
    titulo VARCHAR (50),
    id_lenguaje INT,
    id_genero INT,
    id_editorial INT,
    id_autor INT,

    CONSTRAINT fk_lenguaje_libros
        FOREIGN KEY (id_lenguaje)
            REFERENCES lenguaje(id_lenguaje),

    CONSTRAINT fk_genero_libros
        FOREIGN KEY (id_genero)
            REFERENCES genero(id_genero),

    CONSTRAINT fk_editorial_libros
        FOREIGN KEY (id_editorial)
            REFERENCES editorial(id_editorial),

    CONSTRAINT fk_autor_libros
        FOREIGN KEY (id_autor)
            REFERENCES autor(id_autor)
);

CREATE TABLE IF NOT EXISTS cliente(
    id_cliente INT PRIMARY KEY,
    nombre VARCHAR(50),
    apellido VARCHAR(50),
    correo VARCHAR(50),
    telefono VARCHAR(20),
    direccion VARCHAR (50)
);

CREATE TABLE IF NOT EXISTS sucursal(
    id_sucursal INT PRIMARY KEY,
    sucursal VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS orden(
    id_orden INT PRIMARY KEY,
    fecha_hora TIMESTAMP,

    id_libro INT,
    id_sucursal INT,
    id_cliente INT,
    
    CONSTRAINT fk_libros_orden
        FOREIGN KEY (id_libro)
            REFERENCES libros(id_libro),

    CONSTRAINT fk_sucursal_orden
        FOREIGN KEY (id_sucursal)
            REFERENCES sucursal(id_sucursal)

);
 '''