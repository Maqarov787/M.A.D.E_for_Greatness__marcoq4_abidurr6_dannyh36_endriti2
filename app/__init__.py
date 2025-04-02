from flask import Flask
from flask import render_template  
from flask import request           
from flask import session

app = Flask(__name__)

@app.route("/")
def main():
    return "Project 4"

@app.route("/graph")
def graph():
    return render_template("graph.html")     

@app.route("profile")
def profile():
    return render_template("profile.html")
    
@app.route("signin")
def signin():
    return render_template("signin.html")

@app.route("signup")
def signup():
    return render_template("signup.html")

@app.route("taste")
def taste():
    return render_template("taste.html")

if __name__ == "__main__": 
    app.debug = True      
    app.run(host='0.0.0.0')
