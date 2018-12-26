from wtforms import Form, StringField, BooleanField, PasswordField
from flask_babel import lazy_gettext as _
from wtforms.validators import DataRequired, EqualTo, Email
from flask_wtf.recaptcha import RecaptchaField
from flask_appbuilder.forms import DynamicForm
from flask_appbuilder.fieldwidgets import BS3PasswordFieldWidget, BS3TextFieldWidget



class bugreportform(DynamicForm):

    field1 = StringField(_('Name'),
                          description=_('Not Required'),
                          widget=BS3TextFieldWidget()
                          )

    field2 = StringField(_('Email'),
                          description=_('Not Required'),
                          widget=BS3TextFieldWidget()
                          )

    field3 = StringField(_('Bug'),
                          description=_('Put the bug report here'),
                          validators = [DataRequired()],
                          widget=BS3TextFieldWidget()
                          )

class CustomRegistration(DynamicForm):

    username = StringField(_('User Name'),
                            validators=[DataRequired()],
                            widget=BS3TextFieldWidget())

    email = StringField(_('Email'),
                         validators=[DataRequired(),
                         Email()],
                         widget=BS3TextFieldWidget())

    password = PasswordField(_('Password'),
                              description=_('Please use a good password policy, this application does not check this for you'),
                              validators=[DataRequired()],
                              widget=BS3PasswordFieldWidget())

    conf_password = PasswordField(_('Confirm Password'),
                                  description=_('Please rewrite the password to confirm'),
                                  validators=[EqualTo('password', message=_('Passwords must match'))],
                                  widget=BS3PasswordFieldWidget())
                                  
    recaptcha = RecaptchaField()
