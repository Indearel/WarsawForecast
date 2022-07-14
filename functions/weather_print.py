from datetime import date
from datetime import datetime
from functions import weather_api

def weather_print_terminal():
    weather_dict = weather_api.get_weather_descprition_and_temp()
    today = date.today()
    now = datetime.now()
    current_date = today.strftime("%d.%m.%Y")
    current_time = now.strftime("%H:%M:%S")

    print("Today is:", current_date, current_time)
    print("Today forecast is", weather_dict.get('description'))
    print("The minimum temperature is", weather_dict.get('temp_min'), "Celsius degrees.")
    print("The maximum temperature is", weather_dict.get('temp_max'), "Celsius degrees.")
    print("The pressure is", weather_dict.get('pressure'), "Hectopascals.")