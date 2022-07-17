import json
from datetime import date
from datetime import datetime
from functions import weather_api


def write_to_json_file(path, fileName, data):
    file_path_name_w_ext = './' + path + '/' + fileName + '.json'
    with open(file_path_name_w_ext, 'a') as fp:
        json.dump(data, fp)


def weather_desc_json():
    weather_dict = weather_api.get_weather_description_and_temp()
    today = date.today()
    current_date = today.strftime("%d.%m.%Y")
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    path = "../WarsawForecast"
    filename = 'weather'

    data = {}
    data['Date'] = current_date
    data['Time'] = current_time
    data['Current forecast is '] = weather_dict.get('description')
    data['The minimum temperature is '] = weather_dict.get('temp_min')
    data['The maximum temperature is '] = weather_dict.get('temp_max')
    data['The pressure is '] = weather_dict.get('pressure')

    write_to_json_file(path, filename, data)
