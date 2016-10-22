from google.appengine.ext import ndb

class Model(ndb.Model):
    def to_dict(self):
        d = super(Model, self).to_dict()
        d['id'] = self.key.id()
        return d

class User(Model):
    first_name = ndb.StringProperty(required=True)
    last_name = ndb.StringProperty(required=True)
    email = ndb.StringProperty(required=True)
    password = ndb.StringProperty(required=True)
    classes = ndb.KeyProperty(repeated=True)
    files = ndb.StringProperty(repeated=True)
    
    # @classmethod # TODO use somehow
    # def query_users(cls, ancestor_key):
        # return cls.query(ancestor=ancestor_key)
    
    def to_dict(self):
        d = super(User, self).to_dict()
        d['classes'] = []
        d['files'] = []
        for c in self.classes:
            d['classes'].append(c.id())
        for f in self.files:
            d['files'].append(f.id())
        return d

    def return_dict(self):
        cs = [x.urlsafe() for x in self.classes]
        return {'key': self.key.urlsafe(), 'first_name': self.first_name, 'last_name': self.last_name, 'email': self.email, 'classes': cs }

    
class Message(Model):
    created = ndb.DateTimeProperty(auto_now_add=True)
    message = ndb.StringProperty(required=True)
    user = user = ndb.KeyProperty(required=True)
    
class LineEntry(Model):
    created = ndb.DateTimeProperty(auto_now_add=True)
    user = ndb.KeyProperty(required=True)
    # problem = ndb.StringProperty(required=True) # TODO
    # messages = ndb.StructuredProperty(Message, repeated=True)
    files = ndb.StringProperty(repeated=True)
    
    def to_dict(self):
        d = super(LineEntry, self).to_dict()
        d['created'] = self.created.strftime('%d/%m/%y %H:%M')
        d['user'] = self.user.id()
        return d
    
    def return_dict(self):
        return {'key': self.key.urlsafe(), 'user': self.user.urlsafe(), 'created': self.created.strftime('%d/%m/%y %H:%M.%S') }
    
class UserClass(Model):
    name = ndb.StringProperty(required=True)
    
    def return_dict(self):
        return {'key': self.key.urlsafe(), 'name': self.name}
