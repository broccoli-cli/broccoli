#!/usr/bin/env python3
"""
Çoklu Kullanıcı Test Script'i
Kullanım: python3 test_multi_user.py
"""

import socketio
import requests
import json
import time
import threading
from datetime import datetime

# Sunucu bilgileri
SERVER_URL = "http://localhost:8080"
SOCKET_URL = "http://localhost:8080"

class TestUser:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.token = None
        self.sio = socketio.Client()
        self.messages_received = []
        self.setup_socket_events()
    
    def setup_socket_events(self):
        """Socket event handler'larını ayarla"""
        
        @self.sio.event
        def connect():
            print(f"✅ {self.username} bağlandı!")
            if self.token:
                self.sio.emit('join', {'token': self.token})
        
        @self.sio.event
        def disconnect():
            print(f"❌ {self.username} bağlantısı kesildi!")
        
        @self.sio.on('status')
        def on_status(data):
            print(f"📢 {self.username}: {data['message']}")
        
        @self.sio.on('new_message')
        def on_new_message(data):
            timestamp = datetime.fromisoformat(data['timestamp'].replace('Z', '+00:00'))
            time_str = timestamp.strftime('%H:%M')
            print(f"[{time_str}] {data['username']}: {data['content']}")
            self.messages_received.append(data)
        
        @self.sio.on('user_joined')
        def on_user_joined(data):
            print(f"👋 {data['username']} sohbete katıldı!")
        
        @self.sio.on('user_left')
        def on_user_left(data):
            print(f"👋 {data['username']} sohbetten ayrıldı!")
    
    def register_and_login(self):
        """Kayıt ol ve giriş yap"""
        try:
            # Kayıt ol
            response = requests.post(f"{SERVER_URL}/register", 
                                  json={'username': self.username, 'password': self.password})
            if response.status_code != 201:
                print(f"❌ {self.username} kayıt hatası")
                return False
            
            # Giriş yap
            response = requests.post(f"{SERVER_URL}/login", 
                                  json={'username': self.username, 'password': self.password})
            if response.status_code == 200:
                data = response.json()
                self.token = data['token']
                print(f"✅ {self.username} giriş başarılı!")
                return True
            else:
                print(f"❌ {self.username} giriş hatası")
                return False
                
        except requests.exceptions.ConnectionError:
            print(f"❌ {self.username} sunucuya bağlanılamıyor!")
            return False
    
    def connect_to_chat(self):
        """Chat'e bağlan"""
        try:
            self.sio.connect(SOCKET_URL)
            return True
        except Exception as e:
            print(f"❌ {self.username} WebSocket hatası: {e}")
            return False
    
    def send_message(self, content):
        """Mesaj gönder"""
        if self.token and self.sio.connected:
            self.sio.emit('message', {'token': self.token, 'content': content})
            print(f"💬 {self.username}: {content}")
        else:
            print(f"❌ {self.username} bağlantı yok!")
    
    def disconnect(self):
        """Bağlantıyı kes"""
        if self.sio.connected:
            self.sio.disconnect()

def run_user_test(user, messages, delay=2):
    """Kullanıcı testini çalıştır"""
    if not user.register_and_login():
        return
    
    if not user.connect_to_chat():
        return
    
    time.sleep(delay)  # Bağlantı için bekle
    
    # Mesajları gönder
    for i, message in enumerate(messages):
        user.send_message(message)
        time.sleep(1)  # Mesajlar arası bekle
    
    time.sleep(3)  # Son mesajların gelmesini bekle
    user.disconnect()

def main():
    """Ana test fonksiyonu"""
    print("🧪 Çoklu Kullanıcı Test Başlıyor...")
    print("=" * 50)
    
    # Test kullanıcıları
    users = [
        TestUser("elif", "pass123"),
        TestUser("sercan", "pass456"),
        TestUser("lordi", "pass789")
    ]
    
    # Her kullanıcının mesajları
    user_messages = [
        ["Merhaba Sercan! ❤️", "Seni çok seviyorum!", "Bugün nasılsın canım?"],
        ["Selam Elif! 😊", "Ben de seni seviyorum!", "Hava çok güzel bugün"],
        ["Herkese selam! 😄", "Ben Lordi, şakacı bir çocuğum!", "Haha, ne güzel sohbet bu!"]
    ]
    
    # Thread'ler oluştur
    threads = []
    for i, (user, messages) in enumerate(zip(users, user_messages)):
        thread = threading.Thread(
            target=run_user_test, 
            args=(user, messages, i * 2)  # Her kullanıcı 2 saniye arayla başlasın
        )
        threads.append(thread)
    
    # Thread'leri başlat
    for thread in threads:
        thread.start()
    
    # Tüm thread'lerin bitmesini bekle
    for thread in threads:
        thread.join()
    
    print("\n🎉 Test tamamlandı!")
    print("=" * 50)
    
    # Sonuçları göster
    for user in users:
        print(f"📊 {user.username}: {len(user.messages_received)} mesaj aldı")

if __name__ == "__main__":
    main() 