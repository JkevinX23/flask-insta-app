from src.server.instance import db
from sqlalchemy.sql import func

class Followers(db.Model):
    __tablename__ = 'followers'

    follower_id = db.Column(db.String(36), db.ForeignKey('users.id'), primary_key=True)
    followee_id = db.Column(db.String(36), db.ForeignKey('users.id'), primary_key=True)
    created_at = db.Column(db.DateTime(timezone=False),
                           server_default=func.now(), nullable=False)
    def __repr__(self):
        return f'<Followers {self.follower_id} | { self.followee_id}>'