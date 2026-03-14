from flask import Flask, render_template, request, redirect
import sqlite3
import datetime
import smtplib
from email.mime.text import MIMEText

def send_email(student_email, name):

    sender = "polojualekhya6@gmail.com"
    password = "rujs vlbn wnfm jboz"

    message = f"Hello {name},\n\nToday is your hostel fee due date. Please pay the fee."

    msg = MIMEText(message)
    msg["Subject"] = "Hostel Fee Reminder"
    msg["From"] = sender
    msg["To"] = student_email

    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()

    server.login(sender,password)
    server.send_message(msg)

    server.quit()

app = Flask(__name__)

@app.route("/")
def home():

    conn = sqlite3.connect("database.db")
    cur = conn.cursor()

    cur.execute("SELECT * FROM students")
    data = cur.fetchall()

    conn.close()

    today = datetime.datetime.now().day

    return render_template("dashboard.html", data=data, today=today)


@app.route("/add", methods=["GET","POST"])
def add_student():

    if request.method == "POST":

        name = request.form["name"]
        room = request.form["room"]
        email = request.form["email"]
        due = int(request.form["due"])

        conn = sqlite3.connect("database.db")
        cur = conn.cursor()

        cur.execute(
        "INSERT INTO students(name,room_no,email,due_date,fee_status) VALUES(?,?,?,?,?)",
        (name, room, email, due, "Unpaid")
        )

        conn.commit()
        conn.close()

        return redirect("/")

    return render_template("add_student.html")


if __name__ == "__main__":
    app.run(debug=True)