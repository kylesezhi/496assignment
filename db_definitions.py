from google.appengine.ext import ndb


class Card(ndb.Model):
    name = ndb.StringProperty(required=True)
    card_type = ndb.StringProperty(required=True)
    signup_bonus = ndb.BooleanProperty(required=True)
    points_url = ndb.StringProperty(required=True)
    date_started = ndb.DateProperty(required=True)
    
    def returnDict(self):
        return {'key': self.key.urlsafe(), 'name': self.name, 'card_type': self.card_type, 'signup_bonus': self.signup_bonus, 'points_url': self.points_url, 'date_started': self.date_started}
