
# 🥦 [<img src="https://github.com/broccoli-cli/broccoli/blob/main/assets/broccoli-logo.png" width="50"/>](broccoli.png) broccoli
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
- ✅ Çoklu kullanıcı desteği

### 🧪 Test Yöntemleri:

#### **1. Temel API Testleri:**
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

#### **2. Manuel Çoklu Kullanıcı Testi:**
```bash
# Terminal 1: Sunucu
python3 server.py

# Terminal 2: Client 1
python3 terminal_client.py

# Terminal 3: Client 2  
python3 terminal_client.py

# Terminal 4: Client 3
python3 terminal_client.py
```

#### **3. Otomatik Çoklu Kullanıcı Testi:**
```bash
# 3 kullanıcı otomatik test (elif, sercan, lordi)
python3 test_multi_user.py
```

#### **4. Hızlı Test Script'i:**
```bash
# 3 client otomatik başlatır
./quick_test.sh
```

### 📊 Test Senaryoları:

#### **Senaryo 1: Temel İşlevsellik**
- ✅ Kullanıcı kaydı ve girişi
- ✅ JWT token alımı
- ✅ WebSocket bağlantısı
- ✅ Mesaj gönderme/alma

#### **Senaryo 2: Çoklu Kullanıcı**
- ✅ 3 kullanıcı aynı anda bağlanır
- ✅ Her kullanıcı farklı mesajlar gönderir
- ✅ Gerçek zamanlı iletişim test edilir
- ✅ Kullanıcı giriş/çıkış bildirimleri

#### **Senaryo 3: Performans Testi**
- ✅ WebSocket polling çalışıyor
- ✅ Mesaj gecikmesi < 1 saniye
- ✅ Veritabanı kayıtları doğru
- ✅ Bağlantı kopma/yeniden bağlanma

### 🔍 Test Dosyaları:
- `test_multi_user.py` - Otomatik çoklu kullanıcı testi
- `quick_test.sh` - Hızlı test script'i
- `terminal_client.py` - Manuel test client'ı

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
