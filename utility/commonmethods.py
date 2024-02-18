import json
import re
import sys


class Commonmethods:

    # Get the JSON data
    def get_json_data(self):
        with open("config.json") as file:
            data = json.load(file)
            return data

    # Convert kelvin temperature to Celsius
    # Type casting the temperature data to integer because
    # the web data is in integers
    def convert_kelvin_celsius(self, kelvin_temp):
        return int(kelvin_temp - 273.15)

    # Convert kelvin temperature to Fahrenheit
    # Type casting the temperature data to integer because
    # the web data is in integers
    def convert_kelvin_fahrenheit(self, kelvin_temp):
        return int((kelvin_temp - 273.15) * 1.8 + 32)

    # set driver path based on platform type (LINUX or MAC)
    def set_driver_path(self):
        json_data = self.get_json_data()
        driver_path = ""
        if sys.platform == "darwin":
            driver_path = json_data.get("driver_config").get("chromedriver_for_mac")
        if sys.platform == "linux":
            driver_path = json_data.get("driver_config").get("chromedriver_for_linux")
        if sys.platform == "win32":
            driver_path = json_data.get("driver_config").get("chromedriver_for_win")

        return driver_path

    # compare for variance measure
    def check_variance(self, variance_data):
        data = self.get_json_data()

        temp_c_variance = range(data.get("variance").get("celsius_lb"), data.get("variance").get("celsius_ub"))
        temp_f_variance = range(data.get("variance").get("fahrenheit_lb"), data.get("variance").get("fahrenheit_ub"))
        humidity_variance = range(data.get("variance").get("humidity_lb"), data.get("variance").get("humidity_ub"))
        windspeed_variance = range(data.get("variance").get("windspeed_lb"), data.get("variance").get("windspeed_ub"))

        variance_output = {
            "temp_c": variance_data.get("temp_c") in temp_c_variance,
            "temp_f": variance_data.get("temp_f") in temp_f_variance,
            "humidity": variance_data.get("humidity") in humidity_variance,
            "windspeed": int(variance_data.get("windspeed")) in windspeed_variance
        }

        return variance_output

    # get the humidity value from the string
    def filter_humidity(self, humidity_val):
        split_val = humidity_val.split(":")
        return int(split_val[1].replace("%", ""))

    # get the wind speed value from the string
    def filter_windspeed(self, wind_speed_val):
        split_val = wind_speed_val.split(":")
        filtered_val = re.findall(r"\d\.\d+", split_val[1])
        return float(filtered_val[0])

    # get the temperature value from string
    def filter_temperature(self, temperature_val):
        temp = temperature_val.split(":")
        return int(temp[1])
