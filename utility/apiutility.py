import json
import os

import requests

from utility.commonmethods import Commonmethods
from utility.logger import Logger


class Apiutility(Logger, Commonmethods):

    # Get api key from the environment
    def get_apikey(self):
        try:
            return os.environ["apikey"]
        except KeyError:
            super().log_error("Environment variable not present")

    # Get the data from the API
    def get_api_data(self, api_param):
        try:
            json_obj = super().get_json_data()

            api_config = {
                "method": json_obj.get("api_config").get("method"),
                "content_type": json_obj.get("api_config").get("content_type"),
                "authorization": json_obj.get("api_config").get("auth_type"),
                "endpoint": json_obj.get("api_config").get("endpoint")
            }

            headers = {api_config.get("authorization"): self.get_apikey()}

            response = requests.request(
                api_config.get("method"),
                api_config.get("endpoint"),
                data="",
                headers=headers,
                params=json.loads(api_param)
            )

            # Get the response json
            response_json = response.json()

            if response_json.get("cod") >= 400:
                super().log_error(response_json.get("message"))
            else:
                # Set the API data in dictionary
                api_data = {
                    "condition": response_json.get("weather")[0].get("description"),
                    "wind_speed": response_json.get("wind").get("speed"),
                    "humidity": response_json.get("main").get("humidity"),
                    "temperature_celsius": super().convert_kelvin_celsius(response_json.get("main").get("temp")),
                    "temperature_fahrenheit": super().convert_kelvin_fahrenheit(response_json.get("main").get("temp"))
                }

                return api_data
        except KeyError:
            super().log_error("JSON key error")
