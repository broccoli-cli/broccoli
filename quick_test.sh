#!/bin/bash

echo "🧪 Hızlı Çoklu Kullanıcı Test"
echo "================================"

# Terminal 1'de sunucu çalışıyor, şimdi client'ları test edelim

echo "1️⃣ Elif kullanıcısını test ediyoruz..."
python3 terminal_client.py &
ELIF_PID=$!

sleep 5

echo "2️⃣ Sercan kullanıcısını test ediyoruz..."
python3 terminal_client.py &
SERCAN_PID=$!

sleep 5

echo "3️⃣ Lordi kullanıcısını test ediyoruz..."
python3 terminal_client.py &
LORDI_PID=$!

echo "✅ 3 kullanıcı da başlatıldı!"
echo "📝 Her terminal'de farklı kullanıcı adıyla giriş yapın:"
echo "   - Terminal 1: elif"
echo "   - Terminal 2: sercan" 
echo "   - Terminal 3: lordi"
echo ""
echo "🔄 Test bitince Ctrl+C ile durdurun"

# Test süresince bekle
sleep 30

echo "🧹 Test client'larını temizliyoruz..."
kill $ELIF_PID $SERCAN_PID $LORDI_PID 2>/dev/null

echo "✅ Test tamamlandı!" 