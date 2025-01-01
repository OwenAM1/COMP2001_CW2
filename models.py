# models.py

import pytz
from datetime import datetime
from marshmallow_sqlalchemy import fields

from config import db, ma


class Trail(db.Model):
    __tablename__ = "trail"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    trail_Name = db.Column(db.String(32), unique=True)
    trail_Description = db.Column(db.String(32))
    timestamp = db.Column(
        db.DateTime, default=lambda: datetime.now(pytz.timezone('Europe/London')),
        onupdate=lambda: datetime.now(pytz.timezone('Europe/London'))
    )

class TrailSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Trail
        load_instance = True
        sql_session = db.session
        include_relationships = True

trail_schema = TrailSchema()
trails_schema = TrailSchema(many=True)