from flask_socketio import emit, join_room, leave_room
from flask import request
from models import db, User, Message
from datetime import datetime
import jwt

def init_socket_events(socketio, app):
    """WebSocket event handler'larını başlat"""
    
    @socketio.on('connect')
    def handle_connect():
        """Kullanıcı bağlandığında"""
        print(f"Client connected: {request.sid}")
        emit('status', {'message': 'Connected to chat server'})

    @socketio.on('disconnect')
    def handle_disconnect():
        """Kullanıcı ayrıldığında"""
        print(f"Client disconnected: {request.sid}")

    @socketio.on('join')
    def handle_join(data):
        """Kullanıcı chat odasına katıldığında"""
        token = data.get('token')
        if not token:
            emit('error', {'message': 'Authentication required'})
            return
        
        try:
            # JWT token'ı doğrula
            payload = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
            user_id = payload['sub']
            user = User.query.get(user_id)
            
            if not user:
                emit('error', {'message': 'User not found'})
                return
            
            # Kullanıcıyı genel chat odasına ekle
            join_room('general')
            emit('status', {'message': f'Welcome {user.username}!'})
            emit('user_joined', {'username': user.username}, room='general')
            
        except jwt.ExpiredSignatureError:
            emit('error', {'message': 'Token expired'})
        except jwt.InvalidTokenError:
            emit('error', {'message': 'Invalid token'})

    @socketio.on('message')
    def handle_message(data):
        """Yeni mesaj geldiğinde"""
        token = data.get('token')
        content = data.get('content')
        
        if not token or not content:
            emit('error', {'message': 'Token and content required'})
            return
        
        try:
            # JWT token'ı doğrula
            payload = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
            user_id = payload['sub']
            user = User.query.get(user_id)
            
            if not user:
                emit('error', {'message': 'User not found'})
                return
            
            # Mesajı veritabanına kaydet
            message = Message(content=content, user_id=user_id)
            db.session.add(message)
            db.session.commit()
            
            # Mesajı tüm kullanıcılara gönder
            message_data = {
                'id': message.id,
                'content': message.content,
                'username': user.username,
                'timestamp': message.timestamp.isoformat()
            }
            emit('new_message', message_data, room='general')
            
        except jwt.ExpiredSignatureError:
            emit('error', {'message': 'Token expired'})
        except jwt.InvalidTokenError:
            emit('error', {'message': 'Invalid token'})

    @socketio.on('leave')
    def handle_leave(data):
        """Kullanıcı odadan ayrıldığında"""
        token = data.get('token')
        if not token:
            return
        
        try:
            payload = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
            user_id = payload['sub']
            user = User.query.get(user_id)
            
            if user:
                leave_room('general')
                emit('user_left', {'username': user.username}, room='general')
                
        except (jwt.ExpiredSignatureError, jwt.InvalidTokenError):
            pass 