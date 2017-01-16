
from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')

def landing():
    return render_template("landing_index.html")

@app.route('/ninjas')
 
def ninja():
    return render_template("ninjas.html")

@app.route('/dojo/new')

def dojoes():
    return render_template("dojo.html")


app.run(debug=True)