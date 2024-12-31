# trails.py

from flask import abort, make_response
from config import db
from models import Trail, trails_schema, trail_schema

print("Trails.py is run")

def read_all():
    trails_list = Trail.query.all()
    return trails_schema.dump(trails_list)


def create(new_trail):
    trail_name = new_trail.get("Trail_Name")
    existing_trail = Trail.query.filter(Trail.Trail_Name == trail_name).one_or_none()

    if existing_trail is None:
        new_trail_obj = trail_schema.load(new_trail, session=db.session)
        db.session.add(new_trail_obj)
        db.session.commit()
        return trail_schema.dump(new_trail_obj), 201
    else:
        abort(406, f"Trail with name {trail_name} already exists")


def read_one(trail_name):
    trail_obj = Trail.query.filter(Trail.Trail_Name == trail_name).one_or_none()

    if trail_obj is not None:
        return trail_schema.dump(trail_obj)
    else:
        abort(404, f"Trail with name {trail_name} not found")


def update(trail_name, updated_trail):
    existing_trail = Trail.query.filter(Trail.Trail_Name == trail_name).one_or_none()

    if existing_trail:
        update_trail_obj = trail_schema.load(updated_trail, session=db.session)
        existing_trail.Trail_Name = update_trail_obj.Trail_Name
        existing_trail.Trail_Summary = update_trail_obj.Trail_Summary
        existing_trail.Trail_Description = update_trail_obj.Trail_Description
        existing_trail.Difficulty = update_trail_obj.Difficulty
        existing_trail.Location = update_trail_obj.Location
        existing_trail.Length = update_trail_obj.Length
        existing_trail.Elevation_gain = update_trail_obj.Elevation_gain
        existing_trail.Route_type = update_trail_obj.Route_type
        existing_trail.OwnerID = update_trail_obj.OwnerID
        existing_trail.Pt1_Lat = update_trail_obj.Pt1_Lat
        existing_trail.Pt1_Long = update_trail_obj.Pt1_Long
        existing_trail.Pt1_Desc = update_trail_obj.Pt1_Desc
        existing_trail.Pt2_Lat = update_trail_obj.Pt2_Lat
        existing_trail.Pt2_Long = update_trail_obj.Pt2_Long
        existing_trail.Pt2_Desc = update_trail_obj.Pt2_Desc

        db.session.merge(existing_trail)
        db.session.commit()
        return trail_schema.dump(existing_trail), 201
    else:
        abort(404, f"Trail with name {trail_name} not found")


def delete(trail_name):
    existing_trail = Trail.query.filter(Trail.Trail_Name == trail_name).one_or_none()

    if existing_trail:
        db.session.delete(existing_trail)
        db.session.commit()
        return make_response(f"Trail with name {trail_name} successfully deleted", 200)
    else:
        abort(404, f"Trail with name {trail_name} not found")
