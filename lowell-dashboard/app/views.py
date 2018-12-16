from flask import render_template
from flask_appbuilder import ModelView, AppBuilder, BaseView, expose, has_access
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder.security.registerviews import RegisterUserDBView
from flask_appbuilder.security.sqla.manager import SecurityManager
from app import appbuilder, db
from .tools import retrieve_schedule
"""
    Create your Views::


    class MyModelView(ModelView):
        datamodel = SQLAInterface(MyModel)


    Next, register your Views::


    appbuilder.add_view(MyModelView, "My View", icon="fa-folder-open-o", category="My Category", category_icon='fa-envelope')
"""

# 404 error handeler to render 404.html jijna2 template
@appbuilder.app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', base_template=appbuilder.base_template, appbuilder=appbuilder), 404

# Views for Lowellresources
class LowellResources(BaseView):

    # Top choice for drop down menu
    default_view = 'news'

    # Add route base as root "/"
    route_base = "/"

    '''
    Create path news that renders news.html jijna2 template
    that contains any added news might be moved to models to
    work with database and can only be seen by logged in users
    '''
    @expose('/news')
    @has_access
    def news(self):
        return self.render_template('news.html')

    '''
    Create path textbooks that renders textbooks.html jijna2 template
    that contains any online textbooks availble will probably stay hard coded to add text books
    because not expecting alot of online textbooks to come at a time and can only be seen by logged in users
    '''
    @expose('/textbooks')
    @has_access
    def textbooks(self):
        return self.render_template('textbooks.html')

    '''
    Create path schedules that renders schedules.html jijna2 template
    that contains any added special schedules. Will contain main schedule and year long schedule
    as well as a schedule of the day and can only be seen by logged in users
    '''
    @expose('/schedules')
    @has_access
    def schedules(self):
        schedule = retrieve_schedule.retrieve_schedule()
        print(schedule)
        return self.render_template('schedules.html')

# Create appbuilder dropdown menu
appbuilder.add_view(LowellResources, "News", category='Lowell Resources')

# Create textbook link in drop down menu
appbuilder.add_link("Textbooks", href='/textbooks', category='Lowell Resources')

# Create schedules link in drop down menu
appbuilder.add_link("Schedules", href='/schedules', category='Lowell Resources')

# Views for Site files
class LowellFiles(BaseView):

    # Top choice for drop down menu
    default_view = 'disclaimer'

    # Add route base as root "/"
    route_base = "/"

    '''
    Create path news that renders news.html jijna2 template
    that contains any added news might be moved to models to
    work with database and can only be seen by logged in users
    '''
    @expose('/disclaimer')
    @has_access
    def disclaimer(self):
        return self.render_template('disclaimer.html')

    '''
    Create path textbooks that renders textbooks.html jijna2 template
    that contains any online textbooks availble will probably stay hard coded to add text books
    because not expecting alot of online textbooks to come at a time and can only be seen by logged in users
    '''
    @expose('/license')
    @has_access
    def license(self):
        return self.render_template('license.html')

    '''
    Create path schedules that renders schedules.html jijna2 template
    that contains any added special schedules. Will contain main schedule and year long schedule
    as well as a schedule of the day and can only be seen by logged in users
    '''
    '''
    @expose('/schedules')
    @has_access
    def schedules(self):
        schedule = retrieve_schedule.retrieve_schedule()
        print(schedule)
        return self.render_template('schedules.html')
    '''

# Create appbuilder dropdown menu
appbuilder.add_view(LowellFiles, "Disclaimer", category='Important Files')

# Create textbook link in drop down menu
appbuilder.add_link("License", href='/license', category='Important Files')

# Create schedules link in drop down menu
#appbuilder.add_link("Schedules", href='/schedules', category='Lowell Resources')

# Create any db objects
db.create_all()
