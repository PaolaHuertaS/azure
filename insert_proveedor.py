import psycopg2
import os

def insertar_proveedor(nombre):
    conn = psycopg2.connect(
        host=os.getenv("PGHOST"),
        user=os.getenv("PGUSER"),
        password=os.getenv("PGPASSWORD"),
        dbname=os.getenv("PGDATABASE"),
        port=os.getenv("PGPORT", 5432)
    )
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS proveedores (
            id SERIAL PRIMARY KEY,
            nombre VARCHAR(100) NOT NULL
        );
    """)
    cursor.execute("INSERT INTO proveedores (nombre) VALUES (%s)", (nombre,))
    conn.commit()
    cursor.close()
    conn.close()

if __name__ == "__main__":
    insertar_proveedor("Paola Huerta")
    print("Proveedor insertado")
