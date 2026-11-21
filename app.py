
from flask import Flask, render_template, request

app = Flask(__name__)

# Temporary storage for registered students
users = {}


# LOGIN PAGE
@app.route("/", methods=["GET", "POST"])
def home():

    message = ""
    message_type = ""

    if request.method == "POST":

        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")

        if username in users and users[username]["password"] == password:
            message = "Login Successful!"
            message_type = "success"
        else:
            message = "Invalid Username or Password!"
            message_type = "error"

    return render_template(
        "login.html",
        message=message,
        message_type=message_type
    )


# REGISTRATION PAGE
@app.route("/signup", methods=["GET", "POST"])
def signup():

    message = ""
    message_type = ""

    if request.method == "POST":

        full_name = request.form.get("full_name", "").strip()
        email = request.form.get("email", "").strip()
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")
        confirm_password = request.form.get("confirm_password", "")

        if not all([full_name, email, username, password, confirm_password]):
            message = "Please fill in all fields!"
            message_type = "error"

        elif username in users:
            message = "Username already exists!"
            message_type = "error"

        elif password != confirm_password:
            message = "Passwords do not match!"
            message_type = "error"

        else:
            users[username] = {
                "full_name": full_name,
                "email": email,
                "password": password
            }

            message = "Registration Successful!"
            message_type = "success"

    return render_template(
        "signup.html",
        message=message,
        message_type=message_type
    )


# RUN APPLICATION
if __name__ == "__main__":
    app.run(debug=True)
