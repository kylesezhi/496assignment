import webapp2

config = {'default-group': 'base-data', 'admin-group': 'admin', 'user-group': 'user'}

app = webapp2.WSGIApplication([
    ('/', 'admin.Admin'),
    ('/user/new', 'modify.Add'),
    ('/user/edit', 'modify.Edit'),
], debug=True, config=config)
