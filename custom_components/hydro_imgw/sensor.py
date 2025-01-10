import logging
from datetime import timedelta

import homeassistant.helpers.config_validation as cv
import requests
import voluptuous as vol
from homeassistant.components.sensor import (PLATFORM_SCHEMA, ENTITY_ID_FORMAT, SensorEntity, SensorStateClass)
from homeassistant.const import CONF_NAME, UnitOfLength, ATTR_ATTRIBUTION
from homeassistant.helpers.entity import async_generate_entity_id
from homeassistant.helpers.reload import async_setup_reload_service

_LOGGER = logging.getLogger(__name__)

SCAN_INTERVAL = timedelta(minutes=10)

DEFAULT_NAME = 'Hydro IMGW'
CONF_STATION_ID = "station_id"
DOMAIN = "hydro_imgw"
PLATFORMS = ["sensor"]
ATTRIBUTION = 'Data provided by hydro.imgw.pl.'

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Optional(CONF_NAME, default=DEFAULT_NAME): cv.string,
    vol.Required(CONF_STATION_ID): cv.string
})


async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    await async_setup_reload_service(hass, DOMAIN, PLATFORMS)
    station_id = config.get(CONF_STATION_ID)
    name = config.get(CONF_NAME)
    uid = '{}_{}'.format(DEFAULT_NAME, station_id)
    entity_id = async_generate_entity_id(ENTITY_ID_FORMAT, uid, hass=hass)
    async_add_entities([HydroImgwSensor(entity_id, name, station_id)], True)


class HydroImgwSensor(SensorEntity):
    def __init__(self, entity_id, name, station_id):
        self.entity_id = entity_id
        self._platform_name = name
        self._station_id = station_id
        self._data = None
        self._state = None

    @property
    def name(self):
        name = self._station_id if self._data is None else self.extra_state_attributes["name"]
        return '{} - {}'.format(self._platform_name, name)

    @property
    def icon(self):
        return "mdi:waves"

    @property
    def state(self):
        if self._data is not None:
            try:
                self._state = HydroImgwSensor.extractor(self._data, "status.currentState.value")
            except:
                pass
        return self._state

    @property
    def extra_state_attributes(self):
        attr_paths = {
            "current_date": "status.currentState.date",
            "previous_date": "status.previousState.date",
            "alarm_value": "status.alarmValue",
            "warning_value": "status.warningValue",
            "trend": "status.trend",
            "name": "status.description",
            "level": "stateCode",
            "river": "status.river"
        }
        attributes = {ATTR_ATTRIBUTION: ATTRIBUTION}
        for name, json_path in attr_paths.items():
            attr_value = HydroImgwSensor.extractor(self._data, json_path)
            if attr_value is not None:
                attr_value = attr_value if ".date" not in name else datetime.datetime.fromisoformat(attr_value)
                attributes[name] = attr_value
        return attributes

    @property
    def unit_of_measurement(self):
        return UnitOfLength.CENTIMETERS

    def update(self):
        try:
            address = f"https://hydro-back.imgw.pl/station/hydro/status?id={self._station_id}"
            headers = {
                "User-Agent": "Chrome/131.0.0.0"
            }
            request = requests.get(address, timeout=240, headers=headers)
            if request.status_code == 200 and request.content.__len__() > 0:
                self._data = request.json()
        except:
            pass

    @staticmethod
    def extractor(json, path):
        def extractor_arr(json_obj, path_array):
            if path_array[0] not in json_obj:
                return None
            if len(path_array) > 1:
                return extractor_arr(json_obj[path_array[0]], path_array[1:])
            return json_obj[path_array[0]]

        try:
            return extractor_arr(json, path.split("."))
        except:
            return None

    @property
    def state_class(self) -> SensorStateClass:
        return SensorStateClass.MEASUREMENT
