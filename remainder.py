import sqlite3
import datetime
import smtplib
from email.mime.text import MIMEText

today = datetime.datetime.now().day

conn = sqlite3.connect("database.db")
cur = conn.cursor()

cur.execute("SELECT name,email,due_date FROM students")
data = cur.fetchall()

sender = "polojualekhya6@gmail.com"
password = "rujs vlbn wnfm jboz"

for student in data:

    name = student[0]
    email = student[1]
    due = int(student[2])

    if today == due:

        message = f"Hello {name},\n\nToday is your hostel fee due date. Please pay the fee."

        msg = MIMEText(message)
        msg["Subject"] = "Hostel Fee Reminder"
        msg["From"] = sender
        msg["To"] = email

        server = smtplib.SMTP("smtp.gmail.com",587)
        server.starttls()

        server.login(sender,password)
        server.send_message(msg)

        server.quit()

        print(f"Reminder email sent to {name}")