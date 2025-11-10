from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host='db', user='root', password='rootpassword', database='testdb'
    )

@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT message FROM messages')
    messages = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('index.html', messages=messages)

@app.route('/add', methods=['POST'])
def add_message():
    msg = request.form['message']
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO messages (message) VALUES (%s)', (msg,))
    conn.commit()
    cursor.close()
    conn.close()
    return 'Message Added! <a href="/">Back</a>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
