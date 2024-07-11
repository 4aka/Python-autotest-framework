from selenium.webdriver.common.by import By
from framework.ui.base_app import BasePage
from selenium.webdriver.support.ui import WebDriverWait


class GoogleSearchLocators:
    SEARCH_FIELD = (By.ID, "APjFqb")
    SEARCH_BUTTON = (By.CLASS_NAME, "gNO89b")
    IMAGES_BUTTON = (By.XPATH, "CA0QAA")
    VIDEO_BUTTON = (By.XPATH, "CBAQAA")
    SHOPPING_BUTTON = (By.XPATH, "CBEQAA")
    NEWS_BUTTON = (By.XPATH, "CA8QAA")
    RESULTS_LISTS = (By.CLASS_NAME, "MjjYud")


class SearchPage(BasePage):

    def enter_word(self, word):
        search_field = self.find_element(GoogleSearchLocators.SEARCH_FIELD)
        search_field.click()
        search_field.send_keys(word)
        return search_field

    def click_on_the_search_button(self):
        self.wait_until_clickable(GoogleSearchLocators.SEARCH_BUTTON, 5)
        return self.find_element(GoogleSearchLocators.SEARCH_BUTTON).click()

    def waiting_for_results_list(self):
        self.wait_until_clickable(GoogleSearchLocators.RESULTS_LISTS, 5)

    def get_results_list(self):
        SearchPage.waiting_for_results_list(self)
        return self.find_elements(GoogleSearchLocators.RESULTS_LISTS)
