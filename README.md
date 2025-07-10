
# [<img src="https://github.com/broccoli-cli/broccoli/blob/main/assets/broccoli-logo.png" width="50"/>](broccoli.png) broccoli
![goreport](https://goreportcard.com/badge/github.com/broccoli-cli/broccoli)
![release](https://badgen.net/github/release/broccoli-cli/broccoli)
![license](https://badgen.net/github/license/broccoli-cli/broccoli)

Terminal tabanlı gerçek zamanlı chat uygulaması - Mac kullanıcıları için

## 🚀 Özellikler

- ✅ Kullanıcı kaydı ve girişi (JWT token)
- ✅ Gerçek zamanlı WebSocket iletişimi
- ✅ Terminal tabanlı chat client
- ✅ Mesaj geçmişi veritabanında saklanır
- ✅ Kullanıcı giriş/çıkış bildirimleri

## 📦 Hızlı Kurulum

```bash
# Bağımlılıkları yükle
pip3 install -r requirements.txt

# .env dosyası oluştur
echo "SECRET_KEY=your_super_secret_key_here" > .env

# Sunucuyu başlat
python3 server.py

# Yeni terminal'de client'ı başlat
python3 terminal_client.py
```

## 💻 Kullanım

1. **Kayıt ol** veya **giriş yap**
2. **Mesaj yaz** ve Enter'a bas
3. **Çıkmak için** `quit` yaz

## 🔧 API Endpoints

- `POST /register` - Kullanıcı kaydı
- `POST /login` - Kullanıcı girişi ve JWT token

## 🔌 WebSocket Events

- `connect` - Bağlantı kuruldu
- `join` - Chat odasına katılma
- `message` - Mesaj gönderme
- `leave` - Odadan ayrılma

## ✅ Test Sonuçları

### Başarılı Testler:
- ✅ Kullanıcı kaydı (`/register`)
- ✅ Kullanıcı girişi (`/login`) 
- ✅ JWT token doğrulama
- ✅ WebSocket bağlantısı
- ✅ Gerçek zamanlı mesajlaşma
- ✅ Terminal client arayüzü
- ✅ Mesaj veritabanına kaydetme

### Test Komutları:
```bash
# Register test
curl -X POST http://localhost:8080/register \
  -H "Content-Type: application/json" \
  -d '{"username": "testuser", "password": "testpass123"}'

# Login test  
curl -X POST http://localhost:8080/login \
  -H "Content-Type: application/json" \
  -d '{"username": "testuser", "password": "testpass123"}'
```

## 📋 Gelecek Özellikler (to-do's):

### 🔥 Öncelikli:
- [ ] Özel mesajlaşma (DM)
- [ ] Çoklu chat odaları
- [ ] Dosya paylaşımı
- [ ] Emoji desteği
- [ ] Mesaj düzenleme/silme

### 🚀 Gelişmiş:
- [ ] Arkadaş ekleme/çıkarma
- [ ] Kullanıcı profilleri
- [ ] Çevrimiçi durumu
- [ ] Mesaj arama
- [ ] Bildirim sistemi

### 🎯 Sosyal Medya:
- [ ] Post paylaşma
- [ ] Ana sayfa (son/friend postları)
- [ ] Post beğenme/beğenmeme
- [ ] Yorum sistemi
- [ ] Hashtag desteği

## 📁 Proje Yapısı

```
broccoli/
├── server.py              # Ana sunucu (Flask + SocketIO)
├── models.py              # Veritabanı modelleri (User, Message)
├── routes.py              # API endpoint'leri
├── socket_events.py       # WebSocket event handler'ları
├── terminal_client.py     # Terminal chat client
├── requirements.txt       # Tüm bağımlılıklar
└── proje.db              # SQLite veritabanı
```

## database struct:
![license](https://github.com/broccoli-cli/broccoli/blob/main/assets/database-diagram.png)
