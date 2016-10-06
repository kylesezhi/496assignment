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
        self.template_variables['cards'] = [x.returnDict() for x in db_definitions.Card.query(ancestor=ndb.Key(db_definitions.Card, self.app.config.get('default-group'))).fetch()]
        base_page.BaseHandler.render(self, page, self.template_variables)
        
    def get(self):
        self.render('admin.html')

    def post(self):
        action = self.request.get('action')
        if action == 'add_card':
            k = ndb.Key(db_definitions.Card, self.app.config.get('default-group'))
            card = db_definitions.Card(parent=k)
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
            self.template_variables['message'] = 'Added ' + card.name + '.'
            self.render('admin.html')
        elif action == 'edit_card':
            key = ndb.Key(urlsafe=self.request.get('key'))
            card = key.get()
            # print('DEBUGZ')
            # print(card.returnDict())
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
