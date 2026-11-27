from flask import Flask, render_template, request, redirect, url_for, flash
from db import get_db, init_db

app = Flask(__name__)
app.secret_key = "clave-secreta-dev"
init_db()

# --- RUTAS ---


if __name__ == "__main__":
    app.run(debug=True)