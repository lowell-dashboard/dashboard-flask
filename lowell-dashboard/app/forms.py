from wtforms import Form, StringField, BooleanField, PasswordField, RadioField, TextAreaField
from flask_babel import lazy_gettext as _
from wtforms.validators import DataRequired, EqualTo, Email, Length
from flask_wtf.recaptcha import RecaptchaField
from flask_appbuilder.forms import DynamicForm
from flask_appbuilder.fieldwidgets import BS3PasswordFieldWidget, BS3TextFieldWidget


class bugreportform(DynamicForm):

    name = StringField(_('Name'),
                          description=_('Not Required'),
                          widget=BS3TextFieldWidget()
                          )

    email = StringField(_('Email'),
                          description=_('Not Required'),
                          widget=BS3TextFieldWidget()
                          )

    bug = StringField(_('Bug'),
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
                                  validators=[
                                             EqualTo('password',
                                             message=_('Passwords must match'))
                                             ],
                                  widget=BS3PasswordFieldWidget())

    recaptcha = RecaptchaField()

class CreateNews(DynamicForm):

    title = StringField(_('Title'),
                          validators=[DataRequired()],
                          widget=BS3TextFieldWidget())

    news = TextAreaField(_('News'),
                          render_kw={"rows": 15, "cols": 40},
                          description=_('Please write at least 15 characters and maximum of 300 characters'),
                          validators=[
                                     DataRequired(),
                                     Length(min=15,max=400)
                                     ]
                          )

    rule_check = RadioField(_('Community Guidelines'),
                               description=_('By accepting this you confirm that your post follows the ommunity guidelines. The guidelines are the in the footer of the page'),
                               choices=[('confirm','True'),('deny','False')],
                               validators=[DataRequired()])

    recaptcha = RecaptchaField()
