from time import sleep

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from utility.apiutility import Apiutility


class Webutility(Apiutility):

    # return driver object
    def set_driver(self):
        try:
            driver_path = super().set_driver_path()
            chrome_options = Options()
            # chrome_options.add_argument("--headless")
            chrome_options.add_argument("--no-sandbox")
            driver = webdriver.Chrome(executable_path=driver_path, options=chrome_options)
            return driver
        except WebDriverException as e:
            super().log_error(e)

    # Get the data from web
    def get_weatherdata_from_web(self, city_name):
        if not city_name[0].isupper():
            city_name = city_name.capitalize()
        else:
            pass
        driver_object = self.set_driver()
        driver_object.get(super().get_json_data().get("web_url").get("site"))
        driver_object.implicitly_wait(4)
        sub_menu = self.find_element(driver_object, "id", "h_sub_menu")
        sub_menu.click()
        weather_element = self.find_element(
            driver_object, "link_text",
            super().get_json_data().get("locators").get("weather_link_text")
        )
        weather_element.click()
        data = self.get_location_data(driver_object, city_name)
        driver_object.quit()
        return data

    def get_location_data(self, driver, city_name):
        element = self.find_element(
            driver, "xpath", f"//div[@class='leaflet-pane leaflet-marker-pane']/div/div[@title='{city_name}']"
        )
        condition = super().get_json_data().get("locators").get("condition")
        wind_speed = super().get_json_data().get("locators").get("wind_speed")
        humidity = super().get_json_data().get("locators").get("humidity")
        temp_deg = super().get_json_data().get("locators").get("temp_deg")
        temp_fah = super().get_json_data().get("locators").get("temp_fah")

        try:
            if element:
                super().log_info("Element is present in the map")
                element.click()
                web_data = {
                    "condition": self.find_element(driver, "xpath", condition).text,
                    "humidity": super().filter_humidity(self.find_element(driver, "xpath", humidity).text),
                    "temperature_celsius":
                    super().filter_temperature(self.find_element(driver, "xpath", temp_deg).text),
                    "temperature_fahrenheit":
                    super().filter_temperature(self.find_element(driver, "xpath", temp_fah).text),
                    "wind_speed": super().filter_windspeed(self.find_element(driver, "xpath", wind_speed).text)
                }
                return web_data
            else:
                super().log_info("Selecting location from pin")
                search_box = self.find_element(driver, "id", "searchBox")
                search_box.send_keys(city_name)
                location_chxbox = self.find_element(driver, "id", city_name)
                location_chxbox.click()
        except NoSuchElementException:
            super().log_error("Locator was not found")

    def find_element(self, driver, locator_type, locator):
        try:
            if locator_type == "id":
                return driver.find_element(By.ID, locator)
            if locator_type == "xpath":
                return driver.find_element(By.XPATH, locator)
            if locator_type == "css_selector":
                return driver.find_element(By.CSS_SELECTOR, locator)
            if locator_type == "link_text":
                return driver.find_element(By.LINK_TEXT, locator)
        except NoSuchElementException:
            super().log_error("Locator " + locator + " was not found")
