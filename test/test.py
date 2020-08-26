import unittest

from utility.utility import Utility


class Testdata(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(Testdata, self).__init__(*args, **kwargs)
        self.ut = Utility()

    def test_data(self):
        data = self.ut.get_api_data("city_name")
        print(data)
