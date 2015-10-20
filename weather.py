from weather_lib import CurrentConditions, TenDay, SunriseSunset, \
    WeatherAlerts, ActiveHurricanes


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
    output += 'Current weather: {}˚F, {}\n\n'.format(cc['curr_temp'],
                                                      cc['curr_weather'])

    ten_day = TenDay('94101')
    td = ten_day.run()

    output += '10-day Forecast:\n'

    for n in range(1, 11):
        day = 'day' + str(n)
        output += '{}: High {}˚F, Low {}˚F, {}\n'.format(
            td[day], td[day + '_high'], td[day + '_low'],
            td[day + '_conditions'])


    print(output)

if __name__ == "__main__":
    weather()
