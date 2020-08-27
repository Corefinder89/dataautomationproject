import os

import requests

from utility.commonmethods import Commonmethods
from utility.logger import Logger


class Apiutility:
    def __init__(self):
        self.log = Logger()
        self.cm = Commonmethods()

    # Get api key from the environment
    def get_apikey(self):
        try:
            return os.environ["apikey"]
        except KeyError:
            self.log.log_error("Environment variable not present")

    # Set query parameters for API
    def set_query_params(self, param_type):
        json_obj = self.cm.get_json_data()
        params = {
            "country_code": json_obj.get("location_parameters").get("country_code"),
            "city": json_obj.get("location_parameters").get("city"),
            "latitude": json_obj.get("location_parameters").get("latitude"),
            "longitude": json_obj.get("location_parameters").get("longitude"),
            "city_id": json_obj.get("location_parameters").get("city_id"),
            "zip_code": json_obj.get("location_parameters").get("zip_code")
        }

        # Set query parameter based on co-ordinates
        if param_type == "co-ordinates":
            return {"lat": params.get("latitude"), "lon": params.get("longitude")}

        # Set query parameter based on city_name
        if param_type == "city_name":
            return {"q": params.get("city") + "," + params.get("country_code")}

        # Set query parameter based on city_id
        if param_type == "city_id":
            return {"id": params.get("city_id")}

        # Set query parameter based on zip_code
        if param_type == "zip_code":
            return {"zip": str(params.get("zip_code")) + "," + params.get("country_code")}

    # Get the data from the API
    def get_api_data(self, param_type):
        json_obj = self.cm.get_json_data()

        api_config = {
            "method": json_obj.get("api_config").get("method"),
            "content_type": json_obj.get("api_config").get("content_type"),
            "authorization": json_obj.get("api_config").get("auth_type"),
            "endpoint": json_obj.get("api_config").get("endpoint")
        }

        headers = {api_config.get("authorization"): self.get_apikey()}
        querystring = self.set_query_params(param_type)
        response = requests.request(
            api_config.get("method"), api_config.get("endpoint"), data="", headers=headers, params=querystring
        )

        # Get the response json
        response_json = response.json()

        if response.status_code != 200:
            self.log.log_error(response_json.get("message"))
        else:
            # Set the API data in dictionary
            api_data = {
                "condition": response_json.get("weather")[0].get("description"),
                "wind_speed": response_json.get("wind").get("speed"),
                "humidity": response_json.get("main").get("humidity"),
                "temperature_celsius": self.cm.convert_kelvin_celsius(response_json.get("main").get("temp")),
                "temperature_fahrenheit": self.cm.convert_kelvin_fahrenheit(response_json.get("main").get("temp"))
            }

            return api_data
