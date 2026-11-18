from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return "this is web templating System"


@app.route("/ps")
def ps():
    num = 290
    return render_template("ps.html", n=num)


@app.route("/ps1")
def ps2():
    name = "Piya"
    return render_template("ps2.html", name=name)

@app.route("/ps3/<name>")
def ps3(name):
    return render_template("ps3.html",name=name)

@app.route("/ps4")
def ps4():
    stu_list=[56,"heloo",True,78.0]
    return render_template("ps4.html",list=stu_list)

@app.route("/ps5")
def ps5():
    stud_dict={"id":101,"name":"abc","city":"Pune"}
    return render_template("ps5.html",list=stud_dict)

if __name__ == "__main__":
    app.run(debug=True)