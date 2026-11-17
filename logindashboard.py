from flask import *
app=Flask(__name__)

@app.route("/")
def login():
    return "login page"


@app.route("/hrdashboard")
def hr_dashboard():
    return "Hr Dashboard"

@app.route("/studdashboard")
def stud_dashboard():
    return "Student Dashboard"

if __name__=="__main__":
    app.run(debug=True)