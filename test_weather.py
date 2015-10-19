import os
import requests_mock
from weather import CurrentConditions

my_secret_key = os.environ['WU_KEY']


@requests_mock.Mocker()
def test_current_conditions(m):
    fullurl = 'http://api.wunderground.com/api/{}/conditions/q/94101'.format(
        my_secret_key)

    with open('current-sf.json') as curr_conditions:
        m.get(fullurl, text=curr_conditions.read())

    conditions = CurrentConditions('conditions', '94101')
    res = conditions.run()

    assert res['city_state'] == "San Francisco, CA"
    assert res['curr_temp'] == 66.3
    assert res['curr_weather'] == "Partly Cloudy"
