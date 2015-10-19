import os
import requests


my_secret_key = os.environ['WU_KEY']


class APIException(Exception):
    '''Raised when request status is not 200'''
    pass


class WUndergroundInfo:
    '''Parent Class for Accessing Weather Underground API'''

    def __init__(self, info_type, q_string):
        self.info_type = info_type
        self.q_string = q_string
        self.res = None

    def get_res(self):
        self.res = None
        self.res = requests.get(
            'http://api.wunderground.com/api/{}/{}/q/{}'.format(
                my_secret_key, self.info_type, self.q_string))

        if self.res.status_code != 200:
            raise APIException('Request did not return 200; '
                               'request limit may have been reached.')
        self.res = self.res.json()


class CurrentConditions(WUndergroundInfo):
    '''Given zipcode, get full city/state and current temp in ˚F and weather'''

    def run(self):
        self.get_res()
        city_state = self.res['current_observation'][
            'display_location']['full']
        curr_temp = self.res['current_observation']['temp_f']
        curr_weather = self.res['current_observation']['weather']

        return {'city_state': city_state, 'curr_temp': curr_temp,
                'curr_weather': curr_weather}


class TenDay(WUndergroundInfo):
    pass


class SunriseSunset(WUndergroundInfo):
    pass


class WeatherAlerts(WUndergroundInfo):
    pass


class ActiveHurricanes(WUndergroundInfo):
    pass
