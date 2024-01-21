from datetime import datetime
import time

def start_time(weather_app_instance) -> time:
    """Returns the time of the starting process."""

    weather_app_instance.start = time.time()
    print(f'{datetime.now().strftime("%H:%M:%S")}h - Process started')
    time.sleep(2)

    return weather_app_instance.start

def end_time(weather_app_instance) -> time:
    """Returns the time of the end of the process."""

    weather_app_instance.end = time.time()
    print(f'\n{datetime.now().strftime("%H:%M:%S")}h - Process finished')
    time.sleep(2)

    return weather_app_instance.end

def calculate_total_time(weather_app_instance) -> str:
    """Returns total time in format 00:00:00"""

    end_time(weather_app_instance)
    seconds = weather_app_instance.end - weather_app_instance.start
    result = time.strftime("%M:%S", time.gmtime(seconds))

    print(f"\nThe whole process took {result} minutes\n")

    return result