# Imports
from app import appbuilder, db
from json import dumps
from flask import render_template, flash, g, make_response, current_app, abort, redirect
from secret import SLACK
from .forms import bugreportform, CreateNews
from requests import post
#from tools.news import
#from json import dumps
from app.tools import retrieve_schedule
from app.tools import wkmonth
from app.models import NewsPost, CustomUser
from flask_babel import lazy_gettext as _
from flask_appbuilder import ModelView, AppBuilder, BaseView, expose, has_access, SimpleFormView, PublicFormView
from flask_appbuilder.models.sqla.interface import SQLAInterface

# 404 error handeler to render 404.html jijna2 template
@appbuilder.app.errorhandler(404)
def page_not_found(e):
    return render_template('404.py', base_template=appbuilder.base_template, appbuilder=appbuilder), 404

# 500 error handeler to render 500.html html file
@appbuilder.app.errorhandler(500)
def page_not_found(e):
    return render_template('500.py')

# Views for Lowellresources
class LowellResources(BaseView):

    # Add route base as root "/"
    route_base = "/"

    '''
    Create path news that renders news.html jijna2 template
    that contains any added news might be moved to models to
    work with database and can only be seen by logged in users
    '''

    @expose('/news/<number>')
    def newsview(self, number='1'):
        if number == '0':
            number = '1'
        num = int(number)
        num_news = 1
        # Get data from db
        news_db_data = db.session.query(NewsPost).order_by(NewsPost.id).all()
        # Create empty list to put reverse order data posts
        news_data = []
        # Reverse list
        for news_posts in reversed(news_db_data):
            news_data.append(news_posts)


        return self.render_template('news.py', news=news_data, timestamps=how_long_ago, time_unit=time_unit)

    '''
    Create path textbooks that renders textbooks.html jijna2 template
    that contains any online textbooks availble will probably stay hard coded to add text books
    because not expecting alot of online textbooks to come at a time and can only be seen by logged in users
    '''
    @expose('/textbooks')
    def textbooks(self):
        return self.render_template('textbooks.py')

    '''
    Create path schedules that renders schedules.html jijna2 template
    that contains any added special schedules. Will contain main schedule and year long schedule
    as well as a schedule of the day and can only be seen by logged in users
    '''
    @expose('/schedules')
    def schedules(self):
        # uncomment if you need to update the schedule json
        # retrieve_schedule.update_schedule()
        codes = wkmonth.week_of_month()
        # print(codes)
        schedule_data = wkmonth.get_schedule_times(codes)
        print(wkmonth.get_week_events())
        return self.render_template('schedules.py', table=schedule_data)

# Create paths
appbuilder.add_view_no_menu(LowellResources())

# Views for Site files
class LowellFiles(BaseView):

    # Add route base as root "/files"
    route_base = "/files"

    '''
    Create path disclaimer that renders disclaimer.py jijna2 template
    that contains project's disclaimer
    '''
    @expose('/disclaimer')
    def disclaimer(self):
        return self.render_template('disclaimer.py')

    '''
    Create path license that renders license.py jijna2 template
    that contains the project's license
    '''
    @expose('/license')
    def license(self):
        return self.render_template('license.py')

    '''
    Create path privacy that renders privacy.py jijna2 template
    that contains the project's privacy policy
    '''
    @expose('/privacy')
    def privacy(self):
        return self.render_template('privacy.py')

# Create paths
appbuilder.add_view_no_menu(LowellFiles())

# Views for any home paths
class HomeView(BaseView):

    # add route base for views as /home
    route_base = "/home"

    # Route for new or logged out users
    @expose('/new')
    def new(self):
        return self.render_template('new_user.py')

    # Route for signed in users or users who want to just view data
    @expose('/general')
    def general(self):
        return self.render_template('my_index.py')

# Add paths
appbuilder.add_view_no_menu(HomeView())

