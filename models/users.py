from main import db
from sqlalchemy.sql import func
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password = db.Column(db.String(254))
    name = db.Column(db.String(125))
    premium_id = db.Column(db.Integer, db.ForeignKey('premium_status.id'), nullable=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    #favorited = db.relationship('Favorite',backref='user', lazy='dynamic')
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    def __repr__(self):
        return '<User {}>'.format(self.username)