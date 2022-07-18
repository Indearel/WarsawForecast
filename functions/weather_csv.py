import csv

from datetime import date
from datetime import datetime
from functions import weather_api


def weather_desc_csv():
    weather_dict = weather_api.get_weather_description_and_temp()
    today = date.today()
    current_date = today.strftime("%d.%m.%Y")
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

    today_date = 'Today is: ' + current_date + ' '
    today_forecast = ' Forecast is:' + weather_dict.get('description') + '. '
    today_min_temp = ' The minimum temperature is ' + str(weather_dict.get('temp_min')) + ' Celsius degrees. '
    today_max_temp = ' The maximum temperature is ' + str(weather_dict.get('temp_max')) + ' Celsius degrees. '
    today_pressure = ' The pressure is ' + str(weather_dict.get('pressure')) + ' Hectopascals.'
    today_all = [today_date + current_time, today_forecast, today_min_temp, today_max_temp, today_pressure]

    weather_csv = open('weather.csv', 'a', newline='')
    weather_csv_write = csv.writer(weather_csv)
    weather_csv_write.writerow(today_all)