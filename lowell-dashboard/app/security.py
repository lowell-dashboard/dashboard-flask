from flask_appbuilder.security.manager import AUTH_OID, AUTH_REMOTE_USER, AUTH_DB, AUTH_LDAP, AUTH_OAUTH
from flask_appbuilder.security.sqla.manager import SecurityManager
from flask_appbuilder.security.registerviews import RegisterUserDBView

# Create Registration system
class MyRegisterUserDBView(RegisterUserDBView):
    email_template = 'register_mail.html'
    email_subject = ('Your Account activation for Lowell Help Forum')
    activation_template = 'activation.html'
    form_title = ('Fill out the registration form')
    error_message = ('Not possible to register you at the moment, try again later')
    message = ('Registration sent to your email')

# Change roles
class MySecurityManager(SecurityManager):
    registeruserdbview = MyRegisterUserDBView
