import webapp2
import os
import jinja2


JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__) + '/templates'),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True
)


class BaseHandler(webapp2.RequestHandler):
    @webapp2.cached_property
    def jinja2(self):
        fp = os.path.dirname(__file__) + '/templates'
        return jinja2.Environment(
            loader=jinja2.FileSystemLoader(fp),
            extensions=['jinja2.ext.autoescape'],
            autoescape=True
        )

    def render(self, template, template_variables={}):
        template = self.jinja2.get_template(template)
        self.response.write(template.render(template_variables))


# class ViewCards(webapp2.RequestHandler):
#     def get(self):
#         template = JINJA_ENVIRONMENT.get_template('modify.html')
#         self.response.write(template.render())
#
#     def post(self):
#         self.response.headers['Content-Type'] = 'text/plain'
#         self.response.write('POST')
