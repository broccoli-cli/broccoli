from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    """Kullanıcı bilgilerini tutan model."""
    id = db.Column(db.Integer, primary_key=True) # Her kullanıcı için benzersiz ID
    username = db.Column(db.String(80), unique=True, nullable=False) # Benzersiz ve zorunlu kullanıcı adı
    password_hash = db.Column(db.String(256), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>' 