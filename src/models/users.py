from src.server.instance import db, ma
from sqlalchemy.sql import func

class Users(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.String(36), primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    profile_url = db.Column(db.String(255))
    nickname = db.Column(db.String(255))
    created_at = db.Column(db.DateTime(timezone=False),
                           server_default=func.now())
    

    def __repr__(self):
        return f'<User {self.name}>'

class UserSchema(ma.Schema):
    class Meta:
        fields = ("id","name","description","profile_url", "nickname", "created_at")
user_schema = UserSchema(many = False)
users_schema = UserSchema(many = True)