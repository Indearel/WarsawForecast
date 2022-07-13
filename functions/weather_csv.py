import csv

from datetime import date
from functions import weather_api


def weather_desc_csv():
    weather_dict = weather_api.get_weather_descprition_and_temp()
    today = date.today()
    current_date = today.strftime("%d.%m.%Y")

    today_date = 'Today is: ' + current_date + ' '
    today_forecast = 'Today forecast is:' + weather_dict.get('description') + '. '
    today_min_temp = 'The minimum temperature is ' + str(weather_dict.get('temp_min')) + ' Celsius degrees. '
    today_max_temp = 'The maximum temperature is ' + str(weather_dict.get('temp_max')) + ' Celsius degrees. '
    today_pressure = 'The pressure is ' + str(weather_dict.get('pressure')) + ' Hectopascals.'

    weather_csv = open('weather.csv', 'a', newline='')
    weather_csv_write = csv.writer(weather_csv)
    weather_csv_write.writerow([today_date, today_forecast, today_min_temp, today_max_temp, today_pressure])