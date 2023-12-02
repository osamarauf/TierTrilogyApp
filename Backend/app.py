from flask import Flask, render_template, request, redirect, url_for
import psycopg2

app = Flask(__name__, template_folder="../Frontend/template")

conn = psycopg2.connect(database="postgres", user="postgres", password="root", host="localhost", port="5432") 
cur = conn.cursor() 
cur.execute('''CREATE TABLE IF NOT EXISTS UserInfo (id serial PRIMARY KEY, username varchar(100), email varchar(100), password varchar(100));''') 
conn.commit() 
cur.close() 
conn.close() 

@app.route('/register', methods=['POST']) 
def create(): 
    conn = psycopg2.connect(database="postgres", user="postgres", password="root", host="localhost", port="5432") 
    cur = conn.cursor() 
    username = request.form['username'] 
    email = request.form['email'] 
    password = request.form['password'] 
    cur.execute('''INSERT INTO userinfo (username, email, password) VALUES (%s, %s, %s)''', (username, email, password)) 
    conn.commit() 
    cur.close() 
    conn.close() 
  
    return redirect(url_for('index')) 

@app.route('/view', methods=['GET'])
def view_users():
    conn = psycopg2.connect(database="postgres", user="postgres", password="root", host="localhost", port="5432") 
    cur = conn.cursor() 
    cur.execute('''SELECT * FROM userinfo''') 
    data = cur.fetchall() 
    cur.close() 
    conn.close() 
    return render_template('index.html', data=data) 

@app.route('/') 
def index():
    conn = psycopg2.connect(database="postgres", user="postgres", password="root", host="localhost", port="5432") 
    cur = conn.cursor() 
    cur.execute('''SELECT * FROM userinfo''') 
    data = cur.fetchall() 
    cur.close() 
    conn.close() 
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
