from models.shared import db
from sqlalchemy.ext.declarative import declarative_base
from flask_jsontools import JsonSerializableBase

# Base = declarative_base(cls=(JsonSerializableBase,))


class Gerecht(db.Model):
    __tablename__ = "gerecht"
    id = db.Column(db.Integer, primary_key=True)
    naam = db.Column(db.String)
    status = db.Column(db.Integer)
    afbeelding = db.Column(db.String)
    prijs = db.Column(db.Integer)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())


