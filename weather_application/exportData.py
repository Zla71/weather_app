import time

def csv_file_create(weather_app_instance, current_time) -> list:
    """Creates a list of cities which are taken from csv file."""

    town_list = []
    for _ in weather_app_instance.csv_file:
        city_list = list(weather_app_instance.csv_file["City"])

        town_list.append(city_list)
    weather_app_instance.cities_from_csv = sorted(town_list[0])

    print(f'\n{current_time.strftime("%H:%M:%S")}h - Information from CSV file created\n')
    print(f"FINAL CITIES LIST {town_list[0]}")
    time.sleep(5)

    return town_list[0]