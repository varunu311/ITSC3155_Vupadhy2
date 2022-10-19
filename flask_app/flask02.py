# FLASK Tutorial 1 -- We show the bare bones code to get an app up and running

# imports
import os                 # os is used to get environment variables IP & PORT
from flask import Flask   # Flask is the web app that we will customize
from flask import render_template

app = Flask(__name__)     # create an app

# @app.route is a decorator. It gives the function "index" special powers.
# In this case it makes it so anyone going to "your-url/" makes this function
# get called. What it returns is what is shown as the web page
@app.route('/')
@app.route('/index')
def index():
    a_user = {'name': 'Varun', 'email': 'mogli@uncc.edu'}
    return render_template('index.html', user = a_user)
@app.route('/notes')
def get_notes():
    notes = {1: {'title':'First_note', 'text':'This is my first note', 'date':'10-1-2020'},
             2: {'title':'Second_note', 'text':'This is my second note', 'date':'10-2-2020'}
             }
    return render_template('notes.html', notes=notes)
@app.route('/user/<username>')
def get_user(username):
    return "The user is " + str(username)

app.run(host=os.getenv('IP', '127.0.0.1'),port=int(os.getenv('PORT', 5000)),debug=True)
