from flask import Flask
from flask import render_template

app = Flask(__name__)

about_company_1 = """
The company name is....
Te company was found in.....
"""
@app.route('/')
def index():
	return render_template("index.html")

@app.route("/user/<user_name>")
def user()