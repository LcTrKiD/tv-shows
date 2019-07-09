import json

from typing import Optional

from lib.apitool import APITool, APIToolKeyError


class TMDBError(Exception):
    pass


class TMDBTools(object):
    def __init__(self, api_key: Optional[str] = None):
        self.headers = {'Content-Type': 'application/json',
                        'Accept': 'application/json',
                        'Connection': 'close'}
        self.base_uri = 'https://api.themoviedb.org'
        self.version = '3'
        self.api_key = api_key
        self.apitool = APITool.create(self)

    def _get_tmdb_id(self, tv_show: str) -> Optional[int]:
        path = '/search/tv'
        params = {'query': tv_show}
        response = self.apitool._GET(path, self.version, params)
        if response['results'] is None:
            return None
        id = [r['id'] for r in response['results']
              if r['name'] == tv_show]
        if id == []:
            raise TMDBError('TV Show not found')
        return id[0]

    def _get_imdb_id(self, id: int) -> Optional[int]:
        path = f'/tv/{id}/external_ids'
        try:
            response = self.apitool._GET(path,
                                         self.version)
        except:
            raise TMDBError('TV ID incorrect')
        if response is None:
            return None
        id = response['imdb_id'].replace('t', '')
        return id
