CREATE_DW = '''
CREATE TABLE dimlibros(
	id_libro INT PRIMARY KEY,
	titulo VARCHAR (50), 
	lenguaje VARCHAR (50),
	genero VARCHAR (50),
	editorial VARCHAR (50),
    autor VARCHAR (50)
);

CREATE TABLE dimsucursal(
    id_sucursal INT PRIMARY KEY,
    sucursal VARCHAR(50)
);


CREATE TABLE dimcliente(
	id_cliente INT PRIMARY KEY,
	nombre VARCHAR (50),
    apellido VARCHAR (50),
    correo varchar (50),
    telefono varchar (20),
    direccion varchar (50)
);


CREATE TABLE dimfechahora(
	id_fecha varchar (50) primary key,
	year int,
	month int,
	quarter int,
    day int,
	week int,
    dayofweek int,
	hour int, 
	minute int, 
    second int,
	is_weekend int,
	fecha_hora timestamp
);

-- tabla de hechos
CREATE TABLE factorden(
	id_orden INT PRIMARY KEY,
    titulo varchar (50),
    lenguaje varchar (50),
    genero varchar (50),
    editorial varchar (50),
    autor varchar (50),
    sucursal varchar (50),
    nombre varchar (50),
    apellido varchar (50),
    correo varchar (50),
    telefono varchar (50),
    id_libro INT,
	id_sucursal INT,
	id_cliente INT,
	id_fecha varchar (50),
    fecha_hora timestamp,
	CONSTRAINT fk_fact_dimcliente
		FOREIGN KEY (id_cliente)
			REFERENCES dimcliente(id_cliente),
	CONSTRAINT fk_fact_dimlibro
		FOREIGN KEY (id_libro)
			REFERENCES dimlibros(id_libro),
	CONSTRAINT fk_fact_dimsucursal
		FOREIGN KEY (id_sucursal)
			REFERENCES dimsucursal(id_sucursal),
	CONSTRAINT fk_fact_dimfechahora
		FOREIGN KEY (id_fecha)
			REFERENCES dimfechahora(id_fecha)
);
'''