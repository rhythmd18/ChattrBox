"""Importing desired libraries"""
import sqlite3
from flask import Flask, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required


# Configure session
app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Ensure that templates are auto-reloaded
app.config["TEMPLATES_AUTO-RELOAD"] = True


# Configure CS50 Library to use SQLite database
db = sqlite3.connect("chattrbox.db", check_same_thread=False)


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response



@app.route("/")
@login_required
def index():
    """Enter the chat room"""
    rows = db.execute("SELECT * FROM users WHERE id = ?", session['user_id'])
    username = rows[0]['username']
    return render_template("chat.html", username=username)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", (request.form.get("username"),))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    if request.method == "POST":
        # Load up the users database to check for already existing users
        usernames_dict = db.execute("SELECT username FROM users")
        usernames = []
        for i in range(len(usernames_dict)):
            if usernames_dict == []:
                break
            else:
                usernames.append(usernames_dict[i]["username"])
        
        # Store user's username and password
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")
        hashed_password = generate_password_hash(password)

        # Validate username and password
        if username in usernames:
            return apology("Username aleady exists! Try different usernames out")
        elif not username or not password:
            return apology("Enter both username and password!")
        elif not confirmation:
            return apology("Please confirm your password!")
        elif password != confirmation:
            return apology("Passwords do not match")
        else:
            db.execute("INSERT OR IGNORE INTO users (username, hash) VALUES (?, ?)", username, hashed_password)
            user_id = db.execute("SELECT id FROM users WHERE username = ?", username)
            session["user_id"] = user_id[0]["id"]
            return redirect("/")

    return render_template("register.html")


@app.route("/changepassword", methods=["GET", "POST"])
@login_required
def change_password():
    """Changing user's password"""

    if request.method == "POST":
        password = request.form.get("password")
        newpassword = request.form.get("newpassword")
        confirmation = request.form.get("confirmation")

        if not password:
            return apology("Give your old password")
        elif not newpassword or not confirmation:
            return apology("Enter your password and confirm it as well")
        elif newpassword != confirmation:
            return apology("Enter the same password again")
        else:
            # Query database for id
            rows = db.execute("SELECT * FROM users WHERE id = ?", session["user_id"])

            # Check if the old password entered is correct
            if not check_password_hash(rows[0]["hash"], password):
                return apology("Enter your current password correctly")

            db.execute("UPDATE users SET hash = (?) WHERE id = ?", generate_password_hash(password), session["user_id"])
            return redirect("/")
        
    else:
        return render_template("change-password.html")


