from flask import Flask 
app = Flask(__name__)

@app.route("/")
def login():
    return "<h1>Login Page</h1>"

@app.route("/register")
def register():
    return "<h1>Register Page</h1>"

@app.route("/profile")
def profile():
    return "<h1>Profile Page</h1>"

if __name__=="__main__":
    app.run(debug=True, port=5001)

