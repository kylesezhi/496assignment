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
