"""
REST API Resource Routing
http://flask-restplus.readthedocs.io
"""

from flask import request
from flask_restx import Resource

from . import api_rest

from liquidctl.driver import find_liquidctl_devices
from liquidctl.driver.smart_device import SmartDeviceV2Driver
from liquidctl import util


@api_rest.route('/resource/<string:resource_id>')
class Status(Resource):
    """ Unsecure Resource Class: Inherit from Resource """

    def get(self, resource_id):
        status = self._get_status()
        return {'status': status}

    def post(self, resource_id):
        json_payload = request.json
        return {'timestamp': json_payload}, 201

    def _get_smart_driver(self):
        return next((dev for dev in find_liquidctl_devices() if isinstance(dev, SmartDeviceV2Driver)), None)


    def _get_status(self):
        driver = self._get_smart_driver()
        driver.connect()
        return driver.get_status()

