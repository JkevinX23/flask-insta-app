import os
from flask import Flask
from flask_restx import Api
from werkzeug.middleware.proxy_fix import ProxyFix
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
MIGRATION_DIR = os.path.join('src', 'database', 'migrations')

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)
api = Api(app,
    version='0.1', 
    title='instaApp', 
    description='Instagram clone', 
    doc='/docs'
)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_STRING_CONNECTION')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db, directory=MIGRATION_DIR)
