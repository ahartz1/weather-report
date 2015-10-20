import os
import requests_mock
from weather import CurrentConditions, TenDay, SunriseSunset

my_secret_key = os.environ['WU_KEY']


@requests_mock.Mocker()
def test_current_conditions(m):
    fullurl = 'http://api.wunderground.com/api/{}/conditions/q/94101'.format(
        my_secret_key)

    with open('current-sf.json') as data:
        m.get(fullurl, text=data.read())

    conditions = CurrentConditions('conditions', '94101')
    res = conditions.run()

    assert res['city_state'] == "San Francisco, CA"
    assert res['curr_temp'] == 66.3
    assert res['curr_weather'] == "Partly Cloudy"


@requests_mock.Mocker()
def test_ten_day(m):
    fullurl = 'http://api.wunderground.com/api/{}/forecast10day/q/94101' \
        .format(my_secret_key)

    with open('ten-day.json') as data:
        m.get(fullurl, text=data.read())

    ten_day = TenDay('forecast10day', '94101')
    res = ten_day.run()

    assert res['day1_high'] == "75"
    assert res['day1_low'] == "55"
    assert res['day1_conditions'] == "Partly Cloudy"
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
    fullurl = 'http://api.wunderground.com/api/{}/astronomy/q/94101'.format(
        my_secret_key)

    with open('astronomy.json') as data:
        m.get(fullurl, text=data.read())

    sunrise_sunset = SunriseSunset('astronomy', '94101')
    res = sunrise_sunset.run()

    assert res['sunrise_hour'] == "7"
    assert res['sunrise_min'] == "01"
    assert res['sunset_hour'] == "16"
    assert res['sunset_min'] == "56"


#

#

#

#

#

#

#

#

#

#

#

#

#

#

#

#

#
