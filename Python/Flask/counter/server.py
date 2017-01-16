from flask import Flask, render_template, request, redirect, session
from random import randrange
app = Flask(__name__)
app.secret_key = 'fwfonjn'#need to set a key for security purposes

# called from every route, keeps a record of how many pages/routes loaded
def rand_generator():
        session['randomgen'] = randrange(0,101)
    
@app.route('/')
def index():
    if 'randomgen' not in session:
        session['randomgen'] = 0
    if
    return render_template("index.html") 


















@app.route('/Add2')
def Add2():
    session['counter'] += 2
    return render_template("index.html") 

@app.route('/resetSession')
def resetSession():
    #session.clear()
    session["counter"] = 0
    return render_template("index.html")

app.run(debug=True)
