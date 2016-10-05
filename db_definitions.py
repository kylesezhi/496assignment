from google.appengine.ext import ndb


class Card(ndb.Model):
    name = ndb.StringProperty(required=True)
    card_type = ndb.StringProperty(required=True)
    signup_bonus = ndb.BooleanProperty(required=True)
    points_url = ndb.StringProperty(required=True)
    date_started = ndb.DateProperty(required=True)
