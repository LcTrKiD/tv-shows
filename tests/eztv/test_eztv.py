import unittest

import responses

from lib.eztvtools import EZTVTools
import tests.eztv.eztvcommons as commons


class TestEZTVTools(unittest.TestCase):
    @responses.activate
    def test_eztv_get_torrents(self):
        imdb_id = 1234567890123456780
        responses.add(**{
                      'method': responses.GET,
                      'url': f'{commons.EZTV_URL}{imdb_id}',
                      'json': commons.JSON_EZTV_PAGE1,
                      'status': 200,
                      'content_type': 'application/json',
                      })

        eztv = EZTVTools(imdb_id)
        response = eztv._get_torrents()
        self.assertEqual(commons.JSON_EZTV_PAGE1, response)

    @responses.activate
    def test_get_magnet_url_with_quality(self):
        imdb_id = 234567890123456780
        responses.add(**{
                      'method': responses.GET,
                      'url': f'{commons.EZTV_URL}{imdb_id}',
                      'json': commons.JSON_EZTV_PAGE1,
                      'status': 200,
                      'content_type': 'application/json',
                      })
        responses.add(**{
                      'method': responses.GET,
                      'url': f'{commons.EZTV_URL}{imdb_id}&page=1',
                      'json': commons.JSON_EZTV_PAGE1,
                      'status': 200,
                      'content_type': 'application/json',
                      })
        responses.add(**{
                      'method': responses.GET,
                      'url': f'{commons.EZTV_URL}{imdb_id}&page=2',
                      'json': commons.JSON_EZTV_PAGE2,
                      'status': 200,
                      'content_type': 'application/json',
                      })
        responses.add(**{
                      'method': responses.GET,
                      'url': f'{commons.EZTV_URL}{imdb_id}&page=3',
                      'json': commons.JSON_EZTV_PAGE3,
                      'status': 200,
                      'content_type': 'application/json',
                      })
        test_magnet = commons.TEST_MAGNET_720P
        eztv = EZTVTools(imdb_id, '2', '5', '720p')
        magnet_url = eztv._get_magnet_url()
        self.assertEqual(test_magnet, magnet_url)

    @responses.activate
    def test_get_magnet_url(self):
        imdb_id = 234567890123456780
        responses.add(**{
                      'method': responses.GET,
                      'url': f'{commons.EZTV_URL}{imdb_id}',
                      'json': commons.JSON_EZTV_PAGE1,
                      'status': 200,
                      'content_type': 'application/json',
                      })
        responses.add(**{
                      'method': responses.GET,
                      'url': f'{commons.EZTV_URL}{imdb_id}&page=1',
                      'json': commons.JSON_EZTV_PAGE1,
                      'status': 200,
                      'content_type': 'application/json',
                      })
        responses.add(**{
                      'method': responses.GET,
                      'url': f'{commons.EZTV_URL}{imdb_id}&page=2',
                      'json': commons.JSON_EZTV_PAGE2,
                      'status': 200,
                      'content_type': 'application/json',
                      })
        responses.add(**{
                      'method': responses.GET,
                      'url': f'{commons.EZTV_URL}{imdb_id}&page=3',
                      'json': commons.JSON_EZTV_PAGE3,
                      'status': 200,
                      'content_type': 'application/json',
                      })
        test_magnet = commons.TEST_MAGNET
        eztv = EZTVTools(imdb_id, '2', '5')
        magnet_url = eztv._get_magnet_url()
        self.assertEqual(test_magnet, magnet_url)
