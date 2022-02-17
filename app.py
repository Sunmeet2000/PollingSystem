import sqlite3
from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)

@app.route("/",methods=["POST","GET"])
def login():
    conn = sqlite3.connect('polling.db')

    if request.method == "POST":
        username = request.form.get("uname")
        password = request.form.get("pass")
        if not username or not password:
            return ("\n Enter username and password")
        db=conn.execute("SELECT * FROM user WHERE username = :username ",{"username":username})
        rows = db.fetchone()
        print(generate_password_hash(password))
        if not check_password_hash(rows[1],password):
            return("\nInvalid username or password")

        return redirect("home.html")
    else:
        return render_template("login.html")

