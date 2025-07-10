import jwt
from datetime import datetime, timedelta, timezone
from flask import request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User

def init_routes(app):
    """API endpoint'lerini uygulamaya kaydet"""
    
    @app.route('/register', methods=['POST'])
    def register():
        data = request.get_json()
        if not data or not data.get('username') or not data.get('password'):
            return jsonify({'error': 'Kullanıcı adı ve şifre gereklidir'}), 400
        
        if User.query.filter_by(username=data['username']).first():
            return jsonify({'error': 'Bu kullanıcı adı zaten kullanılıyor'}), 409
        
        hashed_password = generate_password_hash(data['password'], method='pbkdf2:sha256')
        new_user = User(username=data['username'], password_hash=hashed_password)
        
        db.session.add(new_user)
        db.session.commit()
        
        return jsonify({'message': f"Kullanıcı '{data['username']}' başarıyla oluşturuldu!"}), 201

    @app.route('/login', methods=['POST'])
    def login():
        """Kullanıcı girişi yapar ve JWT döndürür."""
        # 1. İstemciden gelen JSON verisini al
        auth = request.get_json()

        # 2. Veri kontrolü
        if not auth or not auth.get('username') or not auth.get('password'):
            return jsonify({'message': 'Giriş yapılamadı: Eksik bilgi.'}), 401 # 401: Unauthorized (Yetkisiz)

        # 3. Kullanıcıyı veritabanında bul
        user = User.query.filter_by(username=auth.get('username')).first()

        # 4. Kullanıcı var mı VE şifre doğru mu kontrol et
        # check_password_hash, gönderilen şifre ile veritabanındaki hash'i güvenli bir şekilde karşılaştır :)
        if not user or not check_password_hash(user.password_hash, auth.get('password')):
            return jsonify({'message': 'Giriş yapılamadı: Hatalı kullanıcı adı veya şifre.'}), 401
        
        # 5. Şifre doğruysa, bir JWT oluştur.
        # Token'ın payload'ı
        payload = {
            'sub': user.id,
            'iat': datetime.now(timezone.utc),
            'exp': datetime.now(timezone.utc) + timedelta(hours=24)
        }
        
        # Token'ı SECRET_KEY ile imzala
        token = jwt.encode(payload, app.config['SECRET_KEY'], algorithm='HS256')

        # 6. Token'ı istemciye gönder
        return jsonify({'token': token}) 