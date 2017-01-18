from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector

from flask_bcrypt import Bcrypt
import re #for regex

app = Flask(__name__)
mysql = MySQLConnector(app,'login')

app.secret_key = 'jnsdflkas'

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
bcrypt=Bcrypt(app) 

name = re.compile(r'^[a-zA-Z]')

@app.route('/')
def index():
    print 'a'
    return render_template('index.html')

@app.route('/register', methods= ['POST'])
def register():
    print 'b'
    error = 0
    if len(request.form['first_name']) <2:
        error += 1
        flash("need more characters")
    elif not name.match(request.form['first_name']):
        error += 1
        flash("no numbers allowed in the name")
    if len(request.form['last_name']) <2:
        error += 1
        flash("need more characters")
    elif not name.match(request.form['last_name']):
        error += 1
        flash("no numbers allowed in the name")
    if not EMAIL_REGEX.match(request.form['email']):
        error += 1
        flash('email is not valid!')
    if len(request.form['password']) <9:
        error+= 1
        flash("password needs to be 9 characters!")
    if request.form['password'] != request.form['confirm']:
        error+= 1
        flash("passwords do not match!")
    if error == 0:
        hashed = bcrypt.generate_password_hash(request.form['password'])
        query = "INSERT INTO users (first_name, last_name, email, pw_hash, created_at, updated_at) VALUES (:first_name, :last_name, :email, :confirm, NOW(), NOW())"
        data = {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'email': request.form['email'],
            'confirm': hashed
        }
        mysql.query_db(query, data)
        return redirect('/login')
    return redirect('/')

@app.route('/login', methods = ['POST'])
def login():
    error = 0
    query = 'SELECT id, pw_hash FROM users WHERE email = "{}"'.format(request.form['email'])
    user = mysql.query_db(query)
    print user
    if len(user) < 1:
        flash("Email doesn't exist")
        error += 1
    elif not bcrypt.check_password_hash(user[0]['pw_hash'], request.form['password']):
        flash('Wrong password')
        error += 1
    elif error == 0:
        session['id'] = user[0]['id']
        return redirect('/login')

    return redirect('/')

@app.route('/login')
def login_info():
    return render_template('login_info.html')

app.run(debug=True)
