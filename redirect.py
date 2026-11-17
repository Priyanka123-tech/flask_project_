from flask import *
app=Flask(__name__)

@app.route("/")
def home():
    return "Redirect Process"

@app.route("/about")
def about():
    return redirect(url_for("welcome2"))# function name of welcome2

@app.route("/welcome1")
def welcome2():
    return "Welcome to Flask Project"

if __name__=="__main__":
    app.run(debug=True)