""" Pregunta 3: Integraciones ERP vía API (Utilizando JSONPlaceholder API)
Supongamos que necesitamos integrar datos de JSONPlaceholder utilizando su API RESTful para obtener
información detallada sobre usuarios y publicaciones.
1. Diseñe una función en Python que:
o Autentique y obtenga acceso a la API de JSONPlaceholder.
o Extraiga los detalles de usuarios y publicaciones (nombre de usuario, email, título de
publicación, cuerpo de publicación, etc.) y guarde esta información en las tablas
correspondientes (Usuarios, Publicaciones).
o Modele los datos en un esquema de base de datos estrella.
2. Se necesita la información en una esquena NearRealtime con actualización diaria, realice un función
Python que diariamente sea ejecutada (sugiera el mecanismo de ejecución en la nube).
Instrucciones Adicionales:
•
•
•
Utilice los siguientes endpoints de JSONPlaceholder para obtener los datos:
o https://jsonplaceholder.typicode.com/users para datos de usuarios.
o https://jsonplaceholder.typicode.com/posts para datos de publicaciones.
Modele los datos en tablas separadas según el modelo propuesto (Usuarios, Publicaciones).
Se solicita además utilizar las mejores prácticas de programación y mecanismos de log .
3. Finalmente se requiere que las tablas obtenidas sean creadas en una BD PostgreSQL 16. implementada
en un esquema dockerizado.
•
•
•
•
•
Entregue los elementos que sean requeridos para crear:
Contenedor de la Base de Datos vía DockerCompose que incluya el SQL de creación de las tablas
y relaciones.
Programa PYTHON que cargue los datos del punto 1.
Archivo docker-compose.yml para implementar el contenedor de Postgresql.
NOTA: Al crear el contenedor Docker de Postgresql debe crear la BD a utilizar. """

import requests
import psycopg2
from psycopg2 import sql
import logging

# Configurar logging
logging.basicConfig(level=logging.INFO)

# Endpoints de JSONPlaceholder
users_url = 'https://jsonplaceholder.typicode.com/users'
posts_url = 'https://jsonplaceholder.typicode.com/posts'

# Función para obtener datos de JSONPlaceholder
def fetch_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        logging.info(f'Datos obtenidos exitosamente de {url}')
        return response.json()
    else:
        logging.error(f'Error en la solicitud: {response.status_code}')
        return []

# Función para insertar datos en la base de datos
def insert_data(cursor, table, data):
    for record in data:
        columns = record.keys()
        values = [record[column] for column in columns]
        insert_statement = sql.SQL('INSERT INTO {table} ({fields}) VALUES ({values}) ON CONFLICT (id) DO NOTHING').format(
            table=sql.Identifier(table),
            fields=sql.SQL(', ').join(map(sql.Identifier, columns)),
            values=sql.SQL(', ').join(sql.Placeholder() * len(values))
        )
        cursor.execute(insert_statement, values)

# Obtener datos de usuarios y publicaciones
users = fetch_data(users_url)
posts = fetch_data(posts_url)

# Conectar a la base de datos PostgreSQL
conn = psycopg2.connect(
    dbname="nombre_base_datos",
    user="usuario",
    password="contraseña",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

# Insertar datos en las tablas correspondientes
insert_data(cur, 'Usuarios', users)
insert_data(cur, 'Publicaciones', posts)

# Confirmar los cambios y cerrar la conexión
conn.commit()
cur.close()
conn.close()

logging.info('Datos insertados exitosamente en la base de datos.')
