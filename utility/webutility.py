import json

from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.options import Options

from utility.commonmethods import Commonmethods
from utility.logger import Logger


class Webutility:
    def __init__(self):
        self.cm = Commonmethods()
        self.log = Logger()

    def get_web_data(self):
        try:
            driver_path = self.cm.set_driver_path()
            chrome_options = Options()
            chrome_options.add_argument("--headless")
            driver = webdriver.Chrome(executable_path=driver_path, options=chrome_options)

            driver.get("https://social.ndtv.com/static/Weather/report/")
            driver.implicitly_wait(5)
            data = driver.execute_script("return weatherJson")
            driver.quit()

            return json.dumps(data)
        except WebDriverException as e:
            self.log.log_error(e)
