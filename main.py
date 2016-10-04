# import logging
import webapp2

app = webapp2.WSGIApplication([
    ('/', 'base_page.HelloWorld'),
], debug=True)
