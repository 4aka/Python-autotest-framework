from framework.ui.base_app import BasePage
from selenium.webdriver.common.by import By


class GoogleSeacrhLocators:
    SEARCH_FIELD = (By.ID, "APjFqb")
    SEARCH_BUTTON = (By.CLASS_NAME, "gNO89b")
    IMAGES_BUTTON = (By.XPATH, "CA0QAA")
    VIDEO_BUTTON = (By.XPATH, "CBAQAA")
    SHOPPING_BUTTON = (By.XPATH, "CBEQAA")
    NEWS_BUTTON = (By.XPATH, "CA8QAA")


class SearchHelper(BasePage):

    def enter_word(self, word):
        search_field = self.find_element(GoogleSeacrhLocators.SEARCH_FIELD)
        search_field.click()
        search_field.send_keys(word)
        return search_field

    def click_on_the_search_button(self):
        return self.find_element(GoogleSeacrhLocators.SEARCH_BUTTON, time=2).click()

    # def check_navigation_bar(self):
    #     all_list = self.find_elements(GoogleSeacrhLocators.NAVIGATION_BAR, time=2)
    #     nav_bar_menu = [x.text for x in all_list if len(x.text) > 0]
    #     return nav_bar_menu
