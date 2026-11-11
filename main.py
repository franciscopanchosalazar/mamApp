from flask import Flask, render_template, redirect, request, url_for, session, jsonify    # Necesario para llamar a las paginas html y obtener su información
import mysql.connector # Permite a Python hablar con las bases de datos de MySQL 
from dotenv import load_dotenv # Utilizado para traer la información privada desde el servidor a este archivo (.env)
import os # Nos permite acceder a las variables mencionadas antes
# Utilizado para hash (encriptar) una contraseña
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)   # Inicializa un objeto de la clase Flask
app.secret_key = "mi_app_key" # Crea una session key

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
        email = request.form["email"]
        contraseña = request.form["contraseña"]

        # Encripta la contraseña antes de guardarla
        contraseña_encriptada = generate_password_hash(contraseña)

        # Utilizado para probar si estamos obteniendo info de la forma de resgistro
        """
        print(email)
        print(contraseña)
        print(contraseña_encriptada)
        """

        sql_query = "INSERT INTO usuarios (email, contraseña_encriptada) VALUES (%s, %s);" 
        cursor.execute(sql_query, (email, contraseña_encriptada))
        db.commit()

        # Obtener id para saber usuario actual.
        session["id_usuario"] = cursor.lastrowid
        session["email"] = email

        return redirect(url_for("modificar_perfil"))

    return render_template("register.html")
# ------------------------------------------------------------------------------------------------------------------------------

@app.route("/iniciar_sesion", methods=['GET', 'POST'])
def login():
    cursor = db.cursor()

    if request.method == "POST":
        email =  request.form["email"]
        contraseña = request.form["contraseña"]

        # PARA HACER PRUEBAS
        #print(email)
        #print(contraseña)

        # Verifica la existencia del usuario
        sql_query = "SELECT id, nombre_usuario, email, contraseña_encriptada FROM usuarios WHERE email = %s"
        cursor.execute(sql_query, (email,))
        usuario = cursor.fetchone()

        if usuario==None:
            print(f"{email} no se encuentra registrado" ) # MODIFICAR ESTE PRINT POR ALGUNA OTRA ACCION
        else:
            # Verifica la contraseña
            if usuario and check_password_hash(usuario[3], contraseña): # usuario[3] representa la contraseña encriptada.

                # Recordar usuario actual
                session["id_usuario"] = usuario[0]  # usuario[0] representa al id del usuario.
                session["email"] = email
                session["nombre_usuario"] = usuario[1] # usuario[1] representa al nombre de usuario.

                return redirect(url_for("perfil"))
            else:
                # MODIFICAR ESTE PRINT POR ALGUNA OTRA ACCION                
                print(f"{usuario[2]} es valido.")
                print("Contraseña equivocada.")

    return render_template("login.html")
# ------------------------------------------------------------------------------------------------------------------------------

@app.route('/cerrar_sesion')
def logout():
    session.clear() # Remueve al usuario de la sesion si es que este existe.
    return redirect(url_for("registrar_usuario"))
# ------------------------------------------------------------------------------------------------------------------------------

@app.route('/modificar_perfil' , methods=['GET', 'POST'])
def modificar_perfil():
    # Obtiene la id de la sesion actual
    id_usuario = session.get("id_usuario")

    # Asegura que tengamos un usuario activo
    if "id_usuario" not in session:
        return redirect(url_for("registrar_usuario"))
    
    cursor = db.cursor()    # Utilizado para llevar a cabo las queries de MySql

    if request.method == "POST":
        nombre =  request.form["nombre"]
        edad = request.form["edad"]
        signo = request.form["signo"]
        comuna = request.form["comuna"]
        descripcion = request.form["descripcion"]
    
        # PARA HACER PRUEBAS
        """
        print(nombre)
        print(edad)
        print(signo)
        print(comuna)
        print(descripcion)
        """

        sql_query = """UPDATE usuarios SET 
        nombre_usuario = %s,
        edad = %s, 
        signo = %s, 
        comuna= %s, 
        descripcion = %s
        WHERE id = %s;""" 

        cursor.execute(sql_query, (nombre, edad, signo, comuna, descripcion, id_usuario))
        db.commit()

        # Al igual que id_usuario e eimail, almacenamos el nombre (obtenido de la forma) en la sesion.
        session["nombre_usuario"] = nombre
        
        return redirect(url_for("perfil"))

    return render_template("editProfile.html")
# ------------------------------------------------------------------------------------------------------------------------------

@app.route('/perfil' , methods=['GET', 'POST'])
def perfil():
    if "id_usuario" not in session:
        return redirect(url_for("registrar_usuario"))
    
    return render_template("dashboard.html")
# ------------------------------------------------------------------------------------------------------------------------------

# Probablemente no lo use mas que para pruebas
@app.route('/mapa')
def mapa():
    return render_template("map.html")
# ------------------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    app.run(debug=True)
