import unittest

import requests
import responses

from lib.tmdbtools import TMDBTools
import tests.tmdb.tmdbcommons as commons


class TestTMDBTools(unittest.TestCase):
    @responses.activate
    def test_get_tmdb_id(self):
        responses.add(**{
                      'method': responses.GET,
                      'url': commons.TMDB_ID_URL,
                      'json': commons.JSON_TMDBID,
                      'status': 200,
                      'content_type': 'application/json',
                      })

        tv_id = [t['id'] for t in commons.JSON_TMDBID['results']
                 if t['name'] == commons.TV_SHOW][0]
        tmdb = TMDBTools(commons.API_KEY)
        tmdb_id = tmdb._get_tmdb_id(commons.TV_SHOW)
        self.assertEqual(tv_id, tmdb_id)

    @responses.activate
    def test_get_imdb_id(self):
        responses.add(**{
                      'method': responses.GET,
                      'url': commons.EXT_ID_URL,
                      'json': commons.JSON_EXT_ID,
                      'status': 200,
                      'content_type': 'application/json',
                      })

        test_id = commons.JSON_EXT_ID['imdb_id'].replace('t', '')
        tmdb = TMDBTools(commons.API_KEY)
        imdb_id = tmdb._get_imdb_id(commons.TMDB_ID)
        self.assertEqual(test_id, imdb_id)

if __name__ == '__main__':
    unittest.main()
