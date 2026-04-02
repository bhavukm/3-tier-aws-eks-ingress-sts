from flask import Flask
import psycopg2
import os

app = Flask(__name__)

conn = psycopg2.connect(
    host=os.environ.get("DB_HOST"),
    database="postgres",
    user=os.environ.get("POSTGRES_USER"),
    password=os.environ.get("POSTGRES_PASSWORD")
)

@app.route("/insert")
def insert():

    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS demo(id serial primary key, message text)")
    cur.execute("INSERT INTO demo(message) VALUES('Hello from Kubernetes')")
    conn.commit()

    return "Data inserted into PostgreSQL"

@app.route("/data")
def data():

    cur = conn.cursor()
    cur.execute("SELECT * FROM demo")
    rows = cur.fetchall()

    return str(rows)

app.run(host="0.0.0.0", port=5000)