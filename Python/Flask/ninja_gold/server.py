from flask import Flask, render_template, request, redirect, session
from random import randint
app = Flask(__name__)
app.secret_key = 'fwfonjn'#need to set a key for security purposes

@app.route('/')
def index():
    if 'gold' not in session:
        session['gold'] = 0
    if 'activities' not in session:
        session['activities'] = []
    return render_template('index.html')

@app.route('/process_money', methods = ['POST'])
def process():
    buildings = {
        'farm': randint (10, 21),
        'cave': randint (5, 11),
        'house': randint (2,6),
        'casino': randint (0, 51),
    }
    if request.form['building'] in buildings:
        result = buildings[request.form['building']]
        session['gold'] = session['gold'] + result
        result_dictionary = {
            'class': "green" if result > 0 else "red",
            'activity': "You went to the {} and {} {} gold!".format(request.form['building'], ('lost', 'gained', [result>0]), result)
        }
        session['activities'].append(result_dictionary)
    return redirect('/')

def clear():
    session.clear()
    # return redirect('/')

# def getRandnum():
#     if 'randomgen' not in session:
#         session['randomgen'] = randrange(0,101)
#     return render_template("index.html")

# @app.route('/server', methods=["POST"]) #reroute to a dif place since post does not post to main route
# def guess():
#     session['guess']= int(request.form['guess']) #submitted in a form so will be a string, so need to convert it to integer to match randomnumber generated
#     return redirect('/')

# @app.route('/clear', methods = ['POST'])
# def clear():
#     session['randomgen'] = randrange(0,101)
#     return redirect('/')

app.run(debug=True)
