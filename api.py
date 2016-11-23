import webapp2
from google.appengine.ext import ndb
import db_definitions
import json
from datetime import datetime

class User(webapp2.RequestHandler):
    def get(self, **kwargs):
        # we want a specific student
        if 'user' in kwargs:
            user_key = ndb.Key(db_definitions.User, self.app.config.get('user-group'), db_definitions.User, int(kwargs['user']))
            user = user_key.get()
            out = user.return_dict()
            self.response.write(json.dumps(out))
        # loop over all users
        else:
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
            user_type - required: 'admin' or 'user' TODO
            classes
            """
        if self.request.get('user_type', default_value=None) == 'admin':
            k = ndb.Key(db_definitions.User, self.app.config.get('admin-group'))
        else:
            k = ndb.Key(db_definitions.User, self.app.config.get('user-group'))

        u = db_definitions.User(parent=k)
        u.first_name = self.request.get('first_name', default_value=None)
        u.last_name = self.request.get('last_name', default_value=None)
        u.email = self.request.get('email', default_value=None)
        u.password = self.request.get('password', default_value=None)
        if None in (u.first_name, u.last_name, u.email, u.password):
            self.response.status = 400
            self.response.message = "Invalid request. Must provide all info for new user."
            return
        key = u.put()
        out = u.to_dict()
        self.response.write(json.dumps(out))
        return
        
    def delete(self, **kwargs):
        if 'user' in kwargs:
            user_key = ndb.Key(db_definitions.User, self.app.config.get('user-group'), db_definitions.User, int(kwargs['user']))
            # admin_key = ndb.Key(db_definitions.User, self.app.config.get('admin-group'), db_definitions.User, int(kwargs['user']))

            # REMOVE RELATED PLACE IN LINE
            lineentries = db_definitions.LineEntry.query()
            for lineentry in lineentries:
                if lineentry.user == user_key:
                    lineentry.key.delete()
                # if lineentry.user == admin_key:
                #     lineentry.key.delete()

            # REMOVE USER
            user_key.delete()
            # admin_key.delete()
        return
        
class UserClass(webapp2.RequestHandler):
    def get(self):
        q = db_definitions.UserClass.query()
        keys = q.fetch(keys_only = True)
        results = {'ids': [x.id() for x in keys]}
        self.response.write(json.dumps(results))

class LineEntry(webapp2.RequestHandler):
    def get(self, **kwargs):
        if 'lineentry' in kwargs:
            line_key = ndb.Key(db_definitions.LineEntry, self.app.config.get('default-group'), db_definitions.LineEntry, int(kwargs['lineentry']))
            line = line_key.get()
            created = line.return_dict()['created']
            user = line.user.get()
            out = user.return_dict()
            out['created'] = created
            self.response.write(json.dumps(out))
        else:
            q = db_definitions.LineEntry.query()
            keys = q.fetch(keys_only = True)
            results = {'ids': [x.id() for x in keys]}
            self.response.write(json.dumps(results))
            return
        
    def put(self, **kwargs):
        # Creates LineEntry
        
        # POST variables:
            # user = ndb.KeyProperty(required=True)
            # problem = ndb.StringProperty(required=True) # TODO
        
        # GET KEY FROM ID
        if 'user' in kwargs:
            user_key = ndb.Key(db_definitions.User, self.app.config.get('user-group'), db_definitions.User, int(kwargs['user']))
            # print('__DEBUG__')
            # print user_key
            
            line_key = ndb.Key(db_definitions.LineEntry, self.app.config.get('default-group'))
            line = db_definitions.LineEntry(parent=line_key)
            line.user = user_key
            line.put()
            out = line.to_dict()
            self.response.write(json.dumps(out))
            return
        return

    def post(self):
        # Creates LineEntry
        
        # POST variables:
            # user = ndb.KeyProperty(required=True)
            # problem = ndb.StringProperty(required=True) # TODO
        
        # GET KEY FROM ID
        user_key = ndb.Key(db_definitions.User, int(self.request.get('user')))
        
        # print('__DEBUG__')
        # print user_key

        line_key = ndb.Key(db_definitions.LineEntry, self.app.config.get('default-group'))
        line = db_definitions.LineEntry(parent=line_key)
        line.user = user_key
        line.put()
        out = line.return_dict()
        self.response.write(json.dumps(out))
        return

class Login(webapp2.RequestHandler):
    def post(self):
        """ Authenticates User
        
        POST variables:
            email - required
            password - required
            """
        pwd = self.request.get('password', default_value=None)
        admins = [x.emailAndPass() for x in db_definitions.User.query(ancestor=ndb.Key(db_definitions.User, self.app.config.get('admin-group'))).fetch()]
        response = {}
        d = next((item for item in admins if item["password"] == pwd), None)
        if d is not None:
            print "OK JOSE"
            response['token'] = d['key']
        self.response.write(json.dumps(response))
        return
