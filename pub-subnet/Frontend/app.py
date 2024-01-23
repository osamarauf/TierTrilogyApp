from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)


@app.route('/view')
def getUser():
    try:
        hostname = request.host.split(':')[0]
        api_url = f'http://{hostname}:80/get'
        response = requests.get(api_url)
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
    hostname = request.host.split(':')[0]
    api_url_get = f'http://{hostname}:80/get'
    api_url_create = f'http://{hostname}:80/create'
    response = requests.post(api_url_create, json=data)
    responses = requests.get(api_url_get)
    userList = responses.json()
    if response.status_code == 200:
        return render_template('index.html', userList=userList)
    else:
        return jsonify({'error': 'Failed to create user'}), 500
    
        
if __name__ == '__main__':
    app.run(debug=True, port=3000, host="0.0.0.0")