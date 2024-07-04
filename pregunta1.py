""" Pregunta 1: Manipulación de Datos con API
Se proporciona la siguiente URL de una API pública que devuelve información sobre libros en formato JSON:
https://api.example.com/books
Escriba un script en Python que haga una solicitud a esta API, obtenga los datos y realice las siguientes tareas:
1. Calcule el número total de libros en la lista.
2. Guarde los datos en un archivo CSV llamado books.csv.
 """
#Se importan las 2 librerías necesarias para realizar la pregunta, una para las solicitudes y otra para realizar la escritura del archivo CSV
import requests
import csv

# URL de la API de ejemplo, aquí hay que cambiarla por la URL correspondiente de una API funcional.
url = 'https://api.example.com/books'

# Hacer la solicitud a la API y guardarla en una variable
response = requests.get(url)

# Si la solicitud fue exitosa
if response.status_code == 200:
    books = response.json()
    
    # Calcular el número total de libros
    total_books = len(books)
    print(f'Número total de libros: {total_books}')
    
    # Guardar los datos en un archivo CSV
    with open('books.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        # Asumo que estos son los valores y atributos del objeto libro, esta mal redactada su instrucción en el PDF,
        writer.writerow(['ID', 'Título', 'Autor', 'Categoría', 'Precio'])
        # Escribir el número total de libros
        writer.writerow(['Total de libros', total_books])
        # Escribir datos en el archivo CSV
        for book in books:
            writer.writerow([book['id'], book['title'], book['author'], book['category'], book['price']])
else:
    print(f'Error en la solicitud: {response.status_code}')
