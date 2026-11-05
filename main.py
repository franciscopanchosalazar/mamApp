from flask import Flask, render_template, redirect, request, url_for, session, jsonify     # Necesario para llamar a las paginas html y obtener su información
import mysql.connector # Permite a Python hablar con las bases de datos de MySQL 
from dotenv import load_dotenv # Utilizado para traer la información privada desde el servidor a este archivo (.env)
import os # Nos permite acceder a las variables mencionadas antes
# Utilizado para hash (encriptar) una contraseña
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)   # Inicializa un objeto de la clase Flask

# Lee el archivo .env y hace que los valores dentro de él esten disponibles para el programa. 

load_dotenv()

# Conecta a mysql usando las credenciales que se encuentran dentro de .env
db = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)

@app.route("/")
def home():
    return render_template("register.html")
# ------------------------------------------------------------------------------------------------------------------------------

# Usuarios

@app.route('/registrar' , methods=['GET', 'POST'])
def registrar_usuario():
    cursor = db.cursor()    # Utilizado para llevar a cabo las queries de MySql

    if request.method == "POST":
        nombre_usuario =  request.form["nombre"]
        email = request.form["email"]
        contraseña = request.form["contraseña"]

        # Hash the password before saving
        contraseña_encriptada = generate_password_hash(contraseña)

        # Utilizado para probar si estamos obteniendo info de la forma de resgistro
        print(nombre_usuario)
        print(email)
        print(contraseña)
        print(contraseña_encriptada)
    
        sql_query = "INSERT INTO usuarios (nombre_usuario, email, contraseña_encriptada) VALUES (%s, %s, %s)" 
        cursor.execute(sql_query, (nombre_usuario, email, contraseña_encriptada))
        db.commit()

        return redirect(url_for("modificar_perfil"))

    return render_template("register.html")
# ------------------------------------------------------------------------------------------------------------------------------

@app.route("/iniciar_sesion", methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        email =  request.form["email"]
        contraseña = request.form["contraseña"]

        # PARA HACER PRUEBAS
        print(email)
        print(contraseña)

        return redirect(url_for("perfil"))

    return render_template("login.html")
# ------------------------------------------------------------------------------------------------------------------------------

@app.route('/modificar_perfil' , methods=['GET', 'POST'])
def modificar_perfil():
    cursor = db.cursor()    # Utilizado para llevar a cabo las queries de MySql

    if request.method == "POST":
        nombre =  request.form["nombre"]
        edad = request.form["edad"]
        signo = request.form["signo"]
        comuna = request.form["comuna"]
        descripcion = request.form["descripcion"]
    
        # PARA HACER PRUEBAS
        print(nombre)
        print(edad)
        print(signo)
        print(comuna)
        print(descripcion)

        return redirect(url_for("perfil"))

    return render_template("editProfile.html")
# ------------------------------------------------------------------------------------------------------------------------------

@app.route('/perfil' , methods=['GET', 'POST'])
def perfil():
    return render_template("dashboard.html")
# ------------------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    app.run(debug=True)
