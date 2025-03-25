from flask import flask, render_template, request, redirect, url_for # type: ignore

app = flask(__name__)

# Mock user data
users = {
    "admin": "password123",
    "user": "mypassword"
}

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username in users and users[username] == password:
            return f"Welcome, {username}!"
        else:
            return "Invalid credentials. Please try again."
    return '''
        <form method="post">
            <label for="username">Username:</label>
            <input type="text" id="username" name="username" required><br>
            <label for="password">Password:</label>
            <input type="password" id="password" name="password" required><br>
            <button type="submit">Login</button>
        </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)

  #teste  
