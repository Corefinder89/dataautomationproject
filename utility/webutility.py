from selenium import webdriver
from selenium.common.exceptions import WebDriverException

from utility.commonmethods import Commonmethods
from utility.logger import Logger


class Webutility:
    def __init__(self):
        self.cm = Commonmethods()
        self.log = Logger()

    def get_web_data(self):
        try:
            driver_path = self.cm.set_driver_path()
            driver = webdriver.Chrome(executable_path=driver_path)
            driver.get("https://www.google.com")
        except WebDriverException as e:
            self.log.log_error(e)
