from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
#index route will handle rendering out form
@app.route('/')
def index():
    return render_template("index.html")
#this route will handle our form submission
#notice how we defined which HTTP methods are allowed byt his route
@app.route('/users', methods=['POST'])
def create_user():
    return render_template("user.html",
    name = request.form['name'],
    email = request.form['email'],
    female = request.form['gender'],
    male = request.form['gender'],
    other = request.form['gender'],
    subscribe = request.form['subscribe'])
    #redirecting back to the '/'route
    return redirect#changed from '/' to allow us to go to the page that displays the name, email, etc

@app.route('/show')
def show_user():
    return render_template('user.html', name = session['name'], email =session['email'], female=session['gender'], male=session['gender'], other=session['gender'], subscribe=session['subscribe'])
app.run(debug=True)