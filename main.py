from functions import weather_print
from functions import weather_json
from functions import weather_txt


def main():

    weather_print.weather_print_terminal()
    weather_json.weather_desc_json()
    weather_txt.weather_desc_txt()

main()