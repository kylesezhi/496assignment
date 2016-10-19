import webapp2

config = {'default-group': 'base-data', 'admin-group': 'admin', 'user-group': 'user'}

app = webapp2.WSGIApplication([
    ('/', 'admin.Admin'),
    ('/user/new', 'modify.AddUser'),
    ('/class/new', 'modify.AddClass'),
    ('/user/edit', 'modify.EditUser'),
    ('/lineentry/new', 'modify.AddLineEntry'),
], debug=True, config=config)
app.router.add(webapp2.Route(r'/api/user','api.User'))
app.router.add(webapp2.Route(r'/api/user/<id:[0-9]+><:/?>','api.User'))
