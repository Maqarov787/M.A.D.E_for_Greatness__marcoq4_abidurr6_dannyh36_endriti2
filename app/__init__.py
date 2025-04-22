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
from flask import url_for
import myanimedb as db
import myanimepanda as db2
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
        return render_template("main.html", username = session['username'], loggedIn="true")
    else:
        return render_template("main.html", loggedIn="false")

@app.route("/filter", methods=['GET', 'POST'])
def filter():
    genres = db2.get_specific_values('genres')
    bdfw = db2.get_specific_values('broadcast_day_of_the_week')
    studios = db2.get_specific_values('studios')
    if 'username' in session.keys():
        return render_template("filter.html", username = session['username'], loggedIn="true", genres = genres, bdfw = bdfw, studios = studios)
    else:
        return render_template('filter.html', loggedIn="false", genres = genres, bdfw = bdfw, studios = studios)

@app.route("/graph", methods=['GET', 'POST'])
def graph():
    if request.method =='POST':
        graph = request.form.get('typeOfGraph')
        category = request.form.get('category')
        values = request.form.get('values')
        print(graph)
        print(category)
        print(values)
        if 'username' in session.keys():
            if (graph == 'line'):
                return render_template("graph.html", username = session['username'], loggedIn="true", __type__ = graph) #__label_array__ will be the names of the anime in each category, __data_array will be their ratings
            if (graph == 'bar'):
                return render_template("graph.html", username = session['username'], loggedIn="true", __type__ = graph, __label_array__ = category) #__data_array__ will be the amount of animes in each category
            if (graph == 'pie'):
                return render_template("graph.html", username = session['username'], loggedIn="true", __type__ = graph, __label_array__ = category) #
        else:
            if (graph == 'line'):
                return render_template("graph.html", loggedIn="false", __type__ = graph)
            if (graph =='bar'):
                return render_template("graph.html", loggedIn="false", __type__ = graph, __label_array__ = category)
            if (graph == 'pie'):
                return render_template("graph.html", loggedIn="false", __type__ = graph, __label_array__ = category)
    
@app.route("/profile/<username>", methods=['GET', 'POST'])
def profile(username):
    if 'username' in session.keys():
        return render_template("profile.html", username = session['username'], loggedIn="true")
    else:
        return render_template("profile.html", loggedIn="false")
    
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

@app.route('/logout', methods=['GET', "POST"])
def logout():
    session.pop('username', None)
    session.pop('password', None)
    return redirect('/')

@app.route("/taste", methods=['GET', 'POST'])
def taste():
    if request.method == 'POST':
        print(db2.mean_score(['source', 'broadcast_day_of_the_week'], ['manga', 'saturday']))
    if 'username' in session.keys():
        return render_template("taste.html", username = session['username'], loggedIn="true")
    else:
        return render_template("taste.html", loggedIn="false")
    
if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
