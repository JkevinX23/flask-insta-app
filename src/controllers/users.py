from flask_restx import Resource

from src.server.instance import app

users_db = [
    {'id': 0, 'name': 'joão'},
    {'id': 1, 'name': 'kevin'}
]

@app.route('/users')
class UserList(Resource): 
    def get(self):
        return users_db
