import webapp2
from google.appengine.ext import ndb
import db_definitions
import json
from datetime import datetime


class Auth(webapp2.RequestHandler):
    # USES key AND usertype TO TELL IF THAT USER EXISTS
    def checkToken(self, key, usertype):
        users = [x.emailAndPass() for x in db_definitions.User.query(ancestor=ndb.Key(db_definitions.User, self.app.config.get(usertype + '-group'))).fetch()]
        d = next((item for item in users if item["key"] == key), None)
        if d is not None: return True
        return False

class User(webapp2.RequestHandler):
    def get(self, **kwargs):
        # we want a specific admin or user
        if 'user' in kwargs:
            users = [x.userData() for x in db_definitions.User.query(ancestor=ndb.Key(db_definitions.User, self.app.config.get('user-group'))).fetch()]
            admins = [x.userData() for x in db_definitions.User.query(ancestor=ndb.Key(db_definitions.User, self.app.config.get('admin-group'))).fetch()]
            for user in users: user['user_type'] = 'user'
            for admin in admins: admin['user_type'] = 'admin'
            response = admins + users
            for x in response:
                if x['id'] == int(kwargs['user']):
                    response = x
                    break
            self.response.write(json.dumps(response))
        # loop over all users
        else:
            users = [x.userData() for x in db_definitions.User.query(ancestor=ndb.Key(db_definitions.User, self.app.config.get('user-group'))).fetch()]
            admins = [x.userData() for x in db_definitions.User.query(ancestor=ndb.Key(db_definitions.User, self.app.config.get('admin-group'))).fetch()]
            for user in users: user['user_type'] = 'user'
            for admin in admins: admin['user_type'] = 'admin'
            
            self.response.write(json.dumps(users + admins))
        
    def post(self):
        """ Creates User
        
        POST variables:
            first_name - required
            last_name - required
            email - required
            password - required
            user_type - required: 'admin' or 'user'
            classes - optional
            """
        if self.request.get('token', default_value=None) == None:
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
        else:
            """ Updates Admin User
            
            POST variables:
                first_name - required
                last_name - required
                email - required
                token - required
                """

            key = ndb.Key(urlsafe=self.request.get('token'))
            user = key.get()
            user.first_name = self.request.get('first_name')
            user.last_name = self.request.get('last_name')
            user.email = self.request.get('email')
            user.put()
            return
        
    def delete(self, **kwargs):
        if 'user' in kwargs:
            user_key = ndb.Key(db_definitions.User, self.app.config.get('user-group'), db_definitions.User, int(kwargs['user']))

            # REMOVE RELATED PLACE IN LINE
            lineentries = db_definitions.LineEntry.query()
            for lineentry in lineentries:
                if lineentry.user == user_key:
                    lineentry.key.delete()

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
        if 'lineentry' in kwargs: # specific line entry
            line_key = ndb.Key(db_definitions.LineEntry, self.app.config.get('default-group'), db_definitions.LineEntry, int(kwargs['lineentry']))
            line = line_key.get()
            created = line.return_dict()['created']
            user = line.user.get()
            out = user.return_dict()
            out['created'] = created
            self.response.write(json.dumps(out))
        else: # return all line entries
            lines = [x.return_dict() for x in db_definitions.LineEntry.query(ancestor=ndb.Key(db_definitions.LineEntry, self.app.config.get('default-group'))).order(db_definitions.LineEntry.created).fetch()]
            users = [x.return_dict() for x in db_definitions.User.query(ancestor=ndb.Key(db_definitions.User, self.app.config.get('user-group'))).fetch()]
            for line in lines:
                if 'key' in line: del line['key']
                d = next((user for user in users if user["key"] == line['user']), None)
                line['username'] = d['first_name'] + ' ' + d['last_name']
                if 'user' in line: del line['user']
            self.response.write(json.dumps(lines))
            return
        
    def put(self, **kwargs):
        # Creates LineEntry
        
        if 'lineentry' in kwargs:
            users = [x.return_dict() for x in db_definitions.User.query(ancestor=ndb.Key(db_definitions.User, self.app.config.get('user-group'))).fetch()]
            d = next((item for item in users if item["id"] == int(kwargs['lineentry'])), None)
            user_key = ndb.Key(urlsafe=d['key'])

            line_key = ndb.Key(db_definitions.LineEntry, self.app.config.get('default-group'))
            line = db_definitions.LineEntry(parent=line_key)
            line.user = user_key
            line.put()
            out = line.return_dict()
            self.response.write(json.dumps(out))
            return
        return

    def post(self):
        # Deletes LineEntry
        
        # POST variables:
            # lineentry = required
            # token = an admin token
        
        # AUTHENTICATE FOR ADMIN ONLY
        token = self.request.get('token', default_value=None)
        if not Auth().checkToken(token, 'admin'):
            self.response.set_status(403, "Forbidden. Must be an admin.")
            self.response.write(self.response.status)

        lines = [x.return_dict() for x in db_definitions.LineEntry.query(ancestor=ndb.Key(db_definitions.LineEntry, self.app.config.get('default-group'))).fetch()]
        d = next((item for item in lines if item["id"] == int(self.request.get('lineentry'))), None)
        line_key = ndb.Key(urlsafe=d['key'])

        line_key.delete()
        return

class Login(Auth):
    def post(self):
        """ Authenticates User
        
        POST variables:
            email - required
            password - required
            """
        pwd = self.request.get('password', default_value=None)
        email = self.request.get('email', default_value=None)
        admins = [x.emailAndPass() for x in db_definitions.User.query(ancestor=ndb.Key(db_definitions.User, self.app.config.get('admin-group'))).fetch()]
        users = [x.emailAndPass() for x in db_definitions.User.query(ancestor=ndb.Key(db_definitions.User, self.app.config.get('user-group'))).fetch()]
        for user in users: user['user_type'] = 'user'
        for admin in admins: admin['user_type'] = 'admin'
        both = admins + users

        response = {}
        # print admins
        d = next((item for item in both if item["email"] == email), None)
        if d is not None:
            if pwd == d['password']:
                response['token'] = d['key']
                response['id'] = d['id']
                response['user_type'] = d['user_type']
        print response
        self.response.write(json.dumps(response))
        return
