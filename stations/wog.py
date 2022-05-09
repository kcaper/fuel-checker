from typing import List

from requests import session, Response
from stations.station import FillingStation


class WOG(FillingStation):
    WOG_API_URL = 'https://api.wog.ua/fuel_stations'

    def __init__(self):
        self.session = session()

    def _get_stations_with_fuel(self, fuel: str) -> List[dict]:
        with self.session as s:
            r = s.get(self.WOG_API_URL, params={'fuels': fuel})

        response = r.json()
        return response['data']['stations']

    def _get_city_stations(self, fuel: str, city: str) -> List[dict]:
        city_name = city.lower()
        stations = self._get_stations_with_fuel(fuel)
        found_city_stations = [s for s in stations if city_name in s.get('city', '').lower()]
        return found_city_stations

    def _fetch_url(self, url: str) -> Response:
        with self.session as s:
            r = s.get(url)
        return r

    @staticmethod
    def _parse(response: Response, fuel: str) -> List[str]:
        description = response.json().get('data', dict()).get('workDescription', '')
        lines = description.split('\n')
        result = list()
        for line in lines:
            if fuel.lower() in line.lower():
                result.append(line)
        return result

    def _check(self, fuel: str, city: str) -> str:
        info = list()
        for s in self._get_city_stations(fuel, city):
            url = s['link']
            resp = self._fetch_url(url)
            if resp.status_code == 200:
                name = s['name']
                station_info = ';\n'.join(self._parse(resp, fuel))
                info.append(f'{name}:\n{station_info}')
            else:
                print(f'{resp} {resp.reason} {resp.json()}')

        return ';\n'.join(info)

    def check(self, fuel: str, city: str) -> str:
        return self._check(fuel, city)
