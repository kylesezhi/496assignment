from google.appengine.ext import ndb


class User(ndb.Model):
    first_name = ndb.StringProperty(required=True)
    last_name = ndb.StringProperty(required=True)
    email = ndb.StringProperty(required=True)
    password = ndb.StringProperty(required=True)
    classes = ndb.KeyProperty(repeated=True)
    files = ndb.StringProperty(repeated=True)
    
    # @classmethod # TODO use somehow
    # def query_users(cls, ancestor_key):
        # return cls.query(ancestor=ancestor_key)
    
    def return_dict(self):
        cs = [x.urlsafe() for x in self.classes]
        return {'key': self.key.urlsafe(), 'first_name': self.first_name, 'last_name': self.last_name, 'email': self.email, 'classes': cs }

    
class Message(ndb.Model):
    created = ndb.DateTimeProperty(auto_now_add=True)
    message = ndb.StringProperty(required=True)
    user = user = ndb.KeyProperty(required=True)
    
class LineEntry(ndb.Model):
    created = ndb.DateTimeProperty(auto_now_add=True)
    user = ndb.KeyProperty(required=True)
    # problem = ndb.StringProperty(required=True) # TODO
    # messages = ndb.StructuredProperty(Message, repeated=True)
    files = ndb.StringProperty(repeated=True)
    
    def return_dict(self):
        return {'key': self.key.urlsafe(), 'user': self.user.urlsafe(), 'created': self.created.strftime('%d/%m/%y %H:%M') }
    
class UserClass(ndb.Model):
    name = ndb.StringProperty(required=True)
    
    def return_dict(self):
        return {'key': self.key.urlsafe(), 'name': self.name}
