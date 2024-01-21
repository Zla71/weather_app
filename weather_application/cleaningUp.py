import os, shutil, glob

def move_files_to_folder(weather_app_instance, current_time) -> str:
    """Moves csv files to folder from current month"""

    print(f"\n{current_time.strftime('%H:%M:%S')}h - Time for clean up, move csv file to current month folder {weather_app_instance.current_month_folder}")

    os.chdir(weather_app_instance.general_csv_files_folder)
    list_of_files = glob.glob('*.{}'.format(weather_app_instance.csv_extension))
    result = ""
    for file in list_of_files:
        if f"{weather_app_instance.year}{weather_app_instance.month}" in file:
            shutil.move(f"{weather_app_instance.general_csv_files_folder}\{file}", f"{weather_app_instance.current_month_folder}\{file}")
            result = f"\nFile {file} was moved to folder: {weather_app_instance.current_month_folder}"
    
    print(result)

    return result