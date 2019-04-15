import logging
import requests
from typing import List


class APIError(Exception):
    pass


class MapboxAPI:
    """
    Mapbox API wrapper
    Main documentation source https://developer.github.com/v3/
    """

    TEMPLATE_API_URL = "https://api.mapbox.com/geocoding/v5/mapbox.places/{search_term}.json?access_token={token}{params}"

    def __init__(self, access_key: str):
        self.logger = logging.getLogger(__name__)
        self.access_key = access_key

    def raw_query(self, search_term: str, params: str, http_method: str = 'GET', data=None):
        url = self.TEMPLATE_API_URL.format(search_term=search_term, token=self.access_key, params=params)
        try:
            response = requests.request(http_method, url, data=data)
            if response.status_code == 403:
                self.logger.info('API rate limit exceeded, need to handle this scenario')

        except Exception as e:
            self.logger.exception("Error occurred while executing request: "+str(e))
            raise APIError('Error occurred while executing request')
        return response

    def fetch_museums(self, lat: str, lng: str) -> List:
        response = self.raw_query(
            'museum', '&proximity={proximity}&types=poi'.format(proximity=lng+','+lat),
        )
        response_json = response.json()
        return response_json
