import requests
import psycopg2
import logging

# Configurar logging
logging.basicConfig(level=logging.INFO)

# Endpoints de JSONPlaceholder
users_url = 'https://jsonplaceholder.typicode.com/users'
posts_url = 'https://jsonplaceholder.typicode.com/posts'

def fetch_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        logging.info(f'Datos obtenidos exitosamente de {url}')
        return response.json()
    else:
        logging.error(f'Error en la solicitud: {response.status_code}')
        return []

def insert_data(cursor, table, data):
    for record in data:
        columns = record.keys()
        values = [record[column] for column in columns]
        insert_statement = f'INSERT INTO {table} ({", ".join(columns)}) VALUES ({", ".join(["%s"] * len(values))}) ON CONFLICT (id) DO NOTHING'
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
