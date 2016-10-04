import webapp2

app = webapp2.WSGIApplication([
    ('/', 'base_page.AddCard'),
], debug=True)
