# FLASK Tutorial 1 -- We show the bare bones code to get an app up and running

# imports
import os                 # os is used to get environment variables IP & PORT
from flask import Flask,request,redirect,url_for   # Flask is the web app that we will customize
from flask import render_template
from database import db

app = Flask(__name__)     # create an app

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flask_note_app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
db.init_app(app)

with app.app_context():
    db.create_all() 

notes = {1: {'title': 'First_note', 'text': 'This is my first note', 'date': '10-1-2020'},
         2: {'title': 'Second_note', 'text': 'This is my second note', 'date': '10-2-2020'},
         3: {'title': 'Third_note', 'text': 'This is my third note', 'date': '10-3-2020'}
         }

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
    a_user = {'name': 'Varun', 'email': 'mogli@uncc.edu'}
    return render_template('notes.html', notes=notes,user = a_user)

@app.route('/notes/new', methods=['GET','POST'])
def new_note():

    a_user = {'name':'Mogli', 'email':'mogli@uncc.edu'}

    if request.method == 'POST':
        title = request.form['title']
        text = request.form['noteText']
        from datetime import date
        today = date.today()
        today = today.strftime("%m-%d-%Y")
        id = len(notes)+1
        notes[id] = {'title':title, 'text':text, 'date':today}
        return redirect(url_for('get_notes'))
    else:
        return render_template('new.html', user=a_user)

@app.route('/notes/<note_id>')
def get_note(note_id):
    a_user = {'name':'Mogli', 'email':'mogli@uncc.edu'}

    return render_template('note.html', note=notes[int(note_id)], user = a_user)

@app.route('/user/<username>')
def get_user(username):
    return "The user is " + str(username)

app.run(host=os.getenv('IP', '127.0.0.1'),port=int(os.getenv('PORT', 5000)),debug=True)
