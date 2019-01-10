# Import form and form fields for forms
from wtforms import Form, StringField, BooleanField, PasswordField, RadioField, TextAreaField
# Import babel for translations
from flask_babel import lazy_gettext as _
# Import Form validators for forms
from wtforms.validators import DataRequired, EqualTo, Email, Length
# Import wtform recaptcha for registration and protect against bot posting
from flask_wtf.recaptcha import RecaptchaField
# Import Flask App Builder Form helper class
from flask_appbuilder.forms import DynamicForm
# Import Flask app builder Widgets
from flask_appbuilder.fieldwidgets import BS3PasswordFieldWidget, BS3TextFieldWidget


# Bug Report Form
class bugreportform(DynamicForm):

    # Get name not required
    name = StringField(_('Name'),
                          description=_('Not Required'),
                          widget=BS3TextFieldWidget()
                          )

    # Get email not required
    email = StringField(_('Email'),
                          description=_('Not Required'),
                          widget=BS3TextFieldWidget()
                          )

    # Get Bug that is being reported, required
    bug = StringField(_('Bug'),
                          description=_('Put the bug report here'),
                          validators = [DataRequired()],
                          widget=BS3TextFieldWidget()
                          )

# Customized Registration
class CustomRegistration(DynamicForm):

    # Get username for User, required
    username = StringField(_('User Name'),
                            validators=[DataRequired()],
                            widget=BS3TextFieldWidget())

    # Get email for activation, required
    email = StringField(_('Email'),
                         validators=[DataRequired(),
                         Email()],
                         widget=BS3TextFieldWidget())

    # Get password for user, required
    password = PasswordField(_('Password'),
                              description=_('Please use a good password policy, this application does not check this for you'),
                              validators=[DataRequired()],
                              widget=BS3PasswordFieldWidget())

    # Confirm password, required
    conf_password = PasswordField(_('Confirm Password'),
                                  description=_('Please rewrite the password to confirm'),
                                  validators=[
                                             EqualTo('password',
                                             message=_('Passwords must match'))
                                             ],
                                  widget=BS3PasswordFieldWidget())

    # Recaptcha for fighting bots, required
    recaptcha = RecaptchaField()

# Creating news for Site
class CreateNews(DynamicForm):

    # Get title for News post, required
    title = StringField(_('Title'),
                          validators=[DataRequired()],
                          widget=BS3TextFieldWidget())

    # Get the news for the News post, required
    news = TextAreaField(_('News'),
                          render_kw={"rows": 15, "cols": 40},
                          description=_('Please write at least 15 characters and maximum of 400 characters'),
                          validators=[
                                     DataRequired(),
                                     Length(min=15,max=400)
                                     ]
                          )

    # Confirm that use accepts that post follows guidelines, required
    rule_check = RadioField(_('Community Guidelines'),
                               description=_('By accepting this you confirm that your post follows the ommunity guidelines. The guidelines are the in the footer of the page'),
                               choices=[('confirm','True'),('deny','False')],
                               validators=[DataRequired()])

    # Recaptcha for fighting bots, required
    recaptcha = RecaptchaField()
