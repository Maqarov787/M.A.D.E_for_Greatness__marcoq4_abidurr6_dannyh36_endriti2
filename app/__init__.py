'''
Marco, Abidur, Danny, Endrit
M.A.D.E for Greatness
SoftDev
P04
Time spent: 50 hours
Target Ship Date: 2025-04-21
'''


from flask import Flask
from flask import render_template  
from flask import request           
from flask import session

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def main():
    return render_template("main.html")

@app.route("/filter", methods=['GET', 'POST'])
def filter():
    return render_template("filter.html")

@app.route("/graph", methods=['GET', 'POST'])
def graph():
    return render_template("graph.html")     

@app.route("/profile", methods=['GET', 'POST'])
def profile():
    return render_template("profile.html")
    
@app.route("/signin", methods=['GET', 'POST'])
def signin():
    return render_template("signin.html")

@app.route("/signup", methods=['GET', 'POST'])
def signup():
    return render_template("signup.html")

@app.route("/taste", methods=['GET', 'POST'])
def taste():
    return render_template("taste.html")

if __name__ == "__main__": 
    app.debug = True      
    app.run(host='0.0.0.0')
