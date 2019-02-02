from app import db
from app.models import *
import random
from datetime import datetime

q = db.session.query(CustomUser).get((1))
q.class_ids = ['1', '3', '4', '5']
print(q.class_ids)
db.session.commit()