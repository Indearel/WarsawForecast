from functions import weather_print
from functions import weather_json
from functions import weather_txt
from functions import weather_csv


def main():

    weather_print.weather_print_terminal()
    weather_json.weather_desc_json()
    weather_txt.weather_desc_txt()
    weather_csv.weather_desc_csv()

main()