from flask import Blueprint, render_template, request

auth = Blueprint('auth', __name__)

# Login
@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form
    return render_template('login.html', text="Testing", boolean=True) # Use Jinja templating to access 'text' value in login.html

# Logout
@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

# Signup
@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    return render_template('sign_up.html')