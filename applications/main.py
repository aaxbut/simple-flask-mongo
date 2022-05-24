from mongoengine import connect
from flask import Flask, request
from config.settings import settings
from applications.models import User

app = Flask(__name__)
app.db = connect(host=settings.URI_DB)


@app.route('/')
def index():
    return {
        'index': 'index'
    }


@app.route('/users', methods=['GET', ])
def fetch_users():
    users = []
    for user in User.objects:
        users.append(user.username)
    return {
        'users': users
    }


@app.route('/users', methods=['POST', ])
def create_user():
    print(request.json)
    username = request.json.get('username')
    user = User.objects(username=username).first()
    if not user:
        user = User(**request.json)
        user.save()
    return {
        'user': f'{user.username} :: {user.created_at}'
    }
