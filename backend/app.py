import os
import psycopg2
from flask import Flask, jsonify, request

app = Flask(__name__)

def get_db_connection():
    return psycopg2.connect(
        host=os.environ.get("DB_HOST", "db"),
        database=os.environ.get("POSTGRES_DB", "appdb"),
        user=os.environ.get("POSTGRES_USER", "admin"),
        password=os.environ.get("POSTGRES_PASSWORD", "secretpassword")
    )

@app.route("/api/items", methods=["GET"])
def get_items():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, name, created_at FROM items ORDER BY id DESC;")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    items = [{"id": r[0], "name": r[1], "created_at": str(r[2])} for r in rows]
    return jsonify(items)

@app.route("/api/items", methods=["POST"])
def add_item():
    data = request.get_json()
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO items (name) VALUES (%s);", (data["name"],))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({"status": "Task added!"}), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
