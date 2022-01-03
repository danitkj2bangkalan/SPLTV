from flask import Flask, render_template, flash, request, redirect, url_for
from flask_wtf import FlaskForm
# membuat instance flask
app = Flask(__name__)
#membuat route decorator
@app.route("/")
def home():
	return render_template("home.html")

@app.get("/materi")
def materi():
	return render_template("materi.html")

@app.get("/video")
def video():
	return render_template("video.html")

@app.get("/tugas")
def tugas():
	return render_template("tugas.html")

@app.get("/quiz")
def quiz():
	return render_template("quiz.html")

@app.get("/absen")
def absen():
	return render_template("absen.html")

@app.get("/referensi")
def referensi():
	return render_template("referensi.html")

@app.get("/pengaturan")
def pengaturan():
	return render_template("pengaturan.html")

@app.get("/daftar")
def daftar():
	return render_template("daftar.html")

@app.get("/lupasandi")
def lupasandi():
	return render_template("lupasandi.html")



#membuat custom error pages
# Invalid URL
@app.errorhandler(404)
def page_not_found(e):
	return render_template("404.html"), 404

# Internal Server Error
@app.errorhandler(500)
def page_not_found(e):
	return render_template("500.html"), 500
