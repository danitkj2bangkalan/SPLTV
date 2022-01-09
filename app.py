from tkinter.messagebox import NO
from flask import Flask, render_template, flash, request, redirect, url_for
from webforms import LoginForm, UserForm
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime
# membuat instance flask
app = Flask(__name__)
# untuk individual page
app.config['SECRET_KEY'] = "sahur amin" # secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db' #menambahkan database
db = SQLAlchemy(app) # inisialisasi database
migrate = Migrate(app, db) 
#membuat model database
class Users(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(200), nullable=False)
	email = db.Column(db.String(120), nullable=False, unique=True)
	nilai = db.Column(db.String(200))
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

# untuk ngisi data ke database ---
@app.route("/daftar",methods=['GET','POST'])
def daftar():
	name = None
	form = UserForm()
	if form.validate_on_submit():
		# user = Users.query.filter_by(email = form.email.data).first()
		# if user is None :
		user = Users(name = form.name.data, email=form.email.data, score = form.nilai.data)
		db.session.add(user)
		db.session.commit()
		name = form.name.data
		form.name.data = ''
		form.email.data = ''
		form.nilai.data = ''
		flash("user ditambahkan")
	
	return render_template("daftar.html", form = form,
	name = name)

@app.route("/guru")
def guru():

	form = UserForm()
	our_users = Users.query.order_by(Users.date_added)
	return render_template("guru.html", our_users = our_users)
# ---
@app.route("/lupasandi")
def lupasandi():
	return render_template("lupasandi.html")

#update user
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
	form = UserForm()
	name_to_update = Users.query.get_or_404(id)
	if request.method == "POST":
		name_to_update.name = request.form['name']
		name_to_update.email = request.form['email']
		name_to_update.nilai = request.form['nilai']
		try:
			db.session.commit()
			flash("User berhasil diupdate")
			return render_template("update.html", 
				form=form,
				name_to_update = name_to_update, id=id)
		except:
			flash("Error!  Sepertinya ada masalah coba lagi")
			return render_template("update.html", 
				form=form,
				name_to_update = name_to_update,
				id=id)
	else:
		return render_template("update.html", 
				form=form,
				name_to_update = name_to_update,
				id = id)


#membuat custom error pages
# Invalid URL
@app.errorhandler(404)
def page_not_found(e):
	return render_template("404.html"), 404

# Internal Server Error
@app.errorhandler(500)
def page_not_found(e):
	return render_template("500.html"), 500
