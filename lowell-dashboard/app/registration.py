from flask import flash, redirect, session, url_for, request
from flask_appbuilder.views import expose, PublicFormView
from flask_babel import lazy_gettext as _
from .forms import CustomRegistration
from flask_appbuilder.validators import Unique
from flask_appbuilder._compat import as_unicode
from flask_mail import Mail, Message

# Create Registration system
class MyRegisterUserDBView(PublicFormView):

    # Email html file for registration with activation
    email_template = 'register_mail.html'

    # Activation template for activating acount
    activation_template = 'activation.html'

    # Subject for Email
    email_subject = _('Your Account activation for Lowell Help Forum')

    # Title for form
    form_title = _('Fill out the registration form for Lowell Help Forum')

    # Error message if form has a problem
    error_message = _('Not possible to register you at the moment, try again later')

    # Message for succesful form
    message = _('Registration sent to your email')

    def send_email(self, register_user):
        mail = Mail(self.appbuilder.get_app)
        msg = Message()
        msg.subject = self.email_subject
        url = url_for('.activation', _external=True, activation_hash=register_user.registration_hash)
        msg.html = self.render_template(self.email_template,
                                        url=url,
                                        username=register_user.username,)
        msg.recipients = [register_user.email]
        try:
            mail.send(msg)
        except Exception as e:
            return False
        return True

    def add_registration(self, username, first_name, last_name, email, password=''):
        register_user = self.appbuilder.sm.add_register_user(username, first_name, last_name, email, password)
        if register_user:
            if self.send_email(register_user):
                flash(as_unicode(self.message), 'info')
                return register_user
            else:
                flash(as_unicode(self.error_message), 'danger')
                self.appbuilder.sm.del_register_user(register_user)
                return None

    @expose('/activation/<string:activation_hash>')
    def activation(self, activation_hash):
        """
            Endpoint to expose an activation url, this url
            is sent to the user by email, when accessed the user is inserted
            and activated
        """
        reg = self.appbuilder.sm.find_register_user(activation_hash)
        if not reg:
            flash(as_unicode(self.false_error_message), 'danger')
            return redirect(self.appbuilder.get_url_for_index)
        if not self.appbuilder.sm.add_user(username=reg.username,
                                           email=reg.email,
                                           role=self.appbuilder.sm.find_role(
                                                            self.appbuilder.sm.auth_user_registration_role),
                                           hashed_password=reg.password):
            flash(as_unicode(self.error_message), 'danger')
            return redirect(self.appbuilder.get_url_for_index)
        else:
            self.appbuilder.sm.del_register_user(reg)
            return self.render_template(self.activation_template,
                               username=reg.username,
                               appbuilder=self.appbuilder)

    def add_form_unique_validations(self, form):
        datamodel_user = self.appbuilder.sm.get_user_datamodel
        datamodel_register_user = self.appbuilder.sm.get_register_user_datamodel
        if len(form.username.validators) == 1:
            form.username.validators.append(Unique(datamodel_user, 'username'))
            form.username.validators.append(Unique(datamodel_register_user, 'username'))
        if len(form.email.validators) == 2:
            form.email.validators.append(Unique(datamodel_user, 'email'))
            form.email.validators.append(Unique(datamodel_register_user, 'email'))

class CustomRegisterUserDBView(MyRegisterUserDBView):

    form = CustomRegistration

    redirect_url = '/'

    def form_get(self, form):
        self.add_form_unique_validations(form)

    def form_post(self, form):
        self.add_form_unique_validations(form)
        self.add_registration(username=form.username.data,
                              email=form.email.data,
                              password=form.password.data
                              )
