from src.server.instance import db
from sqlalchemy.sql import func

class Photos(db.Model):
    __tablename__ = 'photos'

    id = db.Column(db.String(36), primary_key=True)
    url = db.Column(db.String(255), nullable = False)
    post_id = db.Column(db.String(36), db.ForeignKey('posts.id'), nullable = False)
    created_at = db.Column(db.DateTime(timezone=False),
                           server_default=func.now(), nullable=False)
    def __repr__(self):
        return f'<Photos {self.id}>'