import requests
import json
from datetime import date

def writeToJSONFile(path, fileName, data):
    filePathNameWExt = './' + path + '/' + fileName + '.json'
    with open(filePathNameWExt, 'a') as fp:
        json.dump(data, fp)

def get_weather_descprition_and_temp():
    api_key = "token"
    city = "Warszawa"
    url = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+api_key+"&units=metric"

    request = requests.get(url)
    json = request.json()

    description = json.get("weather")[0].get("description")
    temp_min = json.get("main").get("temp_min")
    temp_max = json.get("main").get("temp_max")
    pressure = json.get("main").get("pressure")

    return{'description': description,
            'temp_min': temp_min,
            'temp_max': temp_max,
            'pressure': pressure}

def main():
    weather_dict = get_weather_descprition_and_temp()
    today = date.today()
    current_date = today.strftime("%d.%m.%Y")

    # Print the results
    print("Today is:", current_date)
    print("Today`s forecast is",  weather_dict.get('description'))
    print("The minimum temperature is", weather_dict.get('temp_min'), "Celcius degrees.")
    print("The maximum temperature is", weather_dict.get('temp_max'), "Celcius degrees.")
    print("The pressure is", weather_dict.get('pressure'), "Hectopascals.")

    path = "./"
    filename = 'weather'

    data = {}
    data['Date'] = str(current_date)
    data['Today`s forecast is '] = weather_dict.get('description')
    data['The minimum temperature is '] = weather_dict.get('temp_min')
    data['The maximum temperature is '] = weather_dict.get('temp_max')
    data['The pressure is '] = weather_dict.get('pressure')

    writeToJSONFile(path, filename, data)

main()