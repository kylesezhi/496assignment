import webapp2
import base_page
from google.appengine.ext import ndb
import db_definitions
from datetime import datetime
from google.appengine.api import users


class Login(base_page.BaseHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            nickname = user.nickname()
            logout_url = users.create_logout_url('/')
            self.redirect('/admin')
        else:
            login_url = users.create_login_url('/')
            self.redirect(login_url)
