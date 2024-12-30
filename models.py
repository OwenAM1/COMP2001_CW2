# models.py

from config import db

class Trail(db.Model):
    __tablename__ = "trail"
    
    TrailID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Trail_Name = db.Column(db.String(255), nullable=False)
    Trail_Summary = db.Column(db.String(255), nullable=False)
    Trail_Description = db.Column(db.Text, nullable=True)
    Difficulty = db.Column(db.String(50), nullable=False)
    Location = db.Column(db.String(100), nullable=False)
    Length = db.Column(db.Numeric, nullable=False)
    Elevation_gain = db.Column(db.Numeric, nullable=False)
    Route_type = db.Column(db.String(50), nullable=False)
    OwnerID = db.Column(db.Integer, nullable=False)
    Pt1_Lat = db.Column(db.Numeric, nullable=False)
    Pt1_Long = db.Column(db.Numeric, nullable=False)
    Pt1_Desc = db.Column(db.String(255), nullable=True)
    Pt2_Lat = db.Column(db.Numeric, nullable=False)
    Pt2_Long = db.Column(db.Numeric, nullable=False)
    Pt2_Desc = db.Column(db.String(255), nullable=True)

    def __repr__(self):
        return f"<trail {self.Trail_Name}>"

# Example Schema using Marshmallow
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields

class trailSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Trail
        load_instance = True
        sqla_session = db.session

    # If you have relationships, they can be added here.
