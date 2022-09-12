import uuid
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

def createUser(jsonUser): 
        try:
          name = jsonUser["name"]
          description = jsonUser["description"]
          profile_url = jsonUser["profile_url"]
          nickname = jsonUser["nickname"]
          newUser = Users(id=uuid.uuid4(),name = name, description = description, profile_url = profile_url, nickname = nickname)
          db.session.add(newUser)
          db.session.commit()
          return jsonify(
                {
                    "success": True,
                    "message": "Successfully added",
                }
            )
        except Exception as e:
            print(str(e))
            return jsonify(
                {
                    "success": False,
                    "message":"Failed to add"
                }
            )
