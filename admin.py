import webapp2
import base_page
from google.appengine.ext import ndb
import db_definitions
from datetime import datetime


class Admin(base_page.BaseHandler):        
    def render(self, page):
        self.template_variables['users'] = [x.return_dict() for x in db_definitions.User.query(ancestor=ndb.Key(db_definitions.User, self.app.config.get('user-group'))).fetch()]
        self.template_variables['admins'] = [x.return_dict() for x in db_definitions.User.query(ancestor=ndb.Key(db_definitions.User, self.app.config.get('admin-group'))).fetch()]
        # self.template_variables['classes'] = [x.return_dict() for x in db_definitions.UserClass.query(ancestor=ndb.Key(db_definitions.UserClass, self.app.config.get('default-group'))).fetch()]
        base_page.BaseHandler.render(self, page, self.template_variables)
        
    def get(self):
        self.render('admin.html')

    def post(self):
        action = self.request.get('action')
        if action == 'add_user':
            if db_definitions.User.query(db_definitions.User.email == self.request.get('email')).fetch():
                self.template_variables['message'] = 'Error: that account already exists.'
            else:
                k = ndb.Key(db_definitions.User, self.app.config.get(self.request.get('user_type') + '-group'))
                user = db_definitions.User(parent=k)
                user.first_name = self.request.get('first_name')
                user.last_name = self.request.get('last_name')
                user.email = self.request.get('email')
                user.password = self.request.get('password')
                print(self.request.get_all('classes[]'))
                user.classes = [ndb.Key(urlsafe=x) for x in self.request.get_all('classes[]')]
                user.put()
                self.template_variables['message'] = 'Added ' + user.first_name + ' ' + user.last_name + '.'
            self.render('admin.html')
        elif action == 'edit_user':
            key = ndb.Key(urlsafe=self.request.get('key'))
            card = key.get()
            card.name = self.request.get('card_name')
            card.card_type = self.request.get('card_type')
            if not self.request.get('signup_bonus'):
                card.signup_bonus = False
            else:
                card.signup_bonus = True
            card.points_url = self.request.get('points_url')
            d = datetime.strptime(self.request.get('date_started'), '%Y-%m-%d')
            card.date_started = d
            card.put()
            self.template_variables['message'] = 'Updated ' + card.name + '.'
            self.render('admin.html')
        elif action == 'add_class':
            if db_definitions.UserClass.query(db_definitions.UserClass.name == self.request.get('name')).fetch():
                self.template_variables['message'] = 'Error: that class already exists.'
            else:
                k = ndb.Key(db_definitions.UserClass, self.app.config.get('default-group'))
                user_class = db_definitions.UserClass(parent=k)
                user_class.name = self.request.get('name')
                user_class.put()
                self.template_variables['message'] = 'Added ' + user_class.name + '.'
            self.render('admin.html')

        else:
            self.template_variables['message'] = action + ' is unknown.'
            self.render('admin.html')
