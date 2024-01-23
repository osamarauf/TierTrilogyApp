from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)


@app.route('/view')
def getUser():
    try:
        response = requests.get('http://backend:5000/get')
        response.raise_for_status()
        userList = response.json()
        return render_template('index.html', userList=userList)
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"
        
        
@app.route('/register', methods=['POST'])
def createUser():
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')
    data = {'username': username, 'email':email, 'password': password}
    response = requests.post('http://backend:5000/create', json=data)
    responses = requests.get('http://backend:5000/get')
    userList = responses.json()
    if response.status_code == 200:
        return render_template('index.html', userList=userList)
    else:
        return jsonify({'error': 'Failed to create user'}), 500
    
        
if __name__ == '__main__':
    app.run(debug=True, port=3000, host="0.0.0.0")