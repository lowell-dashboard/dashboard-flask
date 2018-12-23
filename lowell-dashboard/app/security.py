from flask_babel import lazy_gettext as _
from flask_appbuilder.security.manager import AUTH_OID, AUTH_REMOTE_USER, AUTH_DB, AUTH_LDAP, AUTH_OAUTH
from flask_appbuilder.security.sqla.manager import SecurityManager
from flask_appbuilder.security.registerviews import RegisterUserDBView

# Create Registration system
class MyRegisterUserDBView(RegisterUserDBView):
    email_template = 'register_mail.html'
    email_subject = _('Your Account activation for Lowell Help Forum')
    activation_template = 'activation.html'
    form_title = _('Fill out the registration form for Lowell Help Forum')
    error_message = _('Not possible to register you at the moment, try again later')
    message = _('Registration sent to your email')

# Change roles
class MySecurityManager(SecurityManager):
    registeruserdbview = MyRegisterUserDBView
