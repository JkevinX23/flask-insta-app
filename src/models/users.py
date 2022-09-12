from src.server.instance import db
from sqlalchemy.sql import func

class Users(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.String(36), primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    desciption = db.Column(db.Text)
    profile_url = db.Column(db.String(255))
    nickname = db.Column(db.String(255))
    created_at = db.Column(db.DateTime(timezone=False),
                           server_default=func.now())
    

    def __repr__(self):
        return f'<User {self.name}>'