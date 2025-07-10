# 🥦 [<img src="https://github.com/broccoli-cli/broccoli/blob/main/assets/broccoli-logo.png" width="50"/>](broccoli.png) broccoli
![goreport](https://goreportcard.com/badge/github.com/broccoli-cli/broccoli)
![release](https://badgen.net/github/release/broccoli-cli/broccoli)
![license](https://badgen.net/github/license/broccoli-cli/broccoli)

Real-time terminal-based chat application for Mac users

## �� Features

- ✅ User registration and login (JWT token)
- ✅ Real-time WebSocket communication
- ✅ Terminal-based chat client
- ✅ Message history stored in database
- ✅ User join/leave notifications

## 📦 Quick Setup

```bash
# Install dependencies
pip3 install -r requirements.txt

# Create .env file
echo "SECRET_KEY=your_super_secret_key_here" > .env

# Start server
python3 server.py

# Start client in new terminal
python3 terminal_client.py
```

## 💻 Usage

1. **Register** or **login**
2. **Type message** and press Enter
3. **Type `quit`** to exit

## �� API Endpoints

- `POST /register` - User registration
- `POST /login` - User login and JWT token

## �� WebSocket Events

- `connect` - Connection established
- `join` - Join chat room
- `message` - Send message
- `leave` - Leave room

## ✅ Test Results

### Successful Tests:
- ✅ User registration (`/register`)
- ✅ User login (`/login`) 
- ✅ JWT token verification
- ✅ WebSocket connection
- ✅ Real-time messaging
- ✅ Terminal client interface
- ✅ Message database storage
- ✅ Multi-user support

### �� Testing Methods:

#### **1. Basic API Tests:**
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

#### **2. Manual Multi-User Test:**
```bash
# Terminal 1: Server
python3 server.py

# Terminal 2: Client 1
python3 terminal_client.py

# Terminal 3: Client 2  
python3 terminal_client.py

# Terminal 4: Client 3
python3 terminal_client.py
```

#### **3. Automated Multi-User Test:**
```bash
# 3 users automated test (elif, sercan, lordi)
python3 test_multi_user.py
```

#### **4. Quick Test Script:**
```bash
# Automatically starts 3 clients
./quick_test.sh
```

### 📊 Test Scenarios:

#### **Scenario 1: Basic Functionality**
- ✅ User registration and login
- ✅ JWT token acquisition
- ✅ WebSocket connection
- ✅ Message sending/receiving

#### **Scenario 2: Multi-User**
- ✅ 3 users connect simultaneously (Elif, Sercan, Lordi)
- ✅ Elif sends loving messages to Sercan ❤️
- ✅ Sercan responds romantically 😊
- ✅ Lordi sends playful messages like a funny kid 😄
- ✅ Real-time communication tested
- ✅ User join/leave notifications

#### **Scenario 3: Performance Test**
- ✅ WebSocket polling works
- ✅ Message latency < 1 second
- ✅ Database records correct
- ✅ Connection drop/reconnect

### 🔍 Test Files:
- `test_multi_user.py` - Automated multi-user test
- `quick_test.sh` - Quick test script
- `terminal_client.py` - Manual test client

## 📋 To-do's:

### 🔥 Priority:
- [ ] Private messaging (DM)
- [ ] Multiple chat rooms
- [ ] File sharing
- [ ] Emoji support
- [ ] Message editing/deletion

### 🚀 Advanced:
- [ ] Friend add/remove
- [ ] User profiles
- [ ] Online status
- [ ] Message search
- [ ] Notification system

### 🎯 Social Media:
- [ ] Post sharing
- [ ] Homepage (latest/friend posts)
- [ ] Post like/dislike
- [ ] Comment system
- [ ] Hashtag support

## 📁 Project Structure

```
broccoli/
├── server.py              # Main Flask server
├── models.py              # Database models (User, Message)
├── routes.py              # API endpoints (/register, /login)
├── socket_events.py       # WebSocket event handlers
├── terminal_client.py     # Terminal chat client
├── test_multi_user.py    # Automated multi-user test
├── quick_test.sh         # Quick test script
├── requirements.txt       # Python dependencies
├── .env                  # Environment variables (SECRET_KEY)
├── proje.db             # SQLite database
├── .gitignore           # Git ignore file
├── LICENSE              # MIT License
├── README.md            # Turkish README
├── README_EN.md         # English README
└── assets/              # Project assets
    ├── broccoli-logo.png
    └── database-diagram.png
```

## 🔧 Technical Details

### Backend Stack:
- **Flask** - Web framework
- **Flask-SQLAlchemy** - Database ORM
- **Flask-SocketIO** - WebSocket support
- **PyJWT** - JWT authentication
- **SQLite** - Database
- **Eventlet** - Async server

### Frontend (Terminal):
- **Python** - Terminal client
- **SocketIO-client** - WebSocket client
- **Requests** - HTTP client

### Security:
- **JWT tokens** for authentication
- **Password hashing** with werkzeug
- **CORS enabled** for cross-origin requests

## 🚀 Development

### Running in Development:
```bash
# Install dependencies
pip3 install -r requirements.txt

# Set environment
export FLASK_ENV=development
export SECRET_KEY=your_secret_key

# Run server
python3 server.py
```

### Database Management:
```bash
# Database is auto-created on first run
# Location: proje.db (SQLite)

# Tables:
# - users (id, username, password_hash, created_at)
# - messages (id, user_id, content, timestamp)
```

## 📝 API Documentation

### Authentication Endpoints:

#### POST /register
Register a new user
```json
{
  "username": "newuser",
  "password": "password123"
}
```

#### POST /login
Login and get JWT token
```json
{
  "username": "existinguser", 
  "password": "password123"
}
```

### WebSocket Events:

#### Client → Server:
- `join` - Join chat room
- `message` - Send message
- `leave` - Leave room

#### Server → Client:
- `user_joined` - User joined notification
- `user_left` - User left notification  
- `message` - New message received

## 🐛 Troubleshooting

### Common Issues:

1. **Port 5000 already in use:**
   - Server uses port 8080 by default
   - Check if port is available

2. **JWT token errors:**
   - Ensure SECRET_KEY is set in .env
   - Check token expiration

3. **WebSocket connection failed:**
   - Verify server is running
   - Check firewall settings

4. **Database errors:**
   - Delete proje.db to reset
   - Check file permissions

## 🤝 Contributing

1. Fork the repository
2. Create feature branch
3. Make changes
4. Test thoroughly
5. Submit pull request

## 📄 License

MIT License - see LICENSE file for details

---

**Made with ❤️ for Mac users who love terminal-based applications**
