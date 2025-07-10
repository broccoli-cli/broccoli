import os
from dotenv import load_dotenv
from flask import Flask
from models import db
from routes import init_routes

# ---KURULUM ---

# .env dosyasını yükle
load_dotenv()

# Projenin çalıştığı dizinde veritabanı dosyasını oluştur
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

# Veritabanı yapılandırması: SQLite veritabanı 'proje.db' adıyla oluşturulacak.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'proje.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # Performans için

# SECRET_KEY'i .env dosyasından oku, yoksa hata ver
secret_key = os.getenv('SECRET_KEY')
if not secret_key:
    raise ValueError("SECRET_KEY environment variable is required. Please create a .env file with SECRET_KEY=your_secret_key")
app.config['SECRET_KEY'] = secret_key

# Veritabanını uygulamaya bağla
db.init_app(app)

# API endpoint'lerini kaydet
init_routes(app)

# --- SUNUCUYU BAŞLAT ---

if __name__ == '__main__':
    
    with app.app_context():
        db.create_all()
        
    app.run(host='0.0.0.0', port=8080, debug=True) 