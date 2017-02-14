from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'isfjkasnv;jnv23gs5'#need to set a key for security purposes

# called from every route, keeps a record of how many pages/routes loaded
def pageCounter():
    print 'a'
    resetSession()
    session['counter'] += 1
    
@app.route('/')
def index():
    print 'b'
    pageCounter()
    #this route will handle our form submission 
    return render_template("index.html") 

@app.route('/Add2') 
def Add2(): #counts by 2
    print 'c'
    session['counter'] += 2
    return render_template("index.html") 

@app.route('/resetSession')
def resetSession():
    print 'd'
    session["counter"] = 1
    return render_template("index.html")

app.run(debug=True)
