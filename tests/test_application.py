import unittest
from unittest.mock import Mock, patch
from collections import namedtuple
import requests

from search_location_api.application import app


class TestApplication(unittest.TestCase):

    def setUp(self):
        print('setup called')
        app.config['TESTING'] = True
        self.test_app = app.test_client()

    def tearDown(self):
        pass

    def mock_api_response(self):
        sample_resp_json = {
                          "type": "FeatureCollection",
                          "query": [
                            "museum"
                          ],
                          "features": [
                            {
                              "id": "poi.901943132439",
                              "type": "Feature",
                              "place_type": [
                                "poi"
                              ],
                              "relevance": 1,
                              "properties": {
                                "landmark": True,
                                "wikidata": "Q157003",
                                "category": "history museum, history, historical, museum, tourism",
                                "address": "Lindenstr. 9-14"
                              },
                              "text": "Jüdisches Museum",
                              "place_name": "Jüdisches Museum, Lindenstr. 9-14, Berlin, 10969, Germany",
                              "matching_text": " museum",
                              "matching_place_name": "museum, Lindenstr. 9-14, Berlin, 10969, Germany",
                              "center": [
                                13.395242,
                                52.501945
                              ],
                              "geometry": {
                                "coordinates": [
                                  13.395242,
                                  52.501945
                                ],
                                "type": "Point"
                              },
                              "context": [
                                {
                                  "id": "postcode.10272705063647250",
                                  "text": "10969"
                                },
                                {
                                  "id": "place.14880313158564380",
                                  "short_code": "DE-BE",
                                  "wikidata": "Q64",
                                  "text": "Berlin"
                                },
                                {
                                  "id": "country.10743216036480410",
                                  "short_code": "de",
                                  "wikidata": "Q183",
                                  "text": "Germany"
                                }
                              ]
                            },
                          ],
                          "attribution": ""
                        }
        response = namedtuple('Response', ['json', 'status_code', 'headers'])
        response.json = Mock(return_value=sample_resp_json)
        response.status_code = 200
        response.headers = {**{'Content-Type': "application/json; charset=UTF-8"}, }
        return response

    def test_home_url(self):
        response = self.test_app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'Welcome User')

    def test_search_museums(self):
        """
        Mocking the actual request to vendor mapbox api as we are testing our application api here
        """
        with patch.object(requests, 'request', return_value=self.mock_api_response()):
            response = self.test_app.get('/museums?lat=52.494857&lng=13.437641')
            self.assertEqual(response.status_code, 200)
            self.assertIsNotNone(response)
            self.assertIn('10969', response.json.keys())


if __name__ == "__main__":
    unittest.main()
