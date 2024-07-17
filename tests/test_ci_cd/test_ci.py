import os


def test_print_browser_name_from_ci():
    browser_name = os.getenv('BROWSER_NAME')
    print(browser_name)
    assert browser_name is not None, "BROWSER_NAME is not set"


def test_print_log_level_from_ci():
    log_level = os.getenv('LOG_LEVEL')
    print(log_level)
    assert log_level is None, "LOG_LEVEL is set"
