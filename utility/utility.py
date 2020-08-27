import json
import os

import requests

from utility.logger import Logger


class Utility:
    def __init__(self):
        self.log = Logger()

    def get_json_object(self):
        with open("../config.json") as file:
            data = json.load(file)
            return data

    def get_apikey(self):
        try:
            return os.environ["apikey"]
        except KeyError:
            self.log.log_error("Environment variable not present")

    def set_query_params(self, param_type):
        json_obj = self.get_json_object()
        params = {
            "country_code": json_obj.get("location_parameters").get("country_code"),
            "city": json_obj.get("location_parameters").get("city"),
            "latitude": json_obj.get("location_parameters").get("latitude"),
            "longitude": json_obj.get("location_parameters").get("longitude"),
            "city_id": json_obj.get("location_parameters").get("city_id"),
            "zip_code": json_obj.get("location_parameters").get("zip_code")
        }

        if param_type == "co-ordinates":
            return {"lat": params.get("latitude"), "lon": params.get("longitude")}

        if param_type == "city_name":
            return {"q": params.get("city") + "," + params.get("country_code")}

        if param_type == "city_id":
            return {"id": params.get("city_id")}

        if param_type == "zip_code":
            return {"zip": str(params.get("zip_code")) + "," + params.get("country_code")}

    def get_api_data(self, param_type):
        json_obj = self.get_json_object()

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

        response_json = response.json()

        if response.status_code != 200:
            self.log.log_error(response_json.get("message"))
        else:
            return response_json
