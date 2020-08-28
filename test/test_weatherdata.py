from test.test_data import Testdata

import pytest

from utility.webutility import Webutility


class Testweatherdata(Webutility):
    @pytest.mark.parametrize("query_param, city_name", Testdata.data_set)
    def test_weather_condition_data(self, query_param, city_name):
        api_data = super().get_api_data(query_param)
        web_data = super().set_weather_data(city_name)
        diff = {
            "temp_c": abs(api_data.get("temperature_celsius") - web_data.get("temperature_celsius")),
            "temp_f": abs(api_data.get("temperature_fahrenheit") - web_data.get("temperature_fahrenheit")),
            "humidity": abs(api_data.get("humidity") - web_data.get("humidity")),
            "windspeed": abs(round(api_data.get("wind_speed") - web_data.get("wind_speed"), 3))
        }

        results = super().check_variance(diff)
        assert results.get("temp_c"), "Celsius temperature variance is out of bound"
        assert results.get("temp_f"), "Fahrenheit temperature variance is out of bound"
        assert results.get("humidity"), "Humidity variance is out of bound"
        assert results.get("windspeed"), "Windspeed variance is out of bound"
