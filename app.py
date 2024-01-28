from flask import Flask, render_template, request
app = Flask(__name__)
users = []

@app.route("/")
def hello():
    return render_template("homepage.html")

@app.route("/signup/", methods=["POST", "GET"])
def signup():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        users.append((username, password))
        return render_template("users.html", users=users)
    else:
        return render_template("signup.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)