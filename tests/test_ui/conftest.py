import pytest
from selenium import webdriver
from env_preferences import global_vars as global_variebles

browserName = global_variebles.BROWSER_NAME


def get_driver():
    if browserName == "CHROME":
        return webdriver.Chrome()

    elif browserName == ("FIREFOX" or "MOZILLA"):
        return webdriver.Firefox()

    elif browserName == "SAFARI":
        return webdriver.Safari()


@pytest.fixture(scope="session")
def browser():
    driver = get_driver()

    driver.maximize_window()
    driver.implicitly_wait(5)

    yield driver

    driver.quit()
