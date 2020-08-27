from selenium import webdriver

from utility.commonmethods import Commonmethods
from utility.logger import Logger


class Webutility:
    def __init__(self):
        self.cm = Commonmethods()
        self.log = Logger()

    def get_web_data(self):
        driver_path = self.cm.set_driver_path()
        return driver_path
