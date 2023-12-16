from flask import Flask, jsonify, render_template, request, redirect, url_for
import psycopg2

app = Flask(__name__,)

conn = psycopg2.connect(database="postgres", user="postgres", password="root", host="localhost", port="5432") 
cur = conn.cursor() 
cur.execute('''CREATE TABLE IF NOT EXISTS UserInfo (id serial PRIMARY KEY, username varchar(100), email varchar(100), password varchar(100));''') 
conn.commit() 
cur.close() 
conn.close() 

@app.route('/create', methods=['POST']) 
def create(): 
    conn = psycopg2.connect(database="postgres", user="postgres", password="root", host="localhost", port="5432") 
    cur = conn.cursor() 
    data = request.json
    username = data.get('username') 
    email = data.get('email') 
    password = data.get('password') 
    cur.execute('''INSERT INTO userinfo (username, email, password) VALUES (%s, %s, %s)''', (username, email, password)) 
    conn.commit() 
    cur.close() 
    conn.close() 
    return jsonify({'message': 'User Created'}), 200

@app.route('/get', methods=['GET'])
def view_users():
    conn = psycopg2.connect(database="postgres", user="postgres", password="root", host="localhost", port="5432") 
    cur = conn.cursor() 
    cur.execute('''SELECT * FROM userinfo''') 
    data = cur.fetchall()
    userData = [{'username': user[1], 'email':user[2], 'password': user[3]} for user in data]
    cur.close() 
    conn.close() 
    return jsonify(userData)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
