from datetime import datetime 
import pandas as pd


class Weather:

    def __init__(self) -> None:

        # time parameters
        self.now = datetime.now()
        self.current_time = self.now.strftime("%H:%M")
        self.current_date = self.now.strftime("%d-%m-%Y")
        self.time_file_name = self.now.strftime("%Hh-%Mm")
        self.year = self.now.strftime("%Y")
        self.month = self.now.strftime("%m")

        # directories
        self._export_location = rf"D:\Python\packages\weather_application\csv_files\temperatures_table_cities_{self.current_date} {self.time_file_name} {self.year}{self.month}.csv"
        self.csv_file = pd.read_csv(r"D:\Python\packages\weather_application\cities.csv")
        self.csv_files_location = rf"D:\Python\packages\weather_application\csv_files"
        self.csv_file_name = rf"temperatures_table_cities_{self.current_date} {self.time_file_name} {self.year}{self.month}.csv"
        
        self.__logs_location = rf"D:\Python\packages\weather_application\logs\log_data_chosen_cities_{self.current_date}.log",
        self.copy_log_location = self.__logs_location

        # folder with csv files and extentions
        self.general_csv_files_folder = "D:\\Python\\packages\\weather_application\\csv_files"
        self.current_month_folder = f"{self.csv_files_location}\\{self.year}{self.month}"
        self.csv_extension = "csv"

        # HTML session, populated on each iteration
        self.html_session = None

        # calculating time, populated on each iteration
        self.start = None
        self.end = None

        # sql parameters, populated on each iteration
        self.db = None
        self.mycoursor = None
        self.sql_query = "INSERT INTO weather_app (city, temperature, date, hour, log) VALUES (%s,%s,%s,%s,%s)"
        self.cities_list = []

        # useful objects populated on each iteration
        self.cities_from_csv = []
        self.time_zones = {}
        self.list_to_write = []