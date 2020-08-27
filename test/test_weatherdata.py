from test.test_data import Testdata

import pytest

from utility.webutility import Webutility


class Testweatherdata(Webutility):
    @pytest.mark.parametrize("param_type, city_name", Testdata.data_set)
    def test_weather_condition_data(self, param_type, city_name):
        data1 = super().get_api_data(param_type)
        print(data1)
        data2 = super().set_weather_data(city_name)
        print(data2)
