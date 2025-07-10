from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    """Kullanıcı bilgilerini tutan model."""
    id = db.Column(db.Integer, primary_key=True) # Her kullanıcı için benzersiz ID
    username = db.Column(db.String(80), unique=True, nullable=False) # Benzersiz ve zorunlu kullanıcı adı
    password_hash = db.Column(db.String(256), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

class Message(db.Model):
    """Chat mesajlarını tutan model."""
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('messages', lazy=True))

    def __repr__(self):
        return f'<Message {self.id} by {self.user.username}>' 