from datetime import date
from functions import weather_api
from functions import weather_json
from functions import weather_txt


def main():
    weather_dict = weather_api.get_weather_descprition_and_temp()
    today = date.today()
    current_date = today.strftime("%d.%m.%Y")

    # Print the results
    print("Today is:", current_date)
    print("Today forecast is", weather_dict.get('description'))
    print("The minimum temperature is", weather_dict.get('temp_min'), "Celsius degrees.")
    print("The maximum temperature is", weather_dict.get('temp_max'), "Celsius degrees.")
    print("The pressure is", weather_dict.get('pressure'), "Hectopascals.")

    weather_json.weather_desc_json()
    weather_txt.weather_desc_txt()

main()