from weather_lib import CurrentConditions, TenDay, SunriseSunset
from weather_lib import WeatherAlerts, ActiveHurricanes


def get_zipcode():
    while True:
        zipcode = input('Please enter a 5-digit zipcode: ').strip()
        if len(zipcode) != 5:
            'Invalid input.'
            continue
        try:
            zipcode = int(zipcode)
            return zipcode
        except:
            'Invalid input.'


def weather():
    zipcode = get_zipcode()

    q_string = str(zipcode) + '.json'

    output = ''

    conditions = CurrentConditions(q_string)
    cc = conditions.run()

    output += '\n\nWeather for {} ({})\n\n'.format(zipcode, cc['city_state'])
    output += 'Current weather: {}˚F, {}\n'.format(cc['curr_temp'],
                                                    cc['curr_weather'])

    sunrise_sunset = SunriseSunset(zipcode)
    ss = sunrise_sunset.run()

    output += 'Sunrise {}:{}, Sunset {}:{}\n\n'.format(
        ss['sunrise_hour'], ss['sunrise_min'],
        ss['sunset_hour'], ss['sunset_min']
    )

    ten_day = TenDay(zipcode)
    td = ten_day.run()

    output += '10-day Forecast:\n'

    for n in range(1, 11):
        day = 'day' + str(n)
        output += '{}: High {}˚F, Low {}˚F, {}\n'.format(
            td[day], td[day + '_high'], td[day + '_low'],
            td[day + '_conditions'])

    weather_alerts = WeatherAlerts(zipcode)
    we_al = weather_alerts.run()

    if len(we_al) > 0:
        output += '\n\nAlerts:\n'
        for n, alert in enumerate(we_al):
            a = 'alert' + str(n + 1)
            output += '{}\nIssued: {}\nExpires: {}\n'.format(
                alert[0][a], alert[a + '_start'], alert[a + '_end']
            )



    hurricanes = ActiveHurricanes()
    hur = hurricanes.run()

    if len(hur) > 0:
        output += '\n\nCurrent Hurricanes:\n'
        for n in range(len(hur)):
            output += 'Storm: {}, Category: {}\n'.format(
                hur[n]['hurricane_name'], hur[n]['hurricane_category']
            )


    print(output)

if __name__ == "__main__":
    weather()
