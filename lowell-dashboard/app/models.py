import datetime
from flask import g
from flask_appbuilder._compat import as_unicode
from sqlalchemy import Table, Column, Integer, String, Boolean, DateTime, ForeignKey, Sequence, UniqueConstraint, MetaData
from sqlalchemy.orm import relationship, backref
from flask_appbuilder import Model
from sqlalchemy.ext.declarative import declared_attr
from flask_appbuilder.models.mixins import AuditMixin, FileColumn, ImageColumn

"""

You can use the extra Flask-AppBuilder fields and Mixin's

AuditMixin will add automatic timestamp of created and modified by who


"""

_dont_audit = False
_mt = MetaData()

class CustomPermission(Model):
    __tablename__ = 'ab_permission'
    id = Column(Integer, Sequence('ab_permission_id_seq'), primary_key=True)
    name = Column(String(100), unique=True, nullable=False)

    def __repr__(self):
        return self.name


class CustomViewMenu(Model):
    __tablename__ = 'ab_view_menu'
    id = Column(Integer, Sequence('ab_view_menu_id_seq'), primary_key=True)
    name = Column(String(100), unique=True, nullable=False)

    def __eq__(self, other):
        return (isinstance(other, self.__class__)) and (self.name == other.name)

    def __neq__(self, other):
        return self.name != other.name

    def __repr__(self):
        return self.name


class CustomPermissionView(Model):
    __tablename__ = 'ab_permission_view'
    __table_args__ = (UniqueConstraint('permission_id', 'view_menu_id'),)
    id = Column(Integer, Sequence('ab_permission_view_id_seq'), primary_key=True)
    permission_id = Column(Integer, ForeignKey('ab_permission.id'))
    permission = relationship("CustomPermission")
    view_menu_id = Column(Integer, ForeignKey('ab_view_menu.id'))
    view_menu = relationship("CustomViewMenu")

    def __repr__(self):
        return str(self.permission).replace('_', ' ') + ' on ' + str(self.view_menu)


assoc_permissionview_role = Table('ab_permission_view_role', Model.metadata,
                                  Column('id', Integer, Sequence('ab_permission_view_role_id_seq'), primary_key=True),
                                  Column('permission_view_id', Integer, ForeignKey('ab_permission_view.id')),
                                  Column('role_id', Integer, ForeignKey('ab_role.id')),
                                  UniqueConstraint('permission_view_id', 'role_id')
)

class CustomRole(Model):
    __tablename__ = 'ab_role'

    id = Column(Integer, Sequence('ab_role_id_seq'), primary_key=True)
    name = Column(String(64), unique=True, nullable=False)
    permissions = relationship('CustomPermissionView', secondary=assoc_permissionview_role, backref='role')

    def __repr__(self):
        return self.name


assoc_user_role = Table('ab_user_role', Model.metadata,
                                  Column('id', Integer, Sequence('ab_user_role_id_seq'), primary_key=True),
                                  Column('user_id', Integer, ForeignKey('ab_user.id')),
                                  Column('role_id', Integer, ForeignKey('ab_role.id')),
                                  UniqueConstraint('user_id', 'role_id')
)

class CustomUser(Model):
    __tablename__ = 'ab_user'
    id = Column(Integer, Sequence('ab_user_id_seq'), primary_key=True)
    # NOTE: Missing first_name, last_name properties
    first_name = Column(String(64))
    last_name = Column(String(64))
    username = Column(String(64), unique=True, nullable=False)
    password = Column(String(256))
    active = Column(Boolean)
    email = Column(String(64), unique=True, nullable=False)
    last_login = Column(DateTime)
    login_count = Column(Integer)
    fail_login_count = Column(Integer)
    roles = relationship('CustomRole', secondary=assoc_user_role, backref='user')
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

    created_by = relationship("CustomUser", backref=backref("created", uselist=True),
                              remote_side=[id], primaryjoin='CustomUser.created_by_fk == CustomUser.id', uselist=False)
    changed_by = relationship("CustomUser", backref=backref("changed", uselist=True),
                              remote_side=[id], primaryjoin='CustomUser.changed_by_fk == CustomUser.id', uselist=False)

    @classmethod
    def get_user_id(cls):
        try:
            return g.user.id
        except Exception as e:
            return None

    # NOTE: add property because base model had it
    @property
    def is_authenticated(self):
        return True

    # NOTE: add property because base model had it
    @property
    def is_active(self):
        return self.active

    # NOTE: add property because base model had it
    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return as_unicode(self.id)

    def get_full_name(self):
        return u'{0} {1}'.format(self.first_name, self.last_name)

    def __repr__(self):
        return self.get_full_name()


class CustomRegisterUser(Model):
    __tablename__ = 'ab_register_user'
    id = Column(Integer, Sequence('ab_register_user_id_seq'), primary_key=True)
    # NOTE: Missing first_name, last_name properties
    first_name = Column(String(64))
    last_name = Column(String(64))
    username = Column(String(64), unique=True, nullable=False)
    password = Column(String(256))
    email = Column(String(64), nullable=False)
    registration_date = Column(DateTime, default=datetime.datetime.now, nullable=True)
    registration_hash = Column(String(256))

class CustomNews(Model):
    # __tablename__ = 'ab_news'
    id = Column(Integer, primary_key=True)
    title = Column(String(64))
    news = Column(String(2048))

    def __repr__(self):
        return self.title
