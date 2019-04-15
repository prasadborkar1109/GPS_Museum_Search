import os
import yaml
from flask import Flask, request, jsonify, render_template
from .vendor_api import MapboxManager, APIError
from . import paths
from flasgger import Swagger
from flasgger.utils import swag_from

app = Flask(__name__)
swag = Swagger(app=app)

#  Read config data
with open(os.path.join(paths.PATH_CONFIG, 'config.yaml'), 'r') as f:
    config = yaml.load(f)
api_access_key = config['dev']['mapbox_access_token']


@app.route('/')
def api_home():
    return 'Welcome User'


@app.errorhandler(404)
def page_not_found(e):
    return render_template('page_not_found.html')


@swag_from('search_museum.yml', methods=['GET'])
@app.route('/museums', methods=['GET'])
def search_museums_in_proximity():
    try:
        lat = request.args.get('lat')
        lng = request.args.get('lng')
        manager = MapboxManager(api_access_key)
        resp = manager.search_museums_in_proximity(lat, lng)
    except APIError as e:
        err_message = "Error while fetching museum data: " + str(e)
        return jsonify(err_message)
    return jsonify(resp)
