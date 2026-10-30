from flask import Flask, render_template    # Necesario para llamar a las paginas html

app = Flask(__name__)   # Inicializa un objeto de la clase Flask

@app.route("/")
def register():
    #return render_template("register.html")
    return render_template("dashboard.html")

if __name__ == "__main__":
    app.run(debug=True)