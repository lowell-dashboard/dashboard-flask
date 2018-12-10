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

class LowellResources(BaseView):

    default_view = 'news'
    route_base = "/"

    @expose('/news')
    @has_access
    def news(self):
        return self.render_template('news.html')

    @expose('/textbooks')
    @has_access
    def textbooks(self):
        return self.render_template('textbooks.html')

    @expose('/schedules')
    @has_access
    def schedules(self):
        return self.render_template('schedules.html')

db.create_all()
appbuilder.add_view(LowellResources, "News", category='Lowell Resources')
appbuilder.add_link("Textbooks", href='/textbooks', category='Lowell Resources')
appbuilder.add_link("Schedules", href='/schedules', category='Lowell Resources')
