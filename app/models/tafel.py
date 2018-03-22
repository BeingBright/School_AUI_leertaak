from models.gerecht import Gerecht
from models.shared import db

association_table = db.Table('besteldeGerechten', db.metadata,
                             db.Column('gerecht_id', db.Integer, db.ForeignKey('tafel.id')),
                             db.Column('tafel_id', db.Integer, db.ForeignKey(Gerecht.id)),
                             db.Column('status', db.Integer)
                             )


class Tafel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tafelnummer = db.Column(db.Integer)
    gerechten = db.relationship("Gerecht", secondary=association_table)
