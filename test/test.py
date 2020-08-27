import unittest

from utility.apiutility import Apiutility
from utility.webutility import Webutility


class Testdata(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(Testdata, self).__init__(*args, **kwargs)
        self.aut = Apiutility()
        self.wut = Webutility()

    def test_data(self):
        # print("Hello")
        # data = self.aut.get_api_data("zip_code")
        # print(data)
        data = self.wut.set_weather_data("bengaluru")
        print(data)
