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
		Adds Medthod2 as a link under MyView
			href - john
"""
appbuilder.add_view(MyView, "Method1", category='My View')
appbuilder.add_link("Method2", href='/myview/method2/john', category='My View')
appbuilder.add_link("Method3", href='/myview/method3/john', category='My View')

