# models.py

import pytz
from datetime import datetime
from marshmallow_sqlalchemy import fields, SQLAlchemyAutoSchema
from marshmallow import fields
from config import db, ma

print("models.py runs")

class User(db.Model):
    __tablename__ = "USER"
    UserID = db.Column(db.Integer, primary_key=True)
    Email_address = db.Column(db.String(255), nullable=False, unique=True)
    Role = db.Column(db.String(50), nullable=False)

class Trail(db.Model):
    __tablename__ = "TRAIL"
    TrailID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Trail_Name = db.Column(db.String(255), nullable=False)
    Trail_Summary = db.Column(db.Text)
    Trail_Description = db.Column(db.Text)
    Difficulty = db.Column(db.String(50))
    Location = db.Column(db.String(255))
    Length = db.Column(db.Numeric)
    Elevation_gain = db.Column(db.Numeric)
    Route_type = db.Column(db.String(50))
    OwnerID = db.Column(db.Integer, db.ForeignKey("USER.UserID"))
    Pt1_Lat = db.Column(db.Numeric)
    Pt1_Long = db.Column(db.Numeric)
    Pt1_Desc = db.Column(db.Text)
    Pt2_Lat = db.Column(db.Numeric)
    Pt2_Long = db.Column(db.Numeric)
    Pt2_Desc = db.Column(db.Text)

    print("trail is run")

    # Establish relationship with TRAIL_FEATURE
    trail_features = db.relationship(
        "TrailFeature",
        backref="Trail",
        cascade="all, delete, delete-orphan"
    )

class Feature(db.Model):
    __tablename__ = "FEATURE"
    Trail_FeatureID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Trail_Feature = db.Column(db.String(255), nullable=False)

class TrailFeature(db.Model):
    __tablename__ = "TRAIL_FEATURE"
    TrailID = db.Column(db.Integer, db.ForeignKey("TRAIL.TrailID"), primary_key=True)
    Trail_FeatureID = db.Column(db.Integer, db.ForeignKey("FEATURE.Trail_FeatureID"), primary_key=True)

# Marshmallow Schemas
class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
        sqla_session = db.session

class TrailSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Trail
        load_instance = True
        sqla_session = db.session
        include_relationships = True

    trail_features = fields.Nested("TrailFeatureSchema", many=True)

class FeatureSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Feature
        load_instance = True
        sqla_session = db.session

class TrailFeatureSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = TrailFeature
        load_instance = True
        sqla_session = db.session
        include_fk = True

# Schema Instances
user_schema = UserSchema()
users_schema = UserSchema(many=True)

trail_schema = TrailSchema()  # This is the instance for a single trail
trails_schema = TrailSchema(many=True)  # This is the instance for multiple trails

feature_schema = FeatureSchema()
features_schema = FeatureSchema(many=True)

trail_feature_schema = TrailFeatureSchema()
trail_features_schema = TrailFeatureSchema(many=True)
