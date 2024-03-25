# Roots for the website; where can users actually go?

from flask import Blueprint, render_template

# A Blueprint is a collection of URLs for each root
# Each Blueprint needs to be registered in __init__.py
views = Blueprint('views', __name__)

# Homepage
@views.route('/') # URL goes here
def home(): # This function will run whenever we go to the url specified above
    return render_template('home.html')