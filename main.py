import webapp2

config = {'default-group': 'base-data', 'admin-group': 'admin', 'user-group': 'user'}

app = webapp2.WSGIApplication([
    ('/', 'login.Login'),
    ('/admin', 'admin.Admin'),
    ('/admin/user/new', 'modify.AddUser'),
    ('/admin/class/new', 'modify.AddClass'),
    ('/admin/user/edit', 'modify.EditUser'),
    ('/admin/lineentry/new', 'modify.AddLineEntry'),
    ('/admin/api/user','api.User'),
    ('/admin/api/lineentry','api.LineEntry'),
    ('/admin/api/class','api.UserClass'),
], debug=True, config=config)
app.router.add(webapp2.Route('/admin/api/lineentry/<lineentry:[0-9]+><:/?>','api.LineEntry'))
app.router.add(webapp2.Route('/admin/api/user/<user:[0-9]+><:/?>','api.User'))
