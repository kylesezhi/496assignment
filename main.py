# import logging
import webapp2

app = webapp2.WSGIApplication([
    ('/', 'base_page.HelloWorld'),
], debug=True)

# @app.route('/')
# def hello():
#     return 'Hello Worldt!'
# 
# 
# @app.errorhandler(500)
# def server_error(e):
#     # Log the error and stacktrace.
#     logging.exception('An error occurred during a request.')
#     return 'An internal error occurred.', 500
