from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    print("VISITED THE HELLO PAGE")
    return "Hello World!"

@app.route("/about")
def about():
    print("VISITED THE ABOUT PAGE")
    return "About Me"
