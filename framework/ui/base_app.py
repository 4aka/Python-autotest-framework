from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as expected_condition
from framework import load_env as env

baseUrl = env.get_from_env('BASE_WEB_URL')


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = baseUrl

    def find_element(self, locator, time=10):
        message = f"Can't find element by locator {locator}"
        return (WebDriverWait(self.driver, time)
                .until(expected_condition.presence_of_element_located(locator), message=message))

    def find_elements(self, locator, time=10):
        message = f"Can't find element by locator {locator}"
        return (WebDriverWait(self.driver, time)
                .until(expected_condition.presence_of_all_elements_located(locator), message=message))

    def go_to_site(self):
        return self.driver.get(self.base_url)