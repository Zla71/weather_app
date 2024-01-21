from weather_application.class_weather import Weather
from weather_application import databaseUtilities
from weather_application import buildingFile
from weather_application import exportData
from weather_application import cleaningUp
from weather_application import timeZones
from weather_application import timing
from datetime import datetime


weather_app = Weather()

print("\n------------Console Output------------\n")

# STARTING TIMER
timing.start_time(weather_app)

# EXPORT DATA FROM CSV
exportData.csv_file_create(weather_app, datetime.now())

# POPULATE TIME ZONES
timeZones.populate_time_zones(weather_app, datetime.now())

# BUILDING THE MAIN CSV FILE WITH ALL DATA
buildingFile.populate_capitals_information(weather_app, datetime.now())
buildingFile.building_file(weather_app, datetime.now())

# DATABASE CONNECTION AND LOADING DATA IN MYSQL
databaseUtilities.database_connection(weather_app, datetime.now())
databaseUtilities.load_data_in_sql(weather_app, datetime.now())

# CLEAN UP FILES, MOVE FILE TO FOLDERS
cleaningUp.move_files_to_folder(weather_app, datetime.now())

# CALCULATING TIME
timing.calculate_total_time(weather_app)

# LOGGING
# TODO TODO TODO

print("SUCCESS\n")