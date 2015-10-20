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

    conditions = CurrentConditions('conditions', '94101.json')
    res = conditions.run()



if __name__ == "__main__":
    weather()
