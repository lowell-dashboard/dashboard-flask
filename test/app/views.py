from flask import render_template
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView
from app import appbuilder, db

"""
    Create your Views::


    class MyModelView(ModelView):
        datamodel = SQLAInterface(MyModel)


    Next, register your Views::


    appbuilder.add_view(MyModelView, "My View", icon="fa-folder-open-o", category="My Category", category_icon='fa-envelope')
"""

"""
    Application wide 404 error handler
"""
@appbuilder.app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', base_template=appbuilder.base_template, appbuilder=appbuilder), 404

db.create_all()

from flask_appbuilder import AppBuilder, expose, BaseView, has_access
from app import appbuilder

"""
	Adds a BaseView to the appbuilder

	AppBuilder: appbuilder

	Base: MyView
		url-paths: [
				/method1/<string:param1>,
				/method2/<string:param1>
				]

"""
class MyView(BaseView):
    # route_base = "/myview"
    default_view = 'method1'

    """
    @expose
    	param: 
    		url – Relative URL for the view
    		methods – Allowed HTTP methods. By default only GET is allowed.
    """
    """
    @has_access
    	decorator to tell flask that this is a security protected method.
    """
    @expose('/method1/')
    @has_access
    def method1(self):
        # do something with param1
        # and return to previous page or index
        return 'Hello'

    @expose('/method2/<string:param1>')
    @has_access
    def method2(self, param1):
        # do something with param1
        # and render it
        param1 = 'Hello %s' % (param1)
        return param1

    @expose('/method3/<string:param1>')
    @has_access
    def method3(self, param1):
        # do something with param1
        # and render template with param
        param1 = 'Goodbye %s' % (param1)
        """
        func: update_redirect()
        	inserts the current url into the navigation history
        	helps with avoid sending the same form again

        """
        self.update_redirect()
        return self.render_template('method3.html',
                               param1 = param1)
# appbuilder.add_view_no_menu(MyView())
"""
Adds a view: MyView
	Creates a tab on the menu bar called My View
		Adds Method1 under My View
		Adds Method2 as a link under MyView
			href - john
		Adds Method3 as a link under MyView
"""
appbuilder.add_view(MyView, "Method1", category='My View')
appbuilder.add_link("Method2", href='/myview/method2/john', category='My View')
appbuilder.add_link("Method3", href='/myview/method3/john', category='My View')

from flask import render_template, flash
from flask_appbuilder import SimpleFormView
from flask_babel import lazy_gettext as _
from .forms import MyForm

"""
SimpleFormView: MyFormView
	# NOTE: must inculde the following vars
	WTForm: form
	String: form_title
	String: Message 

	form_get:
		params : [
				form
				]
	form_post:
		params : [
				form
				]
"""
class MyFormView(SimpleFormView):
    form = MyForm
    form_title = 'This is my first form view'
    message = 'My form submitted'

    """
    form_get:
    	use to prefill the form data
    	preprocess something on the application
    """
    def form_get(self, form):
        form.field1.data = 'This was prefilled'

    """
    for_post
    	post process the form after the user submits it
    	you can save it to the database
    	send an email
    	or any other action
    """
    def form_post(self, form):
        # post process form
        flash(self.message, 'info')

appbuilder.add_view(MyFormView, "My form View", icon="fa-group", label=_('My form View'),
                     category="My Forms", category_icon="fa-cogs")

from flask_appbuilder import ModelView
from flask_appbuilder.models.sqla.interface import SQLAInterface
from .models import ContactGroup, Contact

class ContactModelView(ModelView):
    datamodel = SQLAInterface(Contact)

    """
    label_columns - defines the labels for your columns. The framework will define the missing ones for you, with a pretty version of your column names.
    show_fieldsets - A fieldset (Django style). You can use show_fieldsets, add_fieldsets, edit_fieldsets customize the show, add and edit views independently.
    """
    label_columns = {'contact_group':'Contacts Group'}
    list_columns = ['name','personal_cellphone','birthday','contact_group']

    show_fieldsets = [
                        (
                            'Summary',
                            {'fields':['name','address','contact_group']}
                        ),
                        (
                            'Personal Info',
                            {'fields':['birthday','personal_phone','personal_cellphone'],'expanded':False}
                        ),
                     ]

"""
ModelView: GroupModelView
	SQLAInterface: datamodel
	[ContactModelView]: related_view
"""
class GroupModelView(ModelView):
    """
    datamodel:
    	the db abstraction layer.
    	initialize it with your view's model
    """
    datamodel = SQLAInterface(ContactGroup)
    """
    related_views:
        if you want a master/detail view on the show and edit. 
        FAB will relate 1/N relations automatically, it will display a show or edit view with tab(or accordion) with a list related record. 
        you can relate charts also
    """
    related_views = [ContactModelView]

db.create_all()
appbuilder.add_view(GroupModelView,
                    "List Groups",
                    icon = "fa-folder-open-o",
                    category = "Contacts",
                    category_icon = "fa-envelope")
appbuilder.add_view(ContactModelView,
                    "List Contacts",
                    icon = "fa-envelope",
                    category = "Contacts")	

from flask_appbuilder import MultipleView

"""
MultipleView: MultipleViewsExp
	[GroupModelView, ContactModelView]: views
"""
class MultipleViewsExp(MultipleView):
    views = [GroupModelView, ContactModelView]

appbuilder.add_view(MultipleViewsExp,
                    "Multiple Views",
                    icon="fa-envelope",
                    category="Contacts")	
