from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "manbearpigMUD_1234456"


@app.route("/hello")
def index():
  return render_template("index.html")


@app.route("/choose_gift", methods=["POST", "GET"])
def submit():
  flash("You have requested the following gift: " + str(request.form['gift_type']))
  return render_template("index.html")