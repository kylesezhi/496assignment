import webapp2
import base_page
from google.appengine.ext import ndb
import db_definitions
from datetime import datetime


class Admin(base_page.BaseHandler):
    def render(self, page):
        self.template_variables['users'] = [x.return_dict() for x in db_definitions.User.query(ancestor=ndb.Key(db_definitions.User, self.app.config.get('user-group'))).fetch()]
        self.template_variables['admins'] = [x.return_dict() for x in db_definitions.User.query(ancestor=ndb.Key(db_definitions.User, self.app.config.get('admin-group'))).fetch()]
        self.template_variables['lineentries'] = []
        lineentries = [x.return_dict() for x in db_definitions.LineEntry.query(ancestor=ndb.Key(db_definitions.LineEntry, self.app.config.get('default-group'))).fetch()]
        for line in lineentries: # TODO abstract out to helper function
            d = next((item for item in self.template_variables['users'] if item["key"] == line['user']), None)
            if d is not None: d['created'] = line['created']
            # d['created'] = line['created']
            self.template_variables['lineentries'].append(d)
        # print('DEBUG')
        # print (lineentries)
        base_page.BaseHandler.render(self, page, self.template_variables)
        
    def get(self):
        self.render('admin.html')

    def post(self):
        action = self.request.get('action')
        if action == 'add_user':
            if db_definitions.User.query(db_definitions.User.email == self.request.get('email')).fetch():
                self.template_variables['message'] = 'Error: that account already exists.'
            else:
                k = ndb.Key(db_definitions.User, self.app.config.get(self.request.get('user_type') + '-group'))
                user = db_definitions.User(parent=k)
                user.first_name = self.request.get('first_name')
                user.last_name = self.request.get('last_name')
                user.email = self.request.get('email')
                user.password = self.request.get('password')
                user.classes = [ndb.Key(urlsafe=x) for x in self.request.get_all('classes[]')]
                user.put()
                self.template_variables['message'] = 'Added ' + user.first_name + ' ' + user.last_name + '.'
            self.render('admin.html')
        elif action == 'edit_user':
            key = ndb.Key(urlsafe=self.request.get('key'))
            user = key.get()
            user.first_name = self.request.get('first_name')
            user.last_name = self.request.get('last_name')
            user.email = self.request.get('email')
            user.classes = [ndb.Key(urlsafe=x) for x in self.request.get_all('classes[]')]
            user.put()
            self.template_variables['message'] = 'Updated ' + user.first_name + ' ' + user.last_name + '.'
            self.render('admin.html')
        elif action == 'add_class':
            if db_definitions.UserClass.query(db_definitions.UserClass.name == self.request.get('name')).fetch():
                self.template_variables['message'] = 'Error: that class already exists.'
            else:
                k = ndb.Key(db_definitions.UserClass, self.app.config.get('default-group'))
                user_class = db_definitions.UserClass(parent=k)
                user_class.name = self.request.get('name')
                user_class.put()
                self.template_variables['message'] = 'Added ' + user_class.name + '.'
            self.render('admin.html')
        elif action == 'add_line_entry': # TODO restrict multiple student addition to list
            user_key = ndb.Key(urlsafe=self.request.get('key'))
            # print("DEBUG")
            # print(user_key)
            # call here TODO
            user = user_key.get()
            line_key = ndb.Key(db_definitions.LineEntry, self.app.config.get('default-group'))
            line = db_definitions.LineEntry(parent=line_key)
            line.user = user_key
            line.put()
            self.template_variables['message'] = 'Added ' + user.first_name + ' ' + user.last_name + ' to the line.'
            self.render('admin.html')
        else:
            self.template_variables['message'] = action + ' is unknown.'
            self.render('admin.html')
