/* Pregunta 2: SQL y Modelado de Bases de Datos
Se proporciona el siguiente esquema simplificado de una base de datos de una librería:
Tabla: Libros
- id_libro (PK)
- titulo
- autor_id (FK a Autores.id_autor)
- categoria_id (FK a Categorias.id_categoria)
- precio
Tabla: Autores
- id_autor (PK)
- nombre
- nacionalidad
Tabla: Categorias
- id_categoria (PK)
- nombre
Escriba consultas SQL para realizar las siguientes operaciones:
1. Seleccione el título y el nombre del autor de todos los libros de la categoría "Ficción".
2. Calcule el precio promedio de todos los libros en la tabla Libros.
3. Actualice el precio de todos los libros escritos por el autor con id_autor = 5 en un 10% de descuento. */

/* 1.Seleccionar el título y el nombre del autor de todos los libros de la categoría "Ficción": */
SELECT Libros.titulo, Autores.nombre
FROM Libros
JOIN Autores ON Libros.autor_id = Autores.id_autor
JOIN Categorias ON Libros.categoria_id = Categorias.id_categoria
WHERE Categorias.nombre = 'Ficción';

/* 2. Calcular el precio promedio de todos los libros: */
SELECT AVG(precio) AS precio_promedio
FROM Libros;

/* Actualizar el precio de todos los libros escritos por el autor con id_autor = 5 con un 10% de descuento: */
UPDATE Libros
SET precio = precio * 0.9
WHERE autor_id = 5;

