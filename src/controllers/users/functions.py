from flask import jsonify
from src.models.users import *


def getAllUsers():
    result = Users.query.all()
    return_results = users_schema.dump(result)
    return jsonify(
        {
            "success": True,
            "data": {
                "users": return_results
            }

        }
    )