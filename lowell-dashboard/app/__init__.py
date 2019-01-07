# Import logging for showing what occurs
import logging
# Import Flask for flask app object
from flask import Flask
# Import Custom Index view
from app.index import MyIndexView
# Import Custom Security Manager
from .security import SecurityManager
# Import Flask appbuilder functions to create the appbuilder object
from flask_appbuilder import SQLA, AppBuilder


"""
 Logging configuration
"""
logging.basicConfig(format='%(asctime)s:%(levelname)s:%(name)s:%(message)s')
logging.getLogger().setLevel(logging.DEBUG)

# Create flask app object
app = Flask(__name__)

# Get Configs from config.py
app.config.from_object('config')

# Create Database object frmo flask app object
db = SQLA(app)

# Create Appbuilder object from db and flask app object and customized classes
appbuilder = AppBuilder(app, db.session, indexview=MyIndexView, security_manager_class=SecurityManager)

# Import views for running app
from app import views
