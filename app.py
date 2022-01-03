from flask import Flask, render_template, flash, request, redirect, url_for
# membuat instance flask
app = Flask(__name__)
#membuat route decorator
@app.route('/')
def index():
    return "tes"
#membuat custom error pages
# Invalid URL
@app.errorhandler(404)
def page_not_found(e):
	return render_template("404.html"), 404

# Internal Server Error
@app.errorhandler(500)
def page_not_found(e):
	return render_template("500.html"), 500
