from flask import render_template
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView, AppBuilder, BaseView, expose, has_access
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

class MyView(BaseView):

    default_view = 'method1'
    route_base = "/myview"

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
        # and render template with param
        param1 = 'Goodbye %s' % (param1)
        return param1

    @expose('/news/')
    @has_access
    def method3(self):
        return self.render_template('news.html')

db.create_all()
appbuilder.add_view(MyView, "Lowell Information", category='lowellinfo')
appbuilder.add_link("Method2", href='/myview/method2/john', category='lowellinfo')
appbuilder.add_link("News", href='/myview/news/', category='lowellinfo')
