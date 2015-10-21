import os
import requests


my_secret_key = os.environ['WU_KEY']


class APIException(Exception):
    '''Raised when request status is not 200'''
    pass


class WUndergroundInfo:
    '''Parent Class for Accessing Weather Underground API'''

    def __init__(self, q_string):
        self.info_type = None
        self.q_string = str(q_string) + ".json"
        self.res = None

    def get_data(self):
        self.full_url = 'http://api.wunderground.com/api/{}/{}/q/{}'.format(
            my_secret_key, self.info_type, self.q_string)
        self.res = None
        self.res = requests.get(self.full_url)

        if self.res.status_code != 200:
            raise APIException('Request did not return 200; '
                               'request limit may have been reached.')
        self.res = self.res.json()


class CurrentConditions(WUndergroundInfo):
    '''Given zipcode, get full city/state and current temp in ˚F and weather'''

    def run(self):
        self.info_type = 'conditions'
        self.get_data()
        city_state = self.res['current_observation'][
            'display_location']['full']
        curr_temp = self.res['current_observation']['temp_f']
        curr_weather = self.res['current_observation']['weather']

        return {'city_state': city_state, 'curr_temp': curr_temp,
                'curr_weather': curr_weather}


class TenDay(WUndergroundInfo):
    '''Given zipcode, gets 10-day forecast'''

    def run(self):
        self.info_type = 'forecast10day'
        self.get_data()
        ret = {}
        for n in range(10):
            day = 'day' + str(n + 1)
            ret[day] = self.res['forecast']['simpleforecast'][
                'forecastday'][n]['date']['weekday_short']
            ret[day + '_high'] = self.res['forecast']['simpleforecast'][
                'forecastday'][n]['high']['fahrenheit']
            ret[day + '_low'] = self.res['forecast']['simpleforecast'][
                'forecastday'][n]['low']['fahrenheit']
            ret[day + '_conditions'] = self.res['forecast']['simpleforecast'][
                'forecastday'][n]['conditions']
        return ret


class SunriseSunset(WUndergroundInfo):
    '''Given zipcode, gets sunrise and sunset times'''

    def run(self):
        self.info_type = 'astronomy'
        self.get_data()
        sunrise_hour = self.res['moon_phase']['sunrise']['hour']
        sunrise_min = self.res['moon_phase']['sunrise']['minute']
        sunset_hour = self.res['moon_phase']['sunset']['hour']
        sunset_min = self.res['moon_phase']['sunset']['minute']
        return {'sunrise_hour': sunrise_hour, 'sunrise_min': sunrise_min,
                'sunset_hour': sunset_hour, 'sunset_min': sunset_min}


class WeatherAlerts(WUndergroundInfo):
    '''Given zipcode, gets weather alerts'''

    def run(self):
        self.info_type = 'alerts'
        self.get_data()
        ret = []
        for n, alert in enumerate(self.res['alerts']):
            ret.append({
                'alert' + str(n + 1): alert.get('description'),
                'alert' + str(n + 1) + '_start': alert.get('date'),
                'alert' + str(n + 1) + '_end': alert.get('expires'),
            })
        return ret


class ActiveHurricanes:
    '''Get all active hurricanes'''

    def run(self):
        self.info_type = 'currenthurricane'
        self.full_url = 'http://api.wunderground.com/api/{}/{}/view.json' \
            .format(my_secret_key, self.info_type)
        self.res = None
        self.res = requests.get(self.full_url)

        if self.res.status_code != 200:
            raise APIException('Request did not return 200; '
                               'request limit may have been reached.')
        self.res = self.res.json()
        ret = []
        for n, hurricane in enumerate(self.res['currenthurricane']):
            if hurricane['Current']['Category'] == "Hurricane":
                ret.append({
                    'hurricane_name': hurricane['stormInfo']['stormName_Nice'],
                    'hurricane_category': hurricane['Current'][
                        'SaffirSimpsonCategory'],
                })
        return ret
