from wtforms import Form, StringField
from wtforms.validators import DataRequired
from flask_appbuilder.forms import DynamicForm
from flask_appbuilder.fieldwidgets import BS3TextFieldWidget


class bugreportform(DynamicForm):

    field1 = StringField(('Name'),
                          description=('Not Required'),
                          widget=BS3TextFieldWidget()
                          )

    field2 = StringField(('Email'),
                          description=('Not Required'),
                          widget=BS3TextFieldWidget()
                          )

    field3 = StringField(('Bug'),
                          description=('Put the bug report here'),
                          validators = [DataRequired()],
                          widget=BS3TextFieldWidget()
                          )
