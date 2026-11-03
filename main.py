from flask import Flask, render_template, redirect, request, url_for, session     # Necesario para llamar a las paginas html y obtener su información
import mysql.connector # Permite a Python hablar con las bases de datos de MySQL 
from dotenv import load_dotenv # Utilizado para traer la información privada desde el servidor a este archivo (.env)
import os # Nos permite acceder a las variables mencionadas antes
app = Flask(__name__)   # Inicializa un objeto de la clase Flask

# Lee el archivo .env y hace que los valores dentro de él esten disponibles para el programa. 

load_dotenv()

# Connect to mysql using credentials stored in .env
# mysql.connector.connect will always ask for host, user, password and database
db = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)
@app.route("/")
def home():
    return render_template("register.html")
    #return render_template("dashboard.html")
    #return render_template("login.html")
# ------------------------------------------------------------------------------------------------------------------------------

# Usuarios

@app.route('/registrar' , methods=['POST'])
def registrar_usuario():
    cursor = db.cursor()    # Utilizado para llevar a cabo las queries de MySql

    if request.method == "POST":
        print("Formulario recibido")
        nombre_usuario =  request.form["nombre"]
        email = request.form["email"]
        contraseña = request.form["contraseña"]

        # Utilizado para probar si estamos obteniendo info de la forma de resgistro
        print(nombre_usuario)
        print(email)
        print(contraseña)

        return redirect(url_for("modificar_perfil"))

    # NO OLVIDAR VOLVER ACA

    # Encripta (Hash) la contraseña antes de guardar
    # contraseña_encriptada = generate_password_hash(contraseña)

    return render_template("register.html")
# ------------------------------------------------------------------------------------------------------------------------------

@app.route('/modificar_perfil' , methods=['GET', 'POST'])
def modificar_perfil():
    cursor = db.cursor()    # Utilizado para llevar a cabo las queries de MySql
    return render_template("dashboard.html")

if __name__ == "__main__":
    app.run(debug=True)
