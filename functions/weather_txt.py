from datetime import date
from functions import weather_api


def weather_desc_txt():
    weather_dict = weather_api.get_weather_descprition_and_temp()
    today = date.today()
    current_date = today.strftime("%d.%m.%Y")

    Today_date = 'Today is: ' + current_date
    Today_forecast = 'Today forecast is:' + weather_dict.get('description')
    Today_minumum_temperature = 'The minimum temperature is ' + str(weather_dict.get('temp_min')) + ' Celsius degrees.'
    Today_maximum_temperature = 'The maximum temperature is ' + str(weather_dict.get('temp_max')) + ' Celsius degrees.'
    Today_pressure = 'The pressure is ' + str(weather_dict.get('pressure')) + ' Hectopascals.'

    Today_weather = Today_date, Today_forecast, Today_minumum_temperature, Today_maximum_temperature, Today_pressure

    f = open("../WarsawForecast/weather.txt", "w")
    f.write(str(Today_weather))
    f.close()