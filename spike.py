import requests
import tmdbsimple as tmdb
from requests_html import HTMLSession


def eztv_general(limit=10, page=1):
    url = 'https://eztv.io/api/get-torrents?'
    api_call = f'{url}limit={limit}&page={page}'
    headers = {"Accept": "Application/json"}
    try:
        request = requests.get(api_call,
                               headers=headers,
                               timeout=30)
        json = request.json()
        return json
    except requests.exceptions.RequestException as e:
        print(f'Get request failed with {e}')


def eztv_imdb(imdb_id, page=1):
    url = 'https://eztv.io/api/get-torrents?'
    api_call = f'{url}imdb_id={imdb_id}&page={page}'
    headers = {"Accept": "Application/json"}
    try:
        request = requests.get(api_call,
                               headers=headers,
                               timeout=30)
        json = request.json()
        return json
    except requests.exceptions.RequestException as e:
        print(f'Get request failed with {e}')


def __get_torrent_count(imdb_id):
    return eztv_imdb(imdb_id)['torrents_count']

def __get_magnet_link(eztv_json, season, episode)


def __get_tmdb_id(tv_show):
    tmdb.API_KEY = 'ae3d0eb6baf8bffc074dbb90b8f764ba'
    search = tmdb.Search()
    response = search.tv(query=tv_show)
    for s in search.results:
        if s['name'] == tv_show:
            return s['id']


def __get_imdb_id(id):
    tv_show = tmdb.TV(id)
    response = tv_show.external_ids()
    return response['imdb_id'].replace('t', '')


def __get_show_id(serie):
    session = HTMLSession()
    r = session.get('https://www.tusubtitulo.com/series.php')
    ahref = r.html.find('a')
    serie = serie.replace('&', '&amp;') if '&' in serie else serie
    link = [e.links for e in ahref if serie in e.text]
    show_id = [show_id for show_id in link[0]][0].split('show/')[1]
    return show_id


def __get_episode_id(id, season, episode):
    session = HTMLSession()
    url = 'https://www.tusubtitulo.com/'
    request = f'{url}ajax_loadShow.php?show={id}&season={season}'
    r = session.get(request)
