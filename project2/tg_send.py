import requests


TOKEN = "8512052287:AAF-7LRbd7623epWoFT5K8yrLKOyT5cez1M"
CHAT_ID = "80385199"
FILE = "message.txt"


url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

with open(FILE, "r", encoding="utf-8") as f:
    text = f.read().strip()

payload = {
    "chat_id": CHAT_ID,
    "text": text,
    "parse_mode": "HTML"  
}

r = requests.post(url, data=payload)

if r.status_code == 200:
    print("Сообщение успешно отправлено в Telegram!")
else:
    print("Ошибка:", r.json())