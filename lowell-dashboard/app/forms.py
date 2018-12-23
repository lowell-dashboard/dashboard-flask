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
