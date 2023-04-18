from . import db
from datetime import datetime


class Notes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    time = db.Column(db.DateTime, default=datetime.utcnow())