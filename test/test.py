import unittest

from utility.apiutility import Apiutility
from utility.webutility import Webutility


class Testdata(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(Testdata, self).__init__(*args, **kwargs)
        self.aut = Apiutility()
        self.wut = Webutility()

    def test_data(self):
        # data = self.aut.get_api_data("zip_code")
        # print(data)
        path = self.wut.get_web_data()
        print(path)
