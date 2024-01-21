import mysql.connector as sql
import pandas as pd
import time


def database_connection(weather_app_instance, current_time) -> sql.connection:
    """Connects to MySQL database"""

    weather_app_instance.db = sql.connect(
                host = "127.0.0.1",
                port = "3306",
                user = "root",
                database = "weather_database",)
    weather_app_instance.mycoursor = weather_app_instance.db.cursor()

    print(f'\n{current_time.strftime("%H:%M:%S")}h - Connected to database\n')
    print(f"Parameters:\nHost: 127:0.0.1\nPort: 3306\nUser: root\nPassword: *****\nDatabase: weather_database\nTable: weather_app")
    time.sleep(3)

    return weather_app_instance.db

def load_data_in_sql(weather_app_instance, current_time) -> None:
    """Loads the created csv file into the database"""

    print(f"\n{current_time.strftime('%H:%M:%S')}h - Start loading process data in MySQL")

    time.sleep(5)

    cities_df = pd.read_csv(weather_app_instance._export_location)
    for cur_city in cities_df:
        city_list = list(cities_df[cur_city])
        weather_app_instance.cities_list.append(city_list)
    
    for city in weather_app_instance.cities_list[0]:
        splitted_city_info = city.split(";")
        city = splitted_city_info[0]
        if city != "City":
            if splitted_city_info[1].isdigit():
                temperature = int(splitted_city_info[1])
                date = splitted_city_info[2]
                hour = splitted_city_info[3]
                log = weather_app_instance.current_time
                val = (city, temperature, date, hour, log)
                weather_app_instance.mycoursor.execute(weather_app_instance.sql_query, val)
                weather_app_instance.db.commit()

    print(f"\n{current_time.strftime('%H:%M:%S')}h - The data from csv file is loaded in the databse 'weather_database', table 'weather_app'")

# not used
def execute_query(weather_app_instance) -> None:
    """Executes a query to MySQL"""

    sql_query = "select * from weather_database.weather_app"
    weather_app_instance.mycoursor.execute(sql_query)
    result_from_query = weather_app_instance.mycoursor.fetchall()

    return result_from_query

### database connection check --->
# connection = database_connection()

# mycoursor = connection.cursor()

# sql_query = "select * from weather_database.cities where city = 'Miami'"

# mycoursor.execute(sql_query)

# result_from_query = mycoursor.fetchall()

# print(result_from_query)



# id int(11) AI PK 
# city varchar(45) 
# temperature int(11) 
# date varchar(45) 
# hour varchar(45) 
# log varchar(45)