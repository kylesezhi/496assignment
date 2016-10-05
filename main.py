import webapp2

config = {'default-group': 'base-data'}

app = webapp2.WSGIApplication([
    ('/', 'admin.Admin'),
    ('/add', 'modify.Add'),
], debug=True, config=config)
