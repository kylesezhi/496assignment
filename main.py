import webapp2

config = {'default-group': 'base-data'}

app = webapp2.WSGIApplication([
    ('/', 'base_page.ViewCards'),
    ('/admin', 'admin.Admin'),
], debug=True)
