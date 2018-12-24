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

class User(Model):
    __tablename__ = 'ab_user'
    id = Column(Integer, Sequence('ab_user_id_seq'), primary_key=True)
    username = Column(String(64), unique=True, nullable=False)
    password = Column(String(256))
    active = Column(Boolean)
    email = Column(String(64), unique=True, nullable=False)
    last_login = Column(DateTime)
    login_count = Column(Integer)
    fail_login_count = Column(Integer)
    roles = relationship('Role', secondary=assoc_user_role, backref='user')
    created_on = Column(DateTime, default=datetime.datetime.now, nullable=True)
    changed_on = Column(DateTime, default=datetime.datetime.now, nullable=True)

    @declared_attr
    def created_by_fk(self):
        return Column(Integer, ForeignKey('ab_user.id'),
                      default=self.get_user_id, nullable=True)

    @declared_attr
    def changed_by_fk(self):
        return Column(Integer, ForeignKey('ab_user.id'),
                      default=self.get_user_id, nullable=True)

    created_by = relationship("User", backref=backref("created", uselist=True),
                              remote_side=[id], primaryjoin='User.created_by_fk == User.id', uselist=False)
    changed_by = relationship("User", backref=backref("changed", uselist=True),
                              remote_side=[id], primaryjoin='User.changed_by_fk == User.id', uselist=False)

    @classmethod
    def get_user_id(cls):
        try:
            return g.user.id
        except Exception as e:
            return None

    def is_authenticated(self):
        return True

    def is_active(self):
        return self.active

    def is_anonymous(self):
        return False

    def get_id(self):
        return as_unicode(self.id)

    def get_full_name(self):
        return u'{0} {1}'.format(self.first_name, self.last_name)

    def __repr__(self):
        return self.get_full_name()


class RegisterUser(Model):
    __tablename__ = 'ab_register_user'
    id = Column(Integer, Sequence('ab_register_user_id_seq'), primary_key=True)
    username = Column(String(64), unique=True, nullable=False)
    password = Column(String(256))
    email = Column(String(64), nullable=False)
    registration_date = Column(DateTime, default=datetime.datetime.now, nullable=True)
    registration_hash = Column(String(256))
