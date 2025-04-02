from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "Project 4"
    
    
if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()
