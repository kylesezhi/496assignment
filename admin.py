import webapp2
import base_page
from google.appengine.ext import ndb
import db_definitions
from datetime import datetime


class Admin(base_page.BaseHandler):
    def __init__(self, request, response):
        self.initialize(request, response)
        self.template_variables = {}
        
    def render(self, page):
        self.template_variables['users'] = [x.return_dict() for x in db_definitions.User.query(ancestor=ndb.Key(db_definitions.User, self.app.config.get('default-group'))).fetch()]
        base_page.BaseHandler.render(self, page, self.template_variables)
        
    def get(self):
        self.render('admin.html')

    def post(self):
        action = self.request.get('action')
        if action == 'add_user':
            # TODO add after User: self.app.config.get('admin-group')
            k = ndb.Key(db_definitions.User, self.app.config.get('default-group'))
            user = db_definitions.User(parent=k)
            user.first_name = self.request.get('first_name')
            user.last_name = self.request.get('last_name')
            user.email = self.request.get('email')
            user.password = self.request.get('password')
            print('DEBUG')
            print(self.request.get('user_type')) # either student or teacher
            user.put()
            self.template_variables['message'] = 'Added ' + user.first_name + ' ' + user.last_name + '.'
            self.render('admin.html')
        elif action == 'edit_card':
            key = ndb.Key(urlsafe=self.request.get('key'))
            card = key.get()
            # print('DEBUGZ')
            # print(card.return_dict())
            card.name = self.request.get('card_name')   # TODO put in class def?
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
        else:
            self.template_variables['message'] = action + ' is unknown.'
            self.render('admin.html')
