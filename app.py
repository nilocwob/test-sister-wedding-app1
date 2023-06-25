import os

from flask import Flask, render_template, request, flash
import smtplib

app = Flask(__name__)
app.secret_key = "manbearpigMUD_1234456"


@app.route("/hello")
def index():
  return render_template("index.html")


@app.route("/choose_gift", methods=["POST", "GET"])
def submit():
  message = ""
  if request.form['gift_type'] != "Other":
    message = str(request.form['gift_type'])
  else:
    message = str(request.form['gift_type']) + " - " + str(request.form['other_gift'])
  flash("You have requested the following gift: " + message)

  email = "cabvids@gmail.com"
  from_addr = os.environ['FROM_EMAIL']

  email_msg = "Request sent to Colin! Please give a gift of " + message

  server = smtplib.SMTP("smtp.gmail.com", 587)
  server.starttls()
  server.login(from_addr, os.environ['EMAIL_PASSWORD'])
  server.sendmail(from_addr, email, email_msg)

  return render_template("index.html")