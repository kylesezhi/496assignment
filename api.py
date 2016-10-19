import webapp2
from google.appengine.ext import ndb
import db_definitions
import json

class User(webapp2.RequestHandler):
    def get(self):
        q = db_definitions.User.query()
        keys = q.fetch(keys_only = True)
        results = {'keys': [x.id() for x in keys]}
        self.response.write(json.dumps(results))
        
    def post(self):
        """ Creates User
        
        POST variables:
            first_name - required
            last_name - required
            email - required
            password - required
            """
        u = db_definitions.User()
        u.first_name = self.request.get('first_name', default_value=None)
        u.last_name = self.request.get('last_name', default_value=None)
        u.email = self.request.get('email', default_value=None)
        u.password = self.request.get('password', default_value=None)
        if None in (u.first_name, u.last_name, u.email, u.password):
            self.response.status = 400
            self.response.message = "Invalid request. Must provide all info for new user."
            return
        key = u.put()
        out = u.return_dict()
        self.response.write(json.dumps(out))
        return
