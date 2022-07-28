from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)


username = "Adi"
password = "123"
facebook_friends=["Yossi","Yossi","Yossi", "Yossi", "Yossi", "Yossi"]





@app.route('/', methods = ['GET', 'POST'])  # '/' for the default page
def login():
	if request.method == 'POST':
		if username == request.form['username']:
			if password == request.form['password']:
				return redirect(url_for('home'))
	else:
		return render_template('login.html')

@app.route("/home")
def home():
	return render_template('home.html', friendslist = facebook_friends)

@app.route("/friend_exists/<string:name>", methods = ["GET", "POST"])
def exist(name):
	if request.method == "GET" and name in facebook_friends:
		boo = "True"
		return render_template("friend_exists.html", n = name, boo = boo)

if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
		debug=True,
		port = 5001
	)