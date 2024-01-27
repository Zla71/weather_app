from weather_application import logging
import time

def populate_time_zones(weather_app_instance, current_time):
    """Populates the dictionary with time zones"""

    weather_app_instance.time_zones = {"Los Angeles":{"Continent": "America", "City": "Los_Angeles"}, "Monaco": {"Continent": "Europe", "City": "Monaco"},
                "Dubai": {"Continent": "Asia", "City": "Dubai"}, "Alicante": {"Continent": "Europe", "City": "Madrid"},
                "Colombo": {"Continent": "Asia", "City": "Colombo"}, "Santa Cruz de Tenerife": {"Continent": "Europe", "City": "Lisbon"},
                "Volos": {"Continent": "Europe", "City": "Athens"}, "Corfu": {"Continent": "Europe", "City": "Athens"},
                "Zakynthos": {"Continent": "Europe", "City": "Athens"},"Lefkada": {"Continent": "Europe", "City": "Athens"},
                "Hurgada": {"Continent": "Europe", "City": "Athens"},"Bari": {"Continent": "Europe", "City": "Rome"},
                "Capri": {"Continent": "Europe", "City": "Rome"}, "Menorka": {"Continent": "Europe", "City": "Rome"},
                "Mayorka": {"Continent": "Europe", "City": "Rome"}, "Miami": {"Continent": "America", "City": "New_York"},
                "Antalya": {"Continent": "Europe", "City": "Athens"}, "Ponce": {"Continent": "America", "City": "Caracas"},
                "Anchorage": {"Continent": "America", "City": "Anchorage"}, "Nayba": {"Continent": "Asia", "City": "Yakutsk"},
                "Lagos": {"Continent": "Africa", "City": "Niamey"}, "Diabugu": {"Continent": "Africa", "City": "Banjul"},
                "Majunga": {"Continent": "Europe", "City": "Athens"}, "Ipoh": {"Continent": "Asia", "City": "Kuala_Lumpur"},
                "Mount Hagen": {"Continent": "Australia", "City": "Brisbane"}, "Perth": {"Continent": "Australia", "City": "Perth"},
                "Bulawayo": {"Continent": "Africa", "City": "Harare"},}

    print(f'\n{current_time.strftime("%H:%M:%S")} - Time zones populated\n')
    print(f"FINAL MAP TIME ZONES {weather_app_instance.time_zones}")

    logging.write_logging(weather_app_instance, f'\n{current_time.strftime("%H:%M:%S")} - Time zones populated\n\n')
    logging.write_logging(weather_app_instance, f"FINAL MAP TIME ZONES {weather_app_instance.time_zones}\n")
    
    time.sleep(5)

    return weather_app_instance.time_zones
    


