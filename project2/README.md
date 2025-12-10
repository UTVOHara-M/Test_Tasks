### README.md для Бота

# Telegram Message Sender

## Установка
```bash
pip install requests
```
## Настройка
В файле tg_send.py замени:
```python
BOT_TOKEN = 'твой_токен_от_BotFather'
CHAT_ID   = 'твой_chat_id'
```

## Использование
```python
tg_send.py message.txt
```
Содержимое файла message.txt будет отправлено в указанный чат.
