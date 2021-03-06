# Line App for Google App Engine
## Introduction
My friend is an ESL instructor at a community college. After classes, he holds one-to-one question and answer sessions with students. He has a paper list that they sign up on, and he crosses them out one by one as he goes. They wait for him in the computer lab and he walks around to them.

Instead of always having to go back to the master list to see who is next and cross him or her off the list, I thought it might be nice to have a web app that allows students to sign up to the list and teachers to cross them off. Most students and teachers have smartphones, so an iOS app was a logical choice.

This application is implemented using the Ionic framework, which has the benefit of creating mobile applications that can be built on both Android and iOS. This particular project is targeted towards iOS.
## Video
For a brief walkthrough of the features of this application, please see this video:
https://www.dropbox.com/s/23ehi4u8mp15aqd/final-project-video.mp4?dl=0
## API
The base URL for the API calls is: https://project-4-144319.appspot.com

Also, you can point your browser to the above URL to access a simple HTML admin interface for the application.

The API uses all 4 major HTTP verbs. All variables are required unless otherwise stated.
### Get All User Information
GET /api/user

Returns JSON representing all users in the system:

![json](https://raw.githubusercontent.com/kylesezhi/line-app-gae/master/image00.png "json")

### Get One User's Information
GET /api/user/[user ID]

Returns JSON representing the queried user.
### Edit Existing User's Information
POST /api/user/

POST variables:
* first_name - string
* last_name - string
* email - string
* token - admin user token for the user to be changed

Returns JSON representing the updated user.
### Create New User
POST /api/user/

POST variables:
* first_name - string
* last_name - string
* email - string
* password - string
* user_type - 'admin' for teachers or 'user' for students

Returns JSON representing the created user.
### Get All Line Entry Information
GET /api/lineentry

Returns JSON representing all line entries in the system:
* created - string in the form '%d/%m/%y %H:%M'
* user - user ID integer
### Log In
POST /api/login

POST variables:
* password - string
* email - string

Returns JSON with a token that identifies the logged in user. This token must be used for some operations (see below).
### Add User to Line
PUT /api/lineentry/[user ID of user to be added to line]

Returns JSON information about the created line entry:
* created - string in the form '%d/%m/%y %H:%M'
* user - user ID
### Delete Line Entry (Authenticated)
POST /api/lineentry/

POST variables:
* token - must be a token for an administrator account
* lineentry - ID of line entry to be deleted

Returns nothing if successful, 403 for an authentication error.
### Delete User
DELETE /api/user/[user ID]

Returns nothing if successful.
## Mobile Feature
The mobile feature I implemented is the badge number on the icon. It represents the number of students currently in line, and could be useful for teachers who want to monitor how many students they have left at a glance from their iOS home screen.

The implementation used a library called ng-cordova, which glues together AngularJS with Cordova plugins. On iOS, permissions for these notifications must be approved by the user, so we use some boilerplate to set up that initial authentication. More details about this implementation can be found on my How To site: http://web.engr.oregonstate.edu/~bedellk/hello-ionic/5.html
## Account System
I created my account system by hand. Users log in with their email and password, and the API returns to them an HTML-friendly version of the key that is autogenerated by the Google Datastore.

This system works well enough, but it is not secure. A better approach would be a public key system or something like OAuth or similar, which would obscure these secrets behind cryptography.
## Conclusion
As a project for this class, this application was built to fulfill the requirements for a RESTful-like API that shows competency in writing applications for mobile using a web API.

For the purposes of my friend the teacher, this application should prove useful with the addition of support for student logins (they were not implemented in this version due to time constraints). From a technical standpoint the application should improve its security for user authentication. Passwords are passed in the open, and tokens are easily decipherable to entities saved in the datastore.
