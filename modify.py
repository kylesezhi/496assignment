import webapp2
import base_page
from google.appengine.ext import ndb
import db_definitions


class Add(base_page.BaseHandler):
    def get(self):
        self.render('add.html')
