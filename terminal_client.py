#!/usr/bin/env python3
"""
Terminal Chat Client for Mac
Kullanım: python3 terminal_client.py
"""

import socketio
import requests
import json
import sys
import os
from datetime import datetime
import threading
import time

# Sunucu bilgileri
SERVER_URL = "http://localhost:8080"
SOCKET_URL = "http://localhost:8080"

class TerminalChatClient:
    def __init__(self):
        self.sio = socketio.Client()
        self.token = None
        self.username = None
        self.setup_socket_events()
    
    def setup_socket_events(self):
        """Socket event handler'larını ayarla"""
        
        @self.sio.event
        def connect():
            print("✅ Sunucuya bağlandı!")
            if self.token:
                self.sio.emit('join', {'token': self.token})
        
        @self.sio.event
        def disconnect():
            print("\n❌ Sunucu bağlantısı kesildi!")
        
        @self.sio.on('status')
        def on_status(data):
            print(f"\n📢 {data['message']}")
        
        @self.sio.on('new_message')
        def on_new_message(data):
            timestamp = datetime.fromisoformat(data['timestamp'].replace('Z', '+00:00'))
            time_str = timestamp.strftime('%H:%M')
            print(f"\n[{time_str}] {data['username']}: {data['content']}")
        
        @self.sio.on('user_joined')
        def on_user_joined(data):
            print(f"\n👋 {data['username']} sohbete katıldı!")
        
        @self.sio.on('user_left')
        def on_user_left(data):
            print(f"\n👋 {data['username']} sohbetten ayrıldı!")
        
        @self.sio.on('error')
        def on_error(data):
            print(f"\n❌ Hata: {data['message']}")
    
    def register(self, username, password):
        """Kullanıcı kaydı"""
        try:
            response = requests.post(f"{SERVER_URL}/register", 
                                  json={'username': username, 'password': password})
            if response.status_code == 201:
                print("✅ Kayıt başarılı!")
                return True
            else:
                data = response.json()
                print(f"❌ Kayıt hatası: {data.get('error', 'Bilinmeyen hata')}")
                return False
        except requests.exceptions.ConnectionError:
            print("❌ Sunucuya bağlanılamıyor!")
            return False
    
    def login(self, username, password):
        """Kullanıcı girişi"""
        try:
            response = requests.post(f"{SERVER_URL}/login", 
                                  json={'username': username, 'password': password})
            if response.status_code == 200:
                data = response.json()
                self.token = data['token']
                self.username = username
                print("✅ Giriş başarılı!")
                return True
            else:
                data = response.json()
                print(f"❌ Giriş hatası: {data.get('message', 'Bilinmeyen hata')}")
                return False
        except requests.exceptions.ConnectionError:
            print("❌ Sunucuya bağlanılamıyor!")
            return False
    
    def connect_to_chat(self):
        """Chat sunucusuna bağlan"""
        try:
            self.sio.connect(SOCKET_URL)
            return True
        except Exception as e:
            print(f"❌ WebSocket bağlantı hatası: {e}")
            return False
    
    def send_message(self, content):
        """Mesaj gönder"""
        if self.token and self.sio.connected:
            self.sio.emit('message', {'token': self.token, 'content': content})
        else:
            print("❌ Bağlantı yok!")
    
    def start_chat(self):
        """Chat'i başlat"""
        print("\n💬 Terminal Chat'e Hoş Geldiniz!")
        print("=" * 50)
        
        # Kullanıcı girişi
        while True:
            choice = input("\n1. Giriş Yap\n2. Kayıt Ol\nSeçiminiz (1/2): ").strip()
            
            if choice == "1":
                username = input("Kullanıcı adı: ").strip()
                password = input("Şifre: ").strip()
                
                if self.login(username, password):
                    break
            elif choice == "2":
                username = input("Kullanıcı adı: ").strip()
                password = input("Şifre: ").strip()
                
                if self.register(username, password):
                    if self.login(username, password):
                        break
            else:
                print("❌ Geçersiz seçim!")
        
        # Chat sunucusuna bağlan
        if not self.connect_to_chat():
            return
        
        print(f"\n🎉 {self.username} olarak sohbete katıldınız!")
        print("Mesaj göndermek için yazın, çıkmak için 'quit' yazın.")
        print("-" * 50)
        
        # Mesaj gönderme döngüsü
        try:
            while True:
                message = input().strip()
                
                if message.lower() == 'quit':
                    break
                elif message:
                    self.send_message(message)
                
        except KeyboardInterrupt:
            print("\n👋 Görüşürüz!")
        finally:
            if self.sio.connected:
                self.sio.disconnect()

def main():
    """Ana fonksiyon"""
    client = TerminalChatClient()
    client.start_chat()

if __name__ == "__main__":
    main() 