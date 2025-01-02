import pytz
from datetime import datetime
from marshmallow_sqlalchemy import fields
#from marshmallow import fields
from config import db, ma


class Trail(db.Model):
    __tablename__ = "TRAIL"
    TrailID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Trail_Name = db.Column(db.String(255), nullable=False)
    Trail_Summary = db.Column(db.Text)
    Trail_Description = db.Column(db.Text)


class TrailSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Trail
        load_instance = True
        sqla_session = db.session
        include_relationships = True



trail_schema = TrailSchema()
trails_schema = TrailSchema(many=True)
