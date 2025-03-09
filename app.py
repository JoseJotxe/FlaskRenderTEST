## Crea una Aplicación Web con Python y Flask | Sin Base de Datos | Despliegue en Render
## Canal CODIGO ESPINOSA
## https://youtu.be/fYu0KDuiw2Q
##

## Pasos
# Creamos la carpeta TEMPLATE ==> aquí es donde están todas las plantillas HTML
#  Dentro de template creamos los templates: el archivo home.html , about.html y form.html
# Creamos la carpeta STATIC ==> aquí es donde están todos los archivos estáticos (CSS, JS, Imágenes)
#   Dentro de static creamos el archivo styles.css

## archivo de requerimientos: pip freeze > requirements.txt  ==> genero el archivo de requerimientos
# voy a dejar solo 
# Flask
# gunicorn  ==> este es para poder trabajar con render

## LIBRERIAS
from flask import Flask, render_template, request, redirect, url_for
import csv
import os  


## Inicializamos aplicacón FLASK
app = Flask(__name__)

CSV_FILE = 'users.csv'  # Archivo que vamos
## Creamos una funcion para leer los usuarios   
def read_users():
    if not os.path.exists(CSV_FILE):  # si no existe lo crea con una lista vacia
        return []
    with open(CSV_FILE, newline='', encoding='utf-8') as csvfile:  # si existe lo lee
        reader = csv.reader(csvfile)
        return list(reader)  # transofrma el archivo en una lista


# Creamos la funcion para añadir un usuario
def add_user(name, email):
    with open(CSV_FILE, mode='a', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([name, email])


## Creamos ruta de inicio  (al ejecutar la APP de flask vamos a estar en un servidor y decimos en que pagina se ejecutan als acciones (la raiz en este caso)
@app.route('/')  # Ruta de inicio. Se ejecutara la funcion home al entrar en la pagina de inicio
def home():   # guarda en una variable users los usuarios de un archivo
    users = read_users()
    return render_template('home.html', users=users)

# Ruta sobre nosotros
@app.route('/about')  # Ruta de about. Se ejecutara la funcion about al entrar en la pagina about
def about():
    return render_template('about.html')

# Ruta sobre nosotros   # tengo GET y POST porque cuando se carga la pagina se hace un GET y cuando se envia el formulario se hace un POST
@app.route('/register', methods=['GET', 'POST'])  # Ruta de register. para añadir un nuevo usuario
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        add_user(name, email)
        return redirect(url_for('home'))
    return render_template('form.html')


## Se va a ejecutar cuando corra el archivo desde app.ppy
if __name__ == '__main__':  # si el archivo se ejecuta directamente
    app.run(debug=True)  # ejecuta la aplicacion en modo debug  
