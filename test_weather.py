import os
import requests_mock
from weather_lib import CurrentConditions, TenDay, SunriseSunset, \
    WeatherAlerts, ActiveHurricanes

my_secret_key = os.environ['WU_KEY']


@requests_mock.Mocker()
def test_current_conditions(m):
    fullurl = 'http://api.wunderground.com/api/{}/conditions/q/94101.json' \
        .format(my_secret_key)

    with open('json-data/current-sf.json') as data:
        m.get(fullurl, text=data.read())

    conditions = CurrentConditions('94101')
    res = conditions.run()

    assert res['city_state'] == "San Francisco, CA"
    assert res['curr_temp'] == 66.3
    assert res['curr_weather'] == "Partly Cloudy"


@requests_mock.Mocker()
def test_ten_day(m):
    fullurl = 'http://api.wunderground.com/api/{}/forecast10day/q/94101.json' \
        .format(my_secret_key)

    with open('json-data/ten-day.json') as data:
        m.get(fullurl, text=data.read())

    ten_day = TenDay('94101')
    res = ten_day.run()

    assert res['day1'] == "Tue"
    assert res['day1_high'] == "75"
    assert res['day1_low'] == "55"
    assert res['day1_conditions'] == "Partly Cloudy"
    assert res['day2'] == "Wed"
    assert res['day2_high'] == "72"
    assert res['day2_low'] == "55"
    assert res['day2_conditions'] == "Partly Cloudy"
    assert res['day3_high'] == "70"
    assert res['day3_low'] == "55"
    assert res['day3_conditions'] == "Partly Cloudy"
    assert res['day4_high'] == "72"
    assert res['day4_low'] == "55"
    assert res['day4_conditions'] == "Partly Cloudy"
    assert res['day5_high'] == "73"
    assert res['day5_low'] == "55"
    assert res['day5_conditions'] == "Fog"
    assert res['day6_high'] == "72"
    assert res['day6_low'] == "55"
    assert res['day6_conditions'] == "Fog"
    assert res['day7_high'] == "70"
    assert res['day7_low'] == "55"
    assert res['day7_conditions'] == "Partly Cloudy"
    assert res['day8_high'] == "75"
    assert res['day8_low'] == "59"
    assert res['day8_conditions'] == "Partly Cloudy"
    assert res['day9_high'] == "73"
    assert res['day9_low'] == "59"
    assert res['day9_conditions'] == "Partly Cloudy"
    assert res['day10_high'] == "73"
    assert res['day10_low'] == "57"
    assert res['day10_conditions'] == "Clear"


@requests_mock.Mocker()
def test_sunrise_sunset(m):
    fullurl = 'http://api.wunderground.com/api/{}/astronomy/q/94101.json' \
        .format(my_secret_key)

    with open('json-data/astronomy.json') as data:
        m.get(fullurl, text=data.read())

    sunrise_sunset = SunriseSunset('94101')
    res = sunrise_sunset.run()

    assert res['sunrise_hour'] == "7"
    assert res['sunrise_min'] == "01"
    assert res['sunset_hour'] == "16"
    assert res['sunset_min'] == "56"


@requests_mock.Mocker()
def test_weather_alerts(m):
    fullurl = 'http://api.wunderground.com/api/{}/alerts/q/94101.json'.format(
        my_secret_key)

    with open('json-data/alerts.json') as data:
        m.get(fullurl, text=data.read())

    weather_alerts = WeatherAlerts('94101')
    res = weather_alerts.run()

    assert res[0]['alert1'] == "Heat Advisory"
    assert res[0]['alert1_start'] == "11:14 am CDT on July 3, 2012"
    assert res[0]['alert1_end'] == "7:00 AM CDT on July 07, 2012"


@requests_mock.Mocker()
def test_hurricanes(m):
    fullurl = 'http://api.wunderground.com/api/{}/currenthurricane/view.json' \
        .format(my_secret_key)

    with open('json-data/hurricane.json') as data:
        m.get(fullurl, text=data.read())

    hurricanes = ActiveHurricanes()
    res = hurricanes.run()

    assert res[0]['hurricane_name'] == "Hurricane Daniel"
    assert res[0]['hurricane_category'] == 1
