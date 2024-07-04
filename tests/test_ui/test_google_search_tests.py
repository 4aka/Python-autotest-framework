from framework.ui.pages.test_google_search_page import SearchHelper


# https://selenium-python.readthedocs.io/

def test_google_search(browser):

    # TODO exclude steps below from the test
    google_page = SearchHelper(browser)
    google_page.go_to_site()

    google_page.enter_word("Automated tests")
    google_page.click_on_the_search_button()
    google_page.waiting_for_results_list()

    elements = google_page.get_results_list()

    assert len(elements) > 1
