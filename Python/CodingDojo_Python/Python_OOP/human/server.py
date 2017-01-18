from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector

app = Flask(__name__)
mysql = MySQLConnector(app,'email_validation')

@app.route('/') #our GET function which renders our main page index.html
def index(): #display local host
    print "a"
    query = "SELECT * FROM users"
    display = mysql.query_db(query)
    return render_template('email.html', displayAll = display) #render_template means it will go to html file and return it in the way the client can understand

@app.route('/new_user', methods=['POST']) #sending info and render it on template
def create_user():
    print "b"
    data ={
        "email": request.form["email"]
    }
    query = "INSERT users (email, created_at, updated_at) VALUES (:email, NOW(), NOW())"
    counter_dot = 0
    counter_at = 0
    for key in data.items(): #dot items does do something - is a built-in function
        for i in key[1]:
            print i
            if i == ".":
                counter_dot = counter_dot + 1
            if i == "@":
                counter_at = counter_at + 1
    print counter_at
    print counter_dot
    if counter_at != 1 or counter_dot != 1:
        print "Invalid email! Try again"
        return invalid_email()
    else:
        mysql.query_db(query, data)
    return redirect('/')

@app.route('/invalid')
def invalid_email():
    return render_template('invalid.html')
app.run(debug=True)
