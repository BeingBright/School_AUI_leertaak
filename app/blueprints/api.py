from flask import Blueprint
from flask_jsontools import jsonapi

api = Blueprint('api', 'api', url_prefix='/api')

from models.shared import db
from models.gerecht import Gerecht

@api.route('/gerecht', methods=['GET'])
@jsonapi
def list_gerecht():
    return Gerecht.query.all()


@api.route('/gerecht/<int:id>', methods=['GET'])
@jsonapi
def get_gerecht(id):
    return list_gerecht().get_json()[id]


@api.route('/gerecht/<int:id>', methods=['DELETE'])
def delete_gerecht(id):
    return {'error': 'Access denied'}


@api.route('/tafel', methods=['GET'])
@jsonapi
def list_tafel():
    return [{1: 'first', 2: 'second'}]


@api.route('/tafel/<int:id>', methods=['GET'])
@jsonapi
def get_tafel(id):
    return list_tafel().get_json()[id]


@api.route('/tafel/<int:id>', methods=['DELETE'])
def delete_tafel(id):
    return {'error': 'Access denied'}

