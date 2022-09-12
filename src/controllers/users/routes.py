from flask import request
from src.controllers.users.functions import *
from src.server.instance import app

@app.route('/users', methods=["GET"])
def getAllForUser():
    return getAllUsers()

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    return createUser(data)
