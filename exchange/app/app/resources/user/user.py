from flask import redirect, render_template, flash, request, url_for, session
from flask_login import login_user, current_user, login_required, logout_user
from app.models.Base import *
from app.models.auth.Group import *
from app.models.auth.Permission import *
from app.models.User import *
from flask.views import MethodView
from app.resources.home.Forms import LoginForm, RegistrationForm
from flask import jsonify


class UserView(MethodView):
	def get(self):
		pass
    
	def post(self):

		form = RegistrationForm()

		if form.validate_on_submit():

			if User.query.filter_by(email=form.email.data).first():
				return jsonify(status = 'validation',
							message = 'Email already exist')
			else:
				user = User(username=form.username.data,
                            password=form.email.data,
                            email=form.password.data)

				permission_level = Permission(name=u'read')
				group_membership = Group(name=u'User')
				db.session.add([user,
                                permission_level,
                                group_membership])
				db.session.commit()

		return jsonify(status = 'validation',
						message = form.errors)



	def delete(self, username):
		return 'delete'

	def put(self, username):
		return 'put'
