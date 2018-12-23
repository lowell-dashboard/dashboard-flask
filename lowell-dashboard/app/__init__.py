import logging
from flask import Flask
from app.index import MyIndexView
from .security import MySecurityManager
from flask_appbuilder import SQLA, AppBuilder


"""
 Logging configuration
"""
logging.basicConfig(format='%(asctime)s:%(levelname)s:%(name)s:%(message)s')
logging.getLogger().setLevel(logging.DEBUG)

app = Flask(__name__)
app.config.from_object('config')
db = SQLA(app)
appbuilder = AppBuilder(app, db.session, indexview=MyIndexView, security_manager_class=MySecurityManager)

from app import views
