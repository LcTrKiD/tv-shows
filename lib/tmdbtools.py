import json

from typing import Optional

from lib.apitool import APITool, APIToolKeyError


class TMDBError(Exception):
    pass

class TMDBTools(object):
    def __init__(self, api_key: str, tv_show: str):
        self.headers = {'Content-Type': 'application/json',
                        'Accept': 'application/json',
                        'Connection': 'close'}
        self.base_uri = 'https://api.themoviedb.org'
        self.path = '/search/tv'
        self.version = '3'
        self.api_key = api_key
        self.tv_show = tv_show
        self.params = {'query': self.tv_show}

    def _get_tmdb_id(self) -> Optional[str]:
        apitool = APITool(self.headers, self.base_uri, self.api_key)
        response = apitool._GET(self.path, self.version, self.params)
        if response['results'] == None:
            return None
        id = [r['id'] for r in response['results'] 
              if r['name'] == self.tv_show]
        if id == []:
            raise TMDBError('TV Show not found')
        return id[0]
