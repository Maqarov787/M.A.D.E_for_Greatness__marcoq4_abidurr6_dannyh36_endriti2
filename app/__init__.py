'''
Marco, Abidur, Danny, Endrit
M.A.D.E for Greatness
SoftDev
P04
Time spent: 50 hours
Target Ship Date: 2025-04-21
'''


import os
from flask import Flask
from flask import render_template
from flask import request
from flask import session
from flask import redirect
import myanimedb as db
import json

app = Flask(__name__)
secret = os.urandom(32)
app.secret_key = secret

def checkUser(username):
    user = db.getUserName(username)
    if user is None:
        return False
    return user[0] == username

def checkPassword(username, password):
    pw = db.getPassword(username)
    if pw is None:
        return False
    return pw[0] == password

@app.route("/", methods=['GET', 'POST'])
def main():
    if 'username' in session.keys():
        user = json.dumps(session['username'])
        return render_template("main.html", user = user)
    else:
        return render_template("main.html")

@app.route("/filter", methods=['GET', 'POST'])
def filter():
    if 'username' in session.keys():
        user = json.dumps(session['username'])
        return render_template("filter.html", user=user)
    else:
        return render_template('filter.html')

@app.route("/graph", methods=['GET', 'POST'])
def graph():
    return render_template("graph.html")

@app.route("/profile/<username>", methods=['GET', 'POST'])
def profile(username):
    return render_template("profile.html")

@app.route("/signin", methods=['GET', 'POST'])
def signin():
    if  'username' in session.keys() and session['username'] is not None:
        return redirect('/')
    elif request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('pw')
        if not checkUser(username):
           return render_template("signin.html", message="This user does not exist")
        if not checkPassword(username, password):
           return render_template("signin.html", message="Incorrect Password")
        session['username'] = username
        session['password'] = password
        return redirect('/')
    return render_template("signin.html")

@app.route("/signup", methods=['GET', 'POST'])
def signup():
    if  'username' in session.keys() and session['username'] is not None:
        return redirect('/')
    elif request.method == 'POST':
        username = request.form['username']
        password = request.form['pw']
        if not checkUser(username):
            db.addUser(username, password)
            return redirect('/signin')
        else:
            return render_template('signup.html', message="Username already exists")
    return render_template("signup.html")

@app.route('/logout', methods=["POST"])
def logout():
    session.pop('username', None)
    session.pop('password', None)
    return redirect('/')

@app.route("/taste", methods=['GET', 'POST'])
def taste():
    return render_template("taste.html")


if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
