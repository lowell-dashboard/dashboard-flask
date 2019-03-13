from app import db
from app.models import *
import random
from datetime import datetime

q = db.session.query(CustomUser).get((1))
q.class_ids = ['1', '3', '4', '5']
print(q.class_ids)
db.session.commit()

classes = Classes()
classes.teacher = 'Mr. Simon'
classes.course_name = 'Geometry'
classes.student_grade_levels = '9th'
classes.block_number = 3
classes.year = 2019
classes.course_type = 'Math'
classes.a_g_requirement = 'A'
classes._students_ids = ''
db.session.add(classes)
db.session.commit()
