import os
import unittest
import json
import requests
from random import randint


APIKEY = os.environ['apikey']


class TestAPI(unittest.TestCase):
    def test_response_api(self):
        response = requests.get(
            "https://www.rijksmuseum.nl/api/en/collection/?key=" +
            APIKEY +
            "&format=json&imgonly=True&ps=1&p=" +
            str(randint(1, 10000))
        )
        self.assertEqual(200, response.status_code)

    def test_json_contents(self):
        response = requests.get(
            "https://www.rijksmuseum.nl/api/en/collection/?key=" +
            APIKEY +
            "&format=json&imgonly=True&ps=1&p=" +
            str(randint(1, 10000))
        )
        data = json.loads(response.text)
        self.assertIn('artObjects', data)


if __name__ == '__main__':
    unittest.main()
