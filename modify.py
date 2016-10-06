import webapp2
import base_page
from google.appengine.ext import ndb
import db_definitions


class Add(base_page.BaseHandler):
    def get(self):
        self.render('add.html')


class Edit(base_page.BaseHandler):
    def __init__(self, request, response):
        self.initialize(request, response)
        self.template_variables = {}

    def render(self, page):
        base_page.BaseHandler.render(self, page, self.template_variables)

    def get(self):
        card_key = ndb.Key(urlsafe=self.request.get('key'))
        card = card_key.get()
        self.template_variables['card'] = card.returnDict()
        self.render('edit.html')
    
