import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)

def create_db():
    SQLALCHEMY_DATABASE_URI = f"postgresql://{os.environ.getenv('DB_USER')}:{os.environ.getenv('DB_PASSWORD')}@{os.environ.getenv('DB_HOST')}:{os.environ.getenv('DB_PORT')}/{os.environ.getenv('DB_NAME')}" # f"postgresql://postgres:root@postgres:5432/postgres"
    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    return SQLAlchemy(app)

db = create_db()

class UserInfo(db.Model):
    __tablename__ = 'userinfo'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    email = db.Column(db.String(100))
    password = db.Column(db.String(100))

with app.app_context():
    db.create_all()

@app.route('/create', methods=['POST'])
def create():
    data = request.json
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    new_user = UserInfo(username=username, email=email, password=password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User Created'}), 200

@app.route('/get', methods=['GET'])
def view_users():
    users = UserInfo.query.all()
    userData = [{'username': user.username, 'email': user.email, 'password': user.password} for user in users]
    return jsonify(userData)

if __name__ == '__main__':
    app.run(debug=True, port=5000, host="0.0.0.0")
