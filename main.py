from flask import Flask, render_template    # Necesario para llamar a las paginas html
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
def register():
    return render_template("register.html")
    #return render_template("dashboard.html")
    #return render_template("login.html")
# ------------------------------------------------------------------------------------------------------------------------------

# Usuarios

@app.route('/registrar' , methods=['GET', 'POST'])
def registrar_usuario():
    cursor = db.cursor()

    # Debo comenzar a trabajar aca 
    return render_template("register.html")

if __name__ == "__main__":
    app.run(debug=True)
