from flask import Flask, render_template, request, redirect, session
from random import randrange
app = Flask(__name__)
app.secret_key = 'fwfonjn'#need to set a key for security purposes

def Count():
    try:
        session['counter'] += 1
    except KeyError:
        session['counter'] = 1

@app.route('/')
def getRandnum():
    Count()
    if (session['counter'] == 1):
        session['class'] = 'clear'
    if 'randomgen' not in session:
        session['randomgen'] = randrange(0,101)
    return render_template("index.html")

@app.route('/server', methods=["POST"]) #reroute to a dif place since post does not post to main route
def guess():
    if int(request.form['guess']) == session['randomgen']: #submitted in a form so will be a string, so need to convert it to integer to match randomnumber generated
        session['randomgen'] = randrange(0,101)
        session['guess']= "Good guess - you win!" 
        session['class'] = 'green'
    elif int(request.form['guess']) > session['randomgen']:
        session['guess']= "Too high!" 
        session['class'] = 'red'
    elif int(request.form['guess']) < session['randomgen']:
        session['guess']= "Too low!" 
        session['class'] = 'red'
    return redirect('/')

@app.route('/clear', methods = ['POST'])
def clear():
    session.clear()
    return redirect('/')

app.run(debug=True)
