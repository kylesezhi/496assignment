import webapp2

app = webapp2.WSGIApplication([
    ('/', 'base_page.ViewCards'),
    ('/admin', 'admin.Admin'),
], debug=True)
