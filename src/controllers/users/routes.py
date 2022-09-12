from src.controllers.users.functions import *
from src.server.instance import app

@app.route("/users", methods=["GET"])
def getAllForUser():
    return getAllUsers()