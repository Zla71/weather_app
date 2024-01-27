def write_logging(weather_app_instance, text) -> None:
    """Writting log method"""

    my_log = open(weather_app_instance.log_file_path, "a+")
    my_log.write(text)
    my_log.close()