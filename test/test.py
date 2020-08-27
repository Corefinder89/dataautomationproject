import unittest

from utility.apiutility import Apiutility


class Testdata(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(Testdata, self).__init__(*args, **kwargs)
        self.ut = Apiutility()

    def test_data(self):
        data = self.ut.get_api_data("zip_code")
        print(data)
