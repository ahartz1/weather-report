import requests_mock
from weather import *


@requests_mock.Mocker()
def test_current_conditions(m):
    with open('current.json') as curr_conditions:
        m.get(fullurl, text=curr_conditions)

        conditions = CurrentConditions('94101')
        res = conditions.run()
        assert res == ('expected')