# Views for SEO Site files
class SEOfiles(BaseView):

    # Add route base as root "/"
    route_base = "/"

    '''
    Create path robots.txt that renders robots.txt text file
    that contains project's robots.txt paths
    '''
    @expose('/robots.txt')
    def disclaimer(self):
        robots_txt = render_template('seo/robots.txt')
        return robots_txt

    '''
    Create path sitemap.xml that renders sitemap.xml xml file
    that contains the project's sitemap for SEO
    '''
    @expose('/sitemap.xml')
    def license(self):
        sitemap_xml = render_template('seo/sitemap.xml')
        response = make_response(sitemap_xml)
        response.headers["Content-Type"] = "application/xml"
        return response

# Create paths
appbuilder.add_view_no_menu(SEOfiles())

# Views for SEO Site files
class UserInfo(BaseView):

    # Add route base as root "/"
    route_base = "/"

    '''
    Create path robots.txt that renders robots.txt text file
    that contains project's robots.txt paths
    '''
    @expose('/profile/<user>')
    def disclaimer(self, user):
        if user.is_anonymous:
            return render_template('profile.py')
        user = g.user
        print(user.roles)
        return render_template('profile.py')

# Create paths
appbuilder.add_view_no_menu(UserInfo())

# Views for SEO Site files
class RandomViews(BaseView):

    # Add route base as root "/"
    route_base = "/"

    '''
    Create path robots.txt that renders robots.txt text file
    that contains project's robots.txt paths
    '''
    @expose('/news')
    @expose('/news/')
    def news_redirect(self):
        return redirect('/news/1')

# Create paths
appbuilder.add_view_no_menu(RandomViews())

'''
Form Views
'''

# Bugreport view
class BugReport(PublicFormView):

    # declare form
    form = bugreportform

    # form data
    form_title = 'Bug Report'
    message_success = 'Your Bug Report has been submitted'
    message_fail = 'Your Bug Report couldn\'t be sent'

    # When form is created and viewed
    def form_get(self, form):
        # Set name and email placeholders because fields not requried
        form.name.data = 'Name'
        form.email.data = 'Email'

    # When form is submit
    def form_post(self, form):
        # Get data from fields
        name = form.name.data
        email = form.email.data
        bug_text = form.bug.data

        # Create json for slack message
        slack_data = {
            'text': 'Bug Report from: ' + str(name) + '\nUsername: ' + str(g.user) + '\nUser\'s Email: ' + str(email) + '\nThe Report: ' + str(bug_text),
            'username': 'LHF Bug Reporter',
            'icon_emoji': ':robot_face:'
        }

        # Send post request and get status code
        response = post(SLACK,
                        data=dumps(slack_data),
                        headers={'Content-Type': 'application/json'}
                       )

        # If sent properly success message and error message if not sent
        if response.status_code != 200:
            flash(self.message_fail, 'error')
        else:
            flash(self.message_success, 'info')

# Add form path
appbuilder.add_view_no_menu(BugReport())

# CreateNews view
class News(SimpleFormView):

    # declare form
    form = CreateNews

    # form data
    form_title = 'Create a News Post'
    message_success = 'Your News Post has been created'
    message_fail = 'Your News Post couldn\'t be created'

    # When form is created and viewed
    def form_get(self, form):
        pass

    # When form is submit
    def form_post(self, form):
        # Get data from fields
        title = form.title.data
        news = form.news.data

        # Create the news post
        model = NewsPost()
        model.creator_username = str(g.user)
        model.title = title
        model.news = news
        model.made_by_message = 'Created by '
        # model.tags = dumps([list])
        # NOTE: for some reason this line must remain outside of the try or else the code won't work
        db.session.add(model)
        # Add the model to the database
        try:
            db.session.commit()
            flash(self.message_success, 'info')
        except:
            # flash error
            flash(self.message_fail, 'error')
        # NOTE: comment once deleted table
        # success = model.add_column(db)
        # flash(success, 'info')

# Add form path
appbuilder.add_view_no_menu(News())

# Create any db objects
db.create_all()
