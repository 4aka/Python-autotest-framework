import pytest

from framework.ui.pages.test_google_search_page import SearchPage


@pytest.fixture(scope='function')
def google_page(browser):
    google_page = SearchPage(browser)
    google_page.go_to_site()

    yield google_page

    print("\nTearing down function...\n")


@pytest.mark.ui
def test_google_search(google_page):

    google_page.enter_word("Automated tests")
    google_page.click_on_the_search_button()
    google_page.waiting_for_results_list()

    elements = google_page.get_results_list()

    assert len(elements) > 1
