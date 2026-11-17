from flask import *

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Url_Building</h1>"

@app.route("/name/str")
def name():
    str="Piya"
    return "Hello My name is %s" %str

@app.route("/roll/num")
def roll_no():
    num=67
    return "My rollno is %d"%num

@app.route("/age/<int:a>")
def age(a):
    return "My age is %d"%a

if __name__ == "__main__":
    app.run(debug=True)
    