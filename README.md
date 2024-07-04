# prueba-tecnica-seleccion-kairos-humano

Este repositorio contiene el desarrollo de la tarea asignada para el puesto de desarrollador fullstack en kairos humano consultoria.

# Desarrollo de requerimientos planteados en PDF

Este proyecto es la solución puntual para cada pregunta planteada en las instrucciones del PDF del repositorio.

## Estructura del Proyecto
```
prueba-t-cnica-selecci-n-kair-s-humano/
├── pregunta3/
│   ├── create_tables.sql
│   ├── docker-compose.yml
│   ├── lambda_function.py
│   ├── load_data.py
│   ├── logica.txt
│   └── pregunta3.py
├── pregunta4/
│   ├── parte1.sql
│   ├── parte2.sql
│   ├── parte3.sql
│   ├── parte4.sql
│   └──parte5.sql
├── pregunta1.py
├── pregunta2.sql
├── Prueba Técnica - Desarrollador Full Stack
└── README.md
```
### Descripción de Directorios y Archivos

- `/pregunta3`: Contiene los archivos que responden la pregunta 3 del PDF.
  - `create_tables.sql`: Archivo para crear la tablas tablas requeridas para la solución de la pregunta en la base de datos.
  - `docker-compose.yml`: Archivo utilizado para definir y configurar un entorno Docker que consiste en un servicio de base de datos PostgreSQL.
  - `lambda_function.py`: Archivo utilizado para definir NearRealtime con actualización diaria, realice un función Python que diariamente sea ejecutada.
  - `pregunta3.py`: Archivo utilizado para cargar los datos en la base de datos.
  - `logica.txt`: Archivo utilizado explicar mi logica utilizada para solucionar esta pregunta 3.
- `/pregunta4`: Contiene los archivos que responden la pregunta 4 del PDF.
  - `parte1.sql`: Listado de ventas del mes actual.
  - `parte2.sql`: Ventas totales por sucursal, vendedor y marca, incluyendo los vendedores sin ventas.
  - `parte3.sql`: Productos con más de 1000 unidades vendidas en los últimos 2 meses.
  - `parte4.sql`: Productos sin ventas en el presente año.
  - `parte5.sql`: De los productos sin ventas en el presente año, monto total de ventas en el año anterior.
- `pregunta1.py`: Archivo que responde la pregunta 1 del PDF
- `pregunta2.sql`: Archivo que responde la pregunta 2 del PDF
- `Prueba Técnica - Desarrollador Full Stack.pdf`: Archivo PDF con las instrucciones de la prueba técnica.
- `README.md`: Este archivo, con instrucciones y documentación del proyecto.

## Requisitos del Sistema

- Python 3.10
- Postgresql 17
- Sistema operativo Linux o MacOs

