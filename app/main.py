from flask import Flask, send_from_directory

from models.tafel import Tafel
from blueprints.api import api

from models.shared import db
app = Flask(__name__, static_url_path='', static_folder='public')
app.config.from_object('config')

with app.app_context():
    db.init_app(app)
    db.create_all()

# print Tafel


@app.route('/')
def root():
    return send_from_directory('public', 'index.html')


@app.route('/<path:path>')
def static_file(path):
    return app.send_static_file(path)

app.register_blueprint(api)

if __name__ == "__main__":
    app.run()
