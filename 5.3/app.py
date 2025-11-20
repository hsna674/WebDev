from flask import Flask, render_template, request, redirect, session
import hashlib

app = Flask(__name__)
app.secret_key = "secret"


def load_creds():
    creds = {}
    with open("credentials.txt") as f:
        for line in f:
            user, pw = line.strip().split(":")
            creds[user] = pw
    return creds


creds = load_creds()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")
    hashed = hashlib.sha256(password.encode()).hexdigest()
    if creds.get(username) == hashed:
        session['logged_in'] = True
        session['user'] = username
        return redirect("/secret")
    else:
        return redirect("/?success=false")


@app.route("/secret")
def secret():
    if not session.get("logged_in"):
        return redirect("/?auth_error=true")
    return render_template("secret.html", user=session.get("user"))


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/?logout=true")


if __name__ == "__main__":
    app.run(debug=True)
