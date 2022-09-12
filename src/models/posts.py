from src.server.instance import db
from sqlalchemy.sql import func

class Posts(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.String(36), primary_key=True)
    description = db.Column(db.Text)
    author_id = db.Column(db.String(36), db.ForeignKey('users.id'), nullable = False)
    created_at = db.Column(db.DateTime(timezone=False),
                           server_default=func.now(), nullable=False)
    def __repr__(self):
        return f'<Posts {self.name}>'