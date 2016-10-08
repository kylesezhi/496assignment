import webapp2
import base_page
from google.appengine.ext import ndb
import db_definitions


class AddUser(base_page.BaseHandler):
    def render(self, page):
        self.template_variables['classes'] = [x.return_dict() for x in db_definitions.UserClass.query(ancestor=ndb.Key(db_definitions.UserClass, self.app.config.get('default-group'))).fetch()]
        base_page.BaseHandler.render(self, page, self.template_variables)

    def get(self):
        self.render('add.html')
        
class AddClass(base_page.BaseHandler):
    def get(self):
        self.render('addclass.html')


class EditUser(base_page.BaseHandler):
    def render(self, page):
        base_page.BaseHandler.render(self, page, self.template_variables)

    def get(self):
        card_key = ndb.Key(urlsafe=self.request.get('key'))
        card = card_key.get()
        self.template_variables['card'] = card.return_dict()
        self.render('edit.html')
