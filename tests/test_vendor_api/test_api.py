import unittest
from search_location_api.vendor_api import MapboxAPI


class TestAPI(unittest.TestCase):

    def setUp(self):
        print('setup called')
        self.api = MapboxAPI('api_key')

    def tearDown(self):
        pass

    def test_search_api(self):
        resp_json = self.api.fetch_museums('52.494857', '13.437641')
        self.assertIsNotNone(resp_json)
        self.assertEqual(resp_json['message'], 'Not Authorized - Invalid Token')


if __name__ == "__main__":
    unittest.main()
