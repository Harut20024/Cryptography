from flask import Flask, request, redirect, session

app = Flask(__name__)
app.secret_key = 'secret'
users = {}

def html_page(content):
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Login/Register</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background: #f4f4f4;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                height: 100vh;
            }}
            form {{
                background: white;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 0 10px rgba(0,0,0,0.1);
            }}
            input {{
                margin: 5px 0;
                padding: 10px;
                width: 100%;
            }}
            button {{
                padding: 10px;
                width: 100%;
                background-color: #3498db;
                color: white;
                border: none;
                border-radius: 5px;
            }}
            a {{
                display: block;
                margin-top: 10px;
                text-align: center;
            }}
        </style>
    </head>
    <body>
        {content}
    </body>
    </html>
    """

@app.route('/')
def home():
    if 'user' in session:
        return html_page(f"<h2>Welcome, {session['user']}!</h2><a href='/logout'>Logout</a>")
    return redirect('/login')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users:
            return html_page("<h3>Username already exists</h3><a href='/register'>Try again</a>")
        users[username] = password
        return redirect('/login')
    return html_page("""
        <h2>Register</h2>
        <form method="post">
            <input name="username" placeholder="Username" required><br>
            <input name="password" type="password" placeholder="Password" required><br>
            <button type="submit">Register</button>
        </form>
        <a href="/login">Already have an account?</a>
    """)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if users.get(username) == password:
            session['user'] = username
            return redirect('/')
        return html_page("<h3>Invalid credentials</h3><a href='/login'>Try again</a>")
    return html_page("""
        <h2>Login</h2>
        <form method="post">
            <input name="username" placeholder="Username" required><br>
            <input name="password" type="password" placeholder="Password" required><br>
            <button type="submit">Login</button>
        </form>
        <a href="/register">Don't have an account?</a>
    """)

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/login')

if __name__ == '__main__':
    app.run(port=8000)

