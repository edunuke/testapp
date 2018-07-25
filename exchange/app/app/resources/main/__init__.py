from flask import Blueprint
from .Main import MainView
from flask_login import login_user, current_user, login_required, logout_user
from flask import redirect, render_template, flash, request, url_for, session

main = Blueprint('main',__name__, template_folder='templates', static_folder='static', static_url_path = '/main/static')

main.add_url_rule('/main/', view_func=MainView.as_view('main'), methods=['GET','POST',])

@main.route('/logout')
@login_required
def logout():
	logout_user()
	return redirect("/")

class Resource:
    def get_blueprint(self):
        return main