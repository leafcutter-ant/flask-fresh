from . import views
from flask import Blueprint

blue_print = Blueprint('user', __name__, url_prefix='/user')

blue_print.add_url_rule('/register', view_func=views.RegisterView.as_view('register'))
blue_print.add_url_rule('/login', view_func=views.LoginView.as_view('login'))
blue_print.add_url_rule('/logout', view_func=views.LogoutView.as_view('logout'))
blue_print.add_url_rule('/active/<token>', view_func=views.ActiveView.as_view('active'))