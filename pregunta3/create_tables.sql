CREATE TABLE IF NOT EXISTS Usuarios (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    nombre_usuario VARCHAR(100),
    email VARCHAR(100),
    direccion JSONB,
    telefono VARCHAR(20),
    sitio_web VARCHAR(100),
    empresa JSONB
);

CREATE TABLE IF NOT EXISTS Publicaciones (
    id SERIAL PRIMARY KEY,
    usuario_id INT,
    titulo VARCHAR(200),
    cuerpo TEXT,
    FOREIGN KEY (usuario_id) REFERENCES Usuarios (id)
);
