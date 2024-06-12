from flask import Flask, request, redirect, url_for
import psycopg2

app = Flask(__name__)

# Replace these values with your PostgreSQL connection details
DB_HOST = '35.224.105.0'
DB_NAME = 'myappdb'
DB_USER = 'myuser'
DB_PASSWORD = 'abhi@1234'

def create_connection():
    conn = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )
    return conn

def insert_data(name, email):
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
    conn.commit()
    conn.close()

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    email = request.form.get('email')
    insert_data(name, email)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
