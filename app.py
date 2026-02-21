from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "astrase_secret_key"

# ---------------- LOGIN PAGE ----------------
@app.route("/")
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        # Hardcoded check for prototype testing
        if email == "admin@gmail.com" and password == "1234":
            session["user"] = email
            return redirect(url_for("home"))
        else:
            return render_template("login.html", error="Use admin@gmail.com and 1234")

    return render_template("login.html")

# ---------------- HOME PAGE ----------------
@app.route("/home")
def home():
    if "user" in session:
        return render_template("home.html")
    return redirect(url_for("login"))

# ---------------- SAFE ROUTES PAGE ----------------
@app.route("/safe")
def safe():
    if "user" in session:
        return render_template("safe.html")
    return redirect(url_for("login"))

# ---------------- SAFE PLACES PAGE ----------------
@app.route("/safeplace")
def safeplace():
    if "user" in session:
        return render_template("safeplace.html")
    return redirect(url_for("login"))

# ---------------- GUARDIANS PAGE ----------------
@app.route("/guardians")
def guardians():
    if "user" in session:
        return render_template("guardians.html")
    return redirect(url_for("login"))

# ---------------- ALERTS PAGE ----------------
@app.route("/alerts")
def alerts():
    if "user" in session:
        return render_template("alerts.html")
    return redirect(url_for("login"))

# ---------------- SETTINGS PAGE ----------------
@app.route("/settings")
def settings():
    if "user" in session:
        return render_template("settings.html")
    return redirect(url_for("login"))

# ---------------- LOGOUT ----------------
@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)