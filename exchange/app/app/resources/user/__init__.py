from .User import UserView
from flask import Blueprint


user = Blueprint('user',__name__, template_folder='templates')
user.add_url_rule('/user/', view_func=UserView.as_view('user'), methods=['GET','POST',])
    

class Resource:
    def get_blueprint(self):
        return user
