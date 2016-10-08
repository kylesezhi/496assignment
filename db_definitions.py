from google.appengine.ext import ndb


class User(ndb.Model):
    first_name = ndb.StringProperty(required=True)
    last_name = ndb.StringProperty(required=True)
    email = ndb.StringProperty(required=True)
    password = ndb.StringProperty(required=True)
    classes = ndb.KeyProperty(repeated=True)
    
    @classmethod
    def query_users(cls, ancestor_key):
        return cls.query(ancestor=ancestor_key)
    
    def return_dict(self):
        return {'key': self.key.urlsafe(), 'first_name': self.first_name, 'last_name': self.last_name, 'email': self.email}

    
class LineEntry(ndb.Model):
    created = ndb.DateTimeProperty(required=True)
    user = ndb.KeyProperty(required=True)
    
class UserClass(ndb.Model):
    name = ndb.StringProperty(required=True)
