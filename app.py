from flask import Flask, render_template, request, redirect, url_for, flash
from db import get_db, init_db

app = Flask(__name__)
app.secret_key = "clave-secreta-dev"
init_db()

# --- RUTAS ---

@app.route("/")
def index():
    conn = get_db()
    productos = conn.execute("SELECT * FROM productos ORDER BY id DESC").fetchall()
    conn.close()
    return render_template("index.html", productos=productos)

@app.route("/nuevo", methods=["GET", "POST"])
def nuevo():
    if request.method == "POST":
        conn = get_db()
        conn.execute(
            "INSERT INTO productos (nombre, categoria, precio, stock) VALUES (?, ?, ?, ?)",
            (request.form["nombre"], request.form["categoria"],
             float(request.form["precio"]), int(request.form["stock"])))
        conn.commit()
        conn.close()
        flash("Producto creado")
        return redirect(url_for("index"))
    return render_template("form.html", titulo="Nuevo producto", p=None)

if __name__ == "__main__":
    app.run(debug=True)