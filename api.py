import webapp2
from google.appengine.ext import ndb
import db_definitions
import json

class User(webapp2.RequestHandler):
    def get(self):
        q = db_definitions.User.query()
        keys = q.fetch(keys_only = True)
        results = {'ids': [x.id() for x in keys]}
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
        
class LineEntry(webapp2.RequestHandler):
    def get(self):
        q = db_definitions.LineEntry.query()
        keys = q.fetch(keys_only = True)
        results = {'ids': [x.id() for x in keys]}
        self.response.write(json.dumps(results))
        
    def post(self):
        # Creates LineEntry
        
        # POST variables:
            # user = ndb.KeyProperty(required=True)
            # problem = ndb.StringProperty(required=True) # TODO
            # messages = ndb.StructuredProperty(Message, repeated=True)
            # files = ndb.StringProperty(repeated=True)
        
        # get the key from the id
        user_id = self.request.get('user') # TODO this must be easier
        q = db_definitions.User.query()
        keys = q.fetch(keys_only = True)
        x = ''
        for key in keys:
            if int(key.id()) == int(user_id):
                x = key
                break
        # results = [x.id() for x in keys if x.id() == user_id]
        # u = User()
        # x = db_definitions.User.get_by_id(5629499534213120)
        # q = db_definitions.User.all()
        # q.filter('__key__ =', 5629499534213120)
        # q.filter('__id__ =', 5629499534213120)
        # x = ndb.Key(db_definitions.User, 5629499534213120).get()
        
        
        
