from flask import Flask, render_template
import psycopg2
import os

app = Flask(__name__)

def obtener_proveedores():
    conn = psycopg2.connect(
        host=os.getenv("PGHOST"),
        user=os.getenv("PGUSER"),
        password=os.getenv("PGPASSWORD"),
        dbname=os.getenv("PGDATABASE"),
        port=os.getenv("PGPORT", 5432)
    )
    cursor = conn.cursor()
    cursor.execute("SELECT nombre FROM proveedores")
    proveedores = [row[0] for row in cursor.fetchall()]
    cursor.close()
    conn.close()
    return proveedores

@app.route("/")
def index():
    proveedores = obtener_proveedores()
    return render_template("index.html", proveedores=proveedores)

if __name__ == "__main__":
    app.run(debug=True)
