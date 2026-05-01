import os
import socket
from flask import Flask, render_template

app = Flask(__name__)

# --- Munish Hacker Tool Setup ---
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
    \033[1;34m[+] Tool Name: Munish Hacker v1.0
    \033[1;37m------------------------------------------------------------
    \033[1;33m[*] Starting Stealth Server on Port 8080...
    \033[1;33m[*] Send the Ngrok/Cloudflare link to target.
    \033[1;37m------------------------------------------------------------
    \033[0m
    """)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    banner()
    # 0.0.0.0 का मतलब है यह लोकल नेटवर्क और क्लाउड (Cloudflared/Ngrok) दोनों पर चलेगा
    app.run(host='0.0.0.0', port=8080, debug=False)
