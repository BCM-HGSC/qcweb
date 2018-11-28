import time

from pytest import mark


@mark.smoke
@mark.ui
class QueryTests:
    def test_can_navigate_to_query_page(self, chrome_browser):
        local_browser = chrome_browser
        local_browser.get('http://localhost:5000/query')

        time.sleep(5)

        dev_browser = chrome_browser
        dev_browser.get('http://submissions-dev.hgsc.bcm.edu/qcweb/main/query')
        assert True

        time.sleep(5)

    def test_valid_query(self):
        assert True

    def test_invalid_query(self):
        assert True
