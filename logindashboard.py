from flask import *
app=Flask(__name__)

@app.route("/")
def home():
    return "Home Page"

@app.route("/login/<role>")
def login(role):
    if role == "hrdashboard":
        return redirect(url_for('hr_dashboard'))
    else:
        return redirect(url_for('stud_dashboard'))
    
@app.route("/hrdashboard")
def hr_dashboard():
    return "Hr Dashboard"

@app.route("/studdashboard")
def stud_dashboard():
    return "Student Dashboard"

if __name__=="__main__":
    app.run(debug=True)
    