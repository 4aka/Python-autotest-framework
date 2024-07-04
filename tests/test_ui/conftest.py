import pytest
from selenium import webdriver
from envs import load_env as env

browserName = env.get_from_env('BROWSER_NAME')


# https://habr.com/ru/articles/472156/
# https://pypi.org/project/chromedriver-py/
# https://pypi.org/project/get-gecko-driver/

# pip install webdriver-manager


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

    # Steps before tests
    yield driver
    # Steps after tests
    driver.quit()
