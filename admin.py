import webapp2
import base_page
from google.appengine.ext import ndb
import db_definitions


class Admin(base_page.BaseHandler):
    def get(self):
        self.render('admin.html')

    def post(self):
        action = self.request.get('action')
        if action == 'add_card':
            print('DEBUG')
            print(self.request)
            k = ndb.Key(db_definitions.Card, self.app.config.get('default-group'))
            card = db_definitions.Card(parent=k)
            card.name = self.request.get('card_name')   # TODO more elegant plz
            card.card_type = self.request.get('card_type')
            if not self.request.get('signup_bonus'):
                card.signup_bonus = False
            else:
                card.signup_bonus = True
            card.points_url = self.request.get('points_url')
            # card.week_started = self.request.get('week_started')
            card.put()
            self.render('admin.html', {'message': 'Added ' + card.name + '.'})
