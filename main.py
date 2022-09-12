from src.server.instance import *

from src.controllers.users.routes import *
from src.models.users import *
from src.models.followers import *
from src.models.posts import *
from src.models.photos import *

if __name__ == "__main__":
    app.run(debug=True)