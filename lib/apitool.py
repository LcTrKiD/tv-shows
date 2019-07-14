import requests
import json

from typing import Optional


class APIToolKeyError(Exception):
    pass


class APITool(object):
    def __init__(self, headers: dict, base_uri: str,
                 api_key: Optional[str] = None):
        self.headers = headers
        self.base_uri = base_uri
        self.api_key = api_key

    @staticmethod
    def create(self) -> object:
        if self.api_key:
            return APITool(self.headers, self.base_uri, self.api_key)
        return APITool(self.headers, self.base_uri)

    def _get_complete_url(self, path: str) -> str:
        return f'{self.base_uri}{path}'

    def _get_params(self, params: Optional[dict]) -> Optional[dict]:
        if self.api_key:
            api_dict = {'api_key': self.api_key}
            if params:
                params.update(api_dict)
            else:
                params = api_dict
        return params

    def _request(self, method: str, path: str,
                 params: Optional[dict] = None,
                 payload: Optional[dict] = None,
                 headers: Optional[dict] = None) -> dict:
        url = self._get_complete_url(path)
        params = self._get_params(params)

        response = requests.request(
            method, url, params=params,
            data=json.dumps(payload) if payload else payload,
            headers=self.headers)

        response.raise_for_status()
        response.encoding = 'utf-8'
        return response.json()

    def _GET(self, path: str,
             params: Optional[dict] = None) -> dict:
        return self._request('GET', path,
                             params=params)

    def _POST(self, path: str,
              params: Optional[dict] = None,
              payload: dict = None) -> dict:
        return self._request('POST', path,
                             params=params,
                             payload=payload)

    def _DELETE(self, path: str,
                params: Optional[dict] = None,
                payload: dict = None) -> dict:
        return self._request('DELETE', path,
                             params=params,
                             payload=payload)
