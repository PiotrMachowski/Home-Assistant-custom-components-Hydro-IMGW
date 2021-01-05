from datetime import timedelta
import logging
import homeassistant.helpers.config_validation as cv
import requests
import voluptuous as vol

from homeassistant.components.sensor import (PLATFORM_SCHEMA, ENTITY_ID_FORMAT)
from homeassistant.const import CONF_NAME, LENGTH_CENTIMETERS
from homeassistant.helpers.entity import Entity
from homeassistant.helpers.entity import async_generate_entity_id

_LOGGER = logging.getLogger(__name__)

SCAN_INTERVAL = timedelta(minutes=10)

DEFAULT_NAME = 'Hydro IMGW'
CONF_STATION_ID = "station_id"

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Optional(CONF_NAME, default=DEFAULT_NAME): cv.string,
    vol.Required(CONF_STATION_ID): cv.string
})


def setup_platform(hass, config, add_entities, discovery_info=None):
    station_id = config.get(CONF_STATION_ID)
    name = config.get(CONF_NAME)
    uid = '{}_{}'.format(DEFAULT_NAME, station_id)
    entity_id = async_generate_entity_id(ENTITY_ID_FORMAT, uid, hass=hass)
    add_entities([HydroImgwSensor(entity_id, name, station_id)], True)


class HydroImgwSensor(Entity):
    def __init__(self, entity_id, name, station_id):
        self.entity_id = entity_id
        self._platform_name = name
        self._station_id = station_id
        self._data = None
        self._state = None

    @property
    def name(self):
        name = self._station_id if self._data is None else self.device_state_attributes["name"]
        return '{} - {}'.format(self._platform_name, name)

    @property
    def icon(self):
        return "mdi:waves"

    @property
    def state(self):
        if self._data is not None:
            self._state = HydroImgwSensor.extractor(self._data, "status.currentState.value")
        return self._state

    @property
    def device_state_attributes(self):
        attr_paths = {
            "current_date": "status.currentState.date",
            "previous_date": "status.previousState.date",
            "alarm_value": "alarmValue",
            "warning_value": "warningValue",
            "high_value": "highValue",
            "low_value": "lowValue",
            "trend": "trend",
            "name": "name",
            "state": "state",
            "river": "status.river"
        }
        attributes = {}
        for name, json_path in attr_paths.items():
            attributes[name] = HydroImgwSensor.extractor(self._data, json_path)
        return attributes

    @property
    def unit_of_measurement(self):
        return LENGTH_CENTIMETERS

    def update(self):
        address = 'https://hydro.imgw.pl/api/station/hydro/?id={}'.format(self._station_id)
        headers = {
            "host": "hydro.imgw.pl"
        }
        request = requests.get(address, headers=headers)
        if request.status_code == 200 and request.content.__len__() > 0:
            self._data = request.json()

    @staticmethod
    def extractor(json, path):
        def extractor_arr(json_obj, path_array):
            if len(path_array) > 1:
                return extractor_arr(json_obj[path_array[0]], path_array[1:])
            return json_obj[path_array[0]]

        return extractor_arr(json, path.split("."))
