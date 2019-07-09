import unittest

import requests
import responses

from lib.tmdbtools import TMDBTools
import lib.tests.tmdb.tmdbcommons as tmdb


class TestTMDBTools(unittest.TestCase):
    @responses.activate
    def test_get_tmdb_id(self):
        responses.add(**{
                      'method': responses.GET,
                      'url': tmdb.URL,
                      'json': tmdb.JSON,
                      'status': 200,
                      'content_type': 'application/json',
                      })

        tv_id = [t['id'] for t in tmdb.JSON['results'] if t['name'] == tmdb.TV_SHOW][0]
        print(tv_id)
        tt = TMDBTools(tmdb.API_KEY, tmdb.TV_SHOW)
        tmdb_id = tt._get_tmdb_id()
        self.assertEqual(tv_id, tmdb_id)

if __name__ == '__main__':
    unittest.main()
