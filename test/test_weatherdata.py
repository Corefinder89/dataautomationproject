from test.test_data import Testdata

import pytest

from utility.webutility import Webutility


class Testweatherdata(Webutility):
    @pytest.mark.parametrize("query_param, city_name", Testdata.data_set)
    @pytest.mark.actualtest
    def test_weather_condition_data(self, query_param, city_name):
        api_data = super().get_api_data(query_param)
        web_data = super().get_weatherdata_from_web(city_name)

        # Use dictionary to store differential data
        diff = {
            "temp_c": abs(api_data.get("temperature_celsius") - web_data.get("temperature_celsius")),
            "temp_f": abs(api_data.get("temperature_fahrenheit") - web_data.get("temperature_fahrenheit")),
            "humidity": abs(api_data.get("humidity") - web_data.get("humidity")),
            "windspeed": abs(round(api_data.get("wind_speed") - web_data.get("wind_speed"), 3))
        }

        # Get the variance result data set
        results = super().check_variance(diff)

        # Assertions for results
        assert results.get("temp_c"), "Celsius temperature variance is out of bound"
        super().log_info("Temperature in celsius is within variance range")
        assert results.get("temp_f"), "Fahrenheit temperature variance is out of bound"
        super().log_info("Temperature in fahrenheit is within variance range")
        assert results.get("humidity"), "Humidity variance is out of bound"
        super().log_info("Humidity is within variance range")
        assert results.get("windspeed"), "Windspeed variance is out of bound"
        super().log_info("Windspeed is within variance range")
