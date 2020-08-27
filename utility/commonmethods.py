import json
import sys


class Commonmethods:

    # Get the JSON data
    def get_json_data(self):
        with open("../config.json") as file:
            data = json.load(file)
            return data

    # Convert kelvin temperature to celsius
    # Type casting the temperature data to integer because
    # the web data is in integers
    def convert_kelvin_celsius(self, kelvin_temp):
        return int(kelvin_temp - 273.15)

    # Convert kelvin temperature to fahrenheit
    # Type casting the temperature data to integer because
    # the web data is in integers
    def convert_kelvin_fahrenheit(self, kelvin_temp):
        return int((kelvin_temp - 273.15) * 1.8 + 32)

    # set driver path based on OS
    def set_driver_path(self):
        json_data = self.get_json_data()
        driver_path = ""
        if sys.platform == "darwin":
            driver_path = json_data.get("driver_config").get("chromedriver_for_mac")
        if sys.platform == "linux":
            driver_path = json_data.get("driver_config").get("chromedriver_for_linux")

        return driver_path
