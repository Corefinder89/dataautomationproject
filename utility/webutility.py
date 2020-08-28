import re

from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.options import Options

from utility.apiutility import Apiutility


class Webutility(Apiutility):

    # Get the data from web
    def get_web_data(self):
        try:
            driver_path = super().set_driver_path()
            chrome_options = Options()
            chrome_options.add_argument("--headless")
            driver = webdriver.Chrome(executable_path=driver_path, options=chrome_options)

            driver.get("https://social.ndtv.com/static/Weather/report/")
            driver.implicitly_wait(5)
            data = driver.execute_script("return weatherJson")
            driver.quit()
            super().log_info("Data fetched from web")
            return data
        except WebDriverException as e:
            super().log_error(e)

    # Set the weather data from the json response
    def set_weather_data(self, city_name):
        try:
            json_data = self.get_web_data()
            if not city_name[0].isupper():
                city_name = city_name.capitalize()
            else:
                pass
            if json_data.get("indian").get(city_name):
                web_data = {
                    "condition": json_data.get("indian").get(city_name).get("condition"),
                    "humidity": self.filter_humidity(json_data.get("indian").get(city_name).get("humidity")),
                    "temperature_celsius": int(json_data.get("indian").get(city_name).get("temp_c")),
                    "temperature_fahrenheit": int(json_data.get("indian").get(city_name).get("temp_f")),
                    "wind_speed": self.filter_windspeed(json_data.get("indian").get(city_name).get("wind_condition"))
                }

                return web_data
        except KeyError:
            super().log_error("JSON key error")

    # get the humidity value from the string
    def filter_humidity(self, humidity_val):
        split_val = humidity_val.split(":")
        return int(split_val[1].replace("%", ""))

    # get the wind speed value from the string
    def filter_windspeed(self, wind_speed_val):
        split_val = wind_speed_val.split(":")
        filtered_val = re.findall(r"\d\.\d+", split_val[1])
        return float(filtered_val[0])
