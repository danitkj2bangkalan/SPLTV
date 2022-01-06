from tkinter.messagebox import NO
from flask import Flask, render_template, flash, request, redirect, url_for
from webforms import LoginForm, UserForm
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
# membuat instance flask
app = Flask(__name__)
# untuk individual page
app.config['SECRET_KEY'] = "sahur amin" # secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db' #menambahkan database
db = SQLAlchemy(app) # inisialisasi database

#membuat model 
class Users(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(200), nullable=False)
	email = db.Column(db.String(120), nullable=False, unique=True)
	# password_hash = db.Column(db.String(128))
	date_added = db.Column(db.DateTime, default=datetime.utcnow)
	# Create A String
	def __repr__(self):
		return '<Name %r>' % self.name

# developing templates
@app.route("/",methods=['GET','POST'])
def home():
	form = LoginForm()
	name = None
	passwd= None
	if form.validate_on_submit():
		name = form.nama.data
		passwd = form.katasandi.data
		print(name,passwd)
		if name == 'amin' and passwd == 'amin':
			return redirect(url_for('guru'))

	return render_template("home.html", form = form)

@app.route("/materi")
def materi():
	return render_template("materi.html")

@app.route("/video")
def video():
	return render_template("video.html")

@app.route("/tugas")
def tugas():
	return render_template("tugas.html")

@app.route("/quiz")
def quiz():
	return render_template("quiz.html")

@app.route("/absen")
def absen():
	return render_template("absen.html")

@app.route("/referensi")
def referensi():
	return render_template("referensi.html")

@app.route("/pengaturan")
def pengaturan():
	return render_template("pengaturan.html")

@app.route("/daftar",methods=['GET','POST'])
def daftar():
	name = None
	form = UserForm()
	if form.validate_on_submit():
		# user = Users.query.filter_by(email = form.email.data).first()
		# if user is None :
		user = Users(name = form.name.data, email=form.email.data)
		db.session.add(user)
		db.session.commit()
		name = form.name.data
		form.name.data = ''
		form.email.data = ''
		flash("user ditambahkan")
	

	return render_template("daftar.html", form = form,
	name = name)

@app.route("/lupasandi")
def lupasandi():
	return render_template("lupasandi.html")

@app.route("/guru")
def guru():
	name = None
	form = UserForm()
	our_users = Users.query.order_by(Users.date_added)
	return render_template("guru.html", name = name, our_users = our_users)

# @app.route('/login',methods=['GET','POST'])
# def login():
# 	form = LoginForm()
# 	username = None
# 	password = None
# 	if form.validate_on_submit():
# 		username = form.username.data
# 		password = form.password.data
# 		print(username,password)
# 		if username == 'amin' and password == 'amin':
# 			flash("Sudah bisa masuk min")
# 			return redirect(url_for('guru'))

# 	return (form)



#membuat custom error pages
# Invalid URL
@app.errorhandler(404)
def page_not_found(e):
	return render_template("404.html"), 404

# Internal Server Error
@app.errorhandler(500)
def page_not_found(e):
	return render_template("500.html"), 500
