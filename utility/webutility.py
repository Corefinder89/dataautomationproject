import re

from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.options import Options

from utility.commonmethods import Commonmethods
from utility.logger import Logger


class Webutility:
    def __init__(self):
        self.cm = Commonmethods()
        self.log = Logger()

    def get_web_data(self):
        try:
            driver_path = self.cm.set_driver_path()
            chrome_options = Options()
            chrome_options.add_argument("--headless")
            driver = webdriver.Chrome(executable_path=driver_path, options=chrome_options)

            driver.get("https://social.ndtv.com/static/Weather/report/")
            driver.implicitly_wait(5)
            data = driver.execute_script("return weatherJson")
            driver.quit()

            return data
        except WebDriverException as e:
            self.log.log_error(e)

    def set_weather_data(self, city_name):
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

    def filter_humidity(self, humidity_val):
        split_val = humidity_val.split(":")
        return int(split_val[1].replace("%", ""))

    def filter_windspeed(self, wind_speed_val):
        split_val = wind_speed_val.split(":")
        filtered_val = re.findall(r"\d\.\d+", split_val[1])
        return float(filtered_val[0])
