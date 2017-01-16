from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'friendsdb')

@app.route('/') #our GET function which renders our main page index.html
def index(): #display local host
    print "a"
    query = ("SELECT * FROM friends")
    friends = mysql.query_db(query)
    return render_template('index.html', all_friends=friends)

@app.route('/friends', methods=['POST']) #POST since creating a friend 
def create():
    print "b"
    query = "INSERT friends (first_name, last_name, occupation, created_at, updated_at) VALUES (:first_name, :last_name, :occupation, NOW(), NOW())"

    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'occupation': request.form['occupation']
    }
    mysql.query_db(query, data)
    return redirect('/')

@app.route('/friends/<friend_id>') #GET function to display a single friend at a time
def show(friend_id):
    print "c"
    query = "SELECT * FROM friends WHERE id = :specific_id" #copied and pasted the specific_id - it is the value in the id table
    data = {'specific_id': friend_id}
    friends = mysql.query_db(query, data)
    return render_template('index.html', one_friend=friends[0])

@app.route('/update_friend/<friend_id>', methods=['POST']) #POST function for updating our friends
def update(friend_id):
    print "d"
    query = """UPDATE friends 
             SET first_name = :first_name, last_name = :last_name, occupation = :occupation 
             WHERE id = :id"""
    data = {
        'first_name': request.form['first_name'],
        'last_name':  request.form['last_name'],
        'occupation': request.form['occupation'],
        'id': friend_id
           }
    mysql.query_db(query, data)
    return redirect('/show_update/'+ friend_id) #redirecting to a different function (not a different page)

@app.route('/show_update/<friend_id>') #new route to display the update
def display_update(friend_id):
    print "e"
    query = "SELECT * FROM friends WHERE id = :specific_id" 
    data = {'specific_id': friend_id}
    friends = mysql.query_db(query, data)
    return render_template('update_friend.html', update_friend=friends[0], friend_id=friend_id)

@app.route('/remove_friend/<friend_id>', methods=['POST'])
def delete(friend_id):
    print "f"
    query = "DELETE FROM friends WHERE id = :id"
    data = {'id': friend_id}
    mysql.query_db(query, data)
    return redirect('/')


app.run(debug=True)
