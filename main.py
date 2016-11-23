import webapp2

config = {'default-group': 'base-data', 'admin-group': 'admin', 'user-group': 'user', 'app-secret': 'lskjdfalskdjfadks'}

app = webapp2.WSGIApplication([
    ('/', 'login.Login'),
    ('/admin', 'admin.Admin'),
    ('/admin/user/new', 'modify.AddUser'),
    ('/admin/class/new', 'modify.AddClass'),
    ('/admin/user/edit', 'modify.EditUser'),
    ('/admin/lineentry/new', 'modify.AddLineEntry'),
    ('/api/user','api.User'),
    ('/api/lineentry','api.LineEntry'),
    ('/api/class','api.UserClass'),
    ('/api/login','api.Login') # login to API
], debug=True, config=config)
app.router.add(webapp2.Route('/api/lineentry/<lineentry:[0-9]+><:/?>','api.LineEntry'))
app.router.add(webapp2.Route('/api/user/<user:[0-9]+><:/?>','api.User'))
