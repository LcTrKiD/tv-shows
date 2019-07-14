import json

from math import ceil

from typing import Optional

from lib.apitool import APITool, APIToolKeyError


class EZTVError(Exception):
    pass


class EZTVTools(object):
    def __init__(self, imdb_id: Optional[int] = None,
                 season: Optional[str] = None,
                 episode: Optional[str] = None,
                 quality: Optional[str] = None):
        self.headers = {'Accept': 'Application/json'}
        self.base_uri = 'https://eztv.io/api'
        self.imdb_id = imdb_id
        self.season = season
        self.episode = episode
        self.quality = quality
        self.api_key = None
        self.apitool = APITool.create(self)

    def _get_torrents(self, page: Optional[int] = None) -> dict:
        path = '/get-torrents'
        if not page:
            params = {'imdb_id': self.imdb_id}
        params = {'imdb_id': self.imdb_id,
                  'page': page}
        response = self.apitool._GET(path, params)
        return response

    def _get_magnet_url(self) -> str:
        ml = []
        seeds = []
        page_limit = 30
        response = self._get_torrents()
        t_count = response['torrents_count']

        for page in range(ceil(t_count/page_limit)):
            page_result = self._get_torrents(page+1)
            for torrent in page_result['torrents']:
                if self.quality:
                    if (torrent['season'] == self.season and
                            torrent['episode'] == self.episode and
                            self.quality in torrent['title']):
                            if not seeds:
                                ml.append(torrent['magnet_url'])
                                seeds.append(torrent['seeds'])
                            if torrent['seeds'] >= seeds[0]:
                                seeds = []
                                ml = []
                                seeds.append(torrent['seeds'])
                                ml.append(torrent['magnet_url'])
                else:
                    if (torrent['season'] == self.season and
                            torrent['episode'] == self.episode):
                            if not seeds:
                                ml.append(torrent['magnet_url'])
                                seeds.append(torrent['seeds'])
                            if torrent['seeds'] >= seeds[0]:
                                seeds = []
                                ml = []
                                seeds.append(torrent['seeds'])
                                ml.append(torrent['magnet_url'])
        return ml[0]
