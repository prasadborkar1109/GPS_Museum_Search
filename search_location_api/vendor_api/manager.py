import logging
from typing import Dict
from search_location_api.vendor_api import MapboxAPI


class MapboxManager:

    def __init__(self, api_token: str):
        self.logger = logging.getLogger(__name__)
        self.api_token = api_token
        self._mapbox_api = MapboxAPI(self.api_token)

    @property
    def api(self) -> MapboxAPI:
        """Access to low-level API"""
        return self._mapbox_api

    def search_museums_in_proximity(self, lat: str, lng: str) -> Dict:
        data_by_postcode = {}
        resp_json = self._mapbox_api.fetch_museums(lat, lng)
        if resp_json:
            feature_list = resp_json['features']
            for feature in feature_list:
                place = feature['text']
                postcode = next(filter(lambda x: x['id'].startswith('postcode.'), feature['context']))['text']
                if postcode in data_by_postcode.keys():
                    place_list = data_by_postcode[postcode]
                    place_list.append(place)
                    data_by_postcode[postcode] = place_list
                else:
                    data_by_postcode[postcode] = [place]

        return data_by_postcode
