import webapp2

config = {'default-group': 'base-data', 'admin-group': 'admin', 'user-group': 'user'}

app = webapp2.WSGIApplication([
    ('/', 'admin.Admin'),
    ('/user/new', 'modify.AddUser'),
    ('/class/new', 'modify.AddClass'),
    ('/user/edit', 'modify.EditUser'),
    ('/lineentry/new', 'modify.AddLineEntry'),
    ('/api/user','api.User'),
    ('/api/lineentry','api.LineEntry'),
    ('/api/class','api.UserClass'),
], debug=True, config=config)
app.router.add(webapp2.Route('/api/lineentry/user/<user:[0-9]+><:/?>','api.LineEntry'))
