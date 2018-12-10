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

    default_view = 'news'
    route_base = "/"

    @expose('/news')
    @has_access
    def news(self):
        return self.render_template('news.html')

db.create_all()
appbuilder.add_view(MyView, "News", category='Lowell Information')
#appbuilder.add_link("Method2", href='/method2/john', category='Lowell Information')
#appbuilder.add_link("News", href='/news', category='Lowell Information')
