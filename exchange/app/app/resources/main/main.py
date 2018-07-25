from flask import redirect, render_template, flash, request, url_for, session
from flask_login import login_user, current_user, login_required, logout_user
#from app.models.auth import *
from app.models.User import *
from flask.views import MethodView
from app.resources.home.Forms import LoginForm, RegistrationForm
from flask import jsonify

class MainView(MethodView):
	def get(self):

		if not current_user.is_authenticated:
			return redirect("/")

		return render_template('main.html', authenticated=current_user.is_authenticated)


	def post(self):
		# log me in
		if request.method == 'POST' and request.form.get('do') == 'login':
			form = LoginForm()
			if form.validate():
				user=User.query.filter_by(email=form.email.data).first()
				password = form.password.data

				if user is None:
				#check user does not exist
					return jsonify(status = 'error',
									message = "Ups! username not found!")

				if user.valid_password(password) == False:
				#check user password is false
					return jsonify(status = 'error',
									message = "Ups! check password")

				#login and remember user user checks it
				if login_user(user, remember=form.remember_me.data):
					session.permanent = not form.remember_me.data
					session['remember_me'] = form.remember_me.data
					session['logged_in'] = True

				return jsonify(status = 'success',
								message = url_for("main.main"))
		#log out 
		if request.method == 'POST' and request.form.get('do') == 'logout':
			logout_user()
			return jsonify(status = 'success',
							message = url_for("home.home"))

		return jsonify(status = 'validation',
						message = form.errors)

