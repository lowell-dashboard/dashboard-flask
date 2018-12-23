import datetime
from flask import g
from flask_appbuilder._compat import as_unicode
from sqlalchemy import Table, Column, Integer, String, Boolean, DateTime, ForeignKey, Sequence, UniqueConstraint
from sqlalchemy.orm import relationship, backref
from flask_appbuilder import Model
from sqlalchemy.ext.declarative import declared_attr
from flask_appbuilder.models.mixins import AuditMixin, FileColumn, ImageColumn

"""

You can use the extra Flask-AppBuilder fields and Mixin's

AuditMixin will add automatic timestamp of created and modified by who


"""
