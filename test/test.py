import unittest

from utility.apiutility import Apiutility
from utility.webutility import Webutility


class Testdata(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(Testdata, self).__init__(*args, **kwargs)
        self.aut = Apiutility()
        self.wut = Webutility()

    def test_data(self):
        data1 = self.aut.get_api_data("zip_code")
        print(data1)
        data2 = self.wut.set_weather_data("kolkata")
        print(data2)
