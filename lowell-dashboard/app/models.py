# Import check user from flask
from flask import g
# Import datetime for saving time
from datetime import datetime
# Import sqlalchemy for sql work for App
from sqlalchemy import Table, Column, Integer, String, Boolean, DateTime, ForeignKey, Sequence, UniqueConstraint, MetaData
# Import specific sqlalchemy functions for sql work
from sqlalchemy.orm import relationship, backref
# Import base class of Flask App Builder for Models
from flask_appbuilder import Model
# Import specific flask app builder function for encoding
from flask_appbuilder._compat import as_unicode
# Import specific sqlalchemy function for sql work
from sqlalchemy.ext.declarative import declared_attr
# Import Flask App Builder special sql columns
from flask_appbuilder.models.mixins import AuditMixin, FileColumn, ImageColumn

# needed variables
_dont_audit = False
_mt = MetaData()

# Custom Permission db class for possible future permissions
class CustomPermission(Model):
    __tablename__ = 'ab_permission'
    id = Column(Integer, Sequence('ab_permission_id_seq'), primary_key=True)
    name = Column(String(100), unique=True, nullable=False)

    def __repr__(self):
        return self.name

# Custom View Menu for future customizations
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

# Custom Permission View for future customizations
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

# Custom Role model for future customizations
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

# Custom User for changing possible user data
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
    created_on = Column(DateTime, default=datetime.now, nullable=True)
    changed_on = Column(DateTime, default=datetime.now, nullable=True)
    _class_ids = Column(String, default='')

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

    def get_username(self):
        return u'{0}'.format(self.username)

    def __repr__(self):
        return self.get_full_name()

    '''
    A getter function for the class id property
    Args:
        None
    Returns:
        list: a list of the class ids that the student has
    Use case:
    print(CustomUser.class_ids)
    ['12', '27']
    '''
    @property
    def class_ids(self):
        return [int(x) for x in self._class_ids.split(';') if x is not '']

    def add_column(db):
        # create a new column named 'col' and has the type String length 64 characters
        _class_ids = Column('_class_ids', String)
        # save the test column into a variable column
        column = _class_ids
        # create a connection to the db
        conn = db.engine.connect()
        # get the table name of the model
        table_name = CustomUser.__tablename__
        # get the key of the column
        column_name = column.key
        # get the type of the column; this is required by sql syntax
        column_type = column.type.compile(conn.dialect)
        try:
            # log.info("Going to alter Column {0} on {1}".format(column_name, table_name))
            # Using the sql 'ALTER' command to add a new column to the model in the db
            conn.execute('ALTER TABLE %s ADD COLUMN %s %s' % (table_name, column_name, column_type))
            return True
            # log.info("Added Column {0} on {1}".format(column_name, table_name))
        except Exception as e:
            print(e)
            return False
    '''
    A setter for the class id property
    Args:
        str: class id
    Returns:
        void: nothing
    Use case:
    CustomUser.class_ids = 12
    '''
    @class_ids.setter
    def class_ids(self, value):
        if type(value) is list:
            for v in value:
                print(self._class_ids)
                self._class_ids += ';%s' % v
            return
        self._class_ids += ';%s' % value
# Custom Register User for changing possible user data
class CustomRegisterUser(Model):
    __tablename__ = 'ab_register_user'
    id = Column(Integer, Sequence('ab_register_user_id_seq'), primary_key=True)
    # NOTE: Missing first_name, last_name properties
    first_name = Column(String(64))
    last_name = Column(String(64))
    username = Column(String(64), unique=True, nullable=False)
    password = Column(String(256))
    email = Column(String(64), nullable=False)
    registration_date = Column(DateTime, default=datetime.now, nullable=True)
    registration_hash = Column(String(256))

# News model for Saving news post data
class NewsPost(Model):
    __tablename__ = 'news_posts'
    id = Column(Integer, primary_key=True)
    creator_username = Column(String(64), nullable=False)
    title = Column(String(64), nullable=False)
    time_created = Column(DateTime, default=datetime.now, nullable=False)
    news = Column(String(1024))
    made_by_message = Column(String(64))
    # tags = Column(String(128))

    def drop_table(self, db):
        try:
            NewsPost.__table__.drop(db.engine)
            return True
        except Exception as e:
            print(e)
            return False

    def add_column(self, db):
        # create a new column named 'test' and has the type String length 64 characters
        test = Column('made_by_message', String(64))
        # save the test column into a variable column
        column = test
        # create a connection to the db
        conn = db.engine.connect()
        # get the table name of the model
        table_name = NewsPost.__tablename__
        # get the key of the column
        column_name = column.key
        # get the type of the column; this is required by sql syntax
        column_type = column.type.compile(conn.dialect)
        try:
            # log.info("Going to alter Column {0} on {1}".format(column_name, table_name))
            # Using the sql 'ALTER' command to add a new column to the model in the db
            conn.execute('ALTER TABLE %s ADD COLUMN %s %s' % (table_name, column_name, column_type))
            return True
            # log.info("Added Column {0} on {1}".format(column_name, table_name))
        except Exception as e:
            print(e)
            return False
            # log.error("Error adding Column {0} on {1}: {2}".format(column_name, table_name, str(e)))

# Class model for Saving Classes data
class Classes(Model):
    __tablename__ = 'all_classes'
    id = Column(Integer, primary_key=True)
    teacher = Column(String(64))
    course_name = Column(String(64))
    student_grade_levels = Column(String(32))
    block_number = Column(Integer)
    year = Column(Integer)
    course_type = Column(String(64))
    a_g_requirement = Column(String(64))
    _students_ids = Column(String, default='')

    '''
    A getter function for the student id property
    Args:
        None
    Returns:
        list: a list of the students ids that are in the class
    Use case:
    print(Classes.students_ids)
    ['421', '319']
    '''
    @property
    def students_ids(self):
        return [float(x) for x in self._students_ids.split(';')]
    '''
    A setter for the student id property
    Args:
        str: user id
    Returns:
        void: nothing
    Use case:
    Classes.students_ids = 421
    '''
    @students_ids.setter
    def students_ids(self, value):
        self._students_ids += ';%s' % value

    def add_column(db):
        # create a new column named 'col' and has the type String length 64 characters
        _students_ids = Column('_students_ids', String)
        # save the test column into a variable column
        column = _students_ids
        # create a connection to the db
        conn = db.engine.connect()
        # get the table name of the model
        table_name = Classes.__tablename__
        # get the key of the column
        column_name = column.key
        # get the type of the column; this is required by sql syntax
        column_type = column.type.compile(conn.dialect)
        try:
            # log.info("Going to alter Column {0} on {1}".format(column_name, table_name))
            # Using the sql 'ALTER' command to add a new column to the model in the db
            conn.execute('ALTER TABLE %s ADD COLUMN %s %s' % (table_name, column_name, column_type))
            return True
            # log.info("Added Column {0} on {1}".format(column_name, table_name))
        except Exception as e:
            print(e)
            return False
