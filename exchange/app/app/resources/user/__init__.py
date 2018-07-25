from .User import User
from flask import Blueprint

user = Blueprint('user',__name__,)

user_api = User.as_view('user_api')

user.add_url_rule('/users/', view_func = user_api, methods=["GET","POST"])
#user.add_url_rule('/users/reset_password/<string:username>	', view_func = user_api_view, methods=["RESET",])

class Resource:
    def get_blueprint(self):
        return user
