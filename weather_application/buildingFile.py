from weather_application import logging
from requests_html import HTMLSession
from datetime import datetime
import pytz, re, time


def populate_capitals_information(weather_app_instance, current_time) -> list:
    """Populates the list with information which will be written in the csv file."""

    print(f'\n{current_time.strftime("%H:%M:%S")} - Start the process of building csv file\n')
    logging.write_logging(weather_app_instance, f'\n{current_time.strftime("%H:%M:%S")} - Start the process of building csv file\n')

    list_to_write = []

    weather_app_instance.html_session = HTMLSession()

    for current_city in weather_app_instance.cities_from_csv:
        # get url
        url = f"https://www.google.com/search?q=weather+{current_city}"
        # google search for "my user agent"
        user_agent = weather_app_instance.html_session.get(url, headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"})
        try:
            temp = user_agent.html.find("span#wob_tm", first = True).text
        except:
            temp = ""

        continent = weather_app_instance.time_zones[current_city]["Continent"]
        city_code = weather_app_instance.time_zones[current_city]["City"]

        UTC = pytz.utc
        IST = pytz.timezone(f"{continent}/{city_code}")
        date_and_hour_info = datetime.now(IST)

        pattern = r"(\d{4}-\d{2}-\d{2})( )(\d{2}:\d{2})"

        result = re.findall(pattern, str(date_and_hour_info))
        date = result[0][0]
        hour = result[0][2]

        dict_1 = {"City": current_city, "Temperature": temp, "Date": date, "Time": hour, "Log": weather_app_instance.current_time}
        list_to_write.append(dict_1)
        
        time.sleep(2)
    
    weather_app_instance.list_to_write = list_to_write

    return list_to_write


def building_file(weather_app_instance, current_time) -> None:
    """Writes the csv file with taken information."""

    with open(weather_app_instance._export_location, "a+") as file:
        # header used for creating file
        file.write("City;Temperature;Date;Hour;Log\n")
        for info in weather_app_instance.list_to_write:
            file.write(f"{info['City']};{info['Temperature']};{info['Date']};{info['Time']};{info['Log']}\n")

    print(f'{current_time.strftime("%H:%M:%S")} - File is buit\n')
    print(f"File name: {weather_app_instance.csv_file_name}")
    print(f"Location: {weather_app_instance.csv_files_location}, mind that it will be moved during the process")

    logging.write_logging(weather_app_instance, f'\n{current_time.strftime("%H:%M:%S")} - File is buit\n\n')
    logging.write_logging(weather_app_instance, f"File name: {weather_app_instance.csv_file_name}\n")
    logging.write_logging(weather_app_instance, f"Location: {weather_app_instance.csv_files_location}, mind that it will be moved during the process\n\n")
    
    time.sleep(5)