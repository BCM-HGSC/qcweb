import time

from pytest import mark


@mark.skip(reason="demonstration only")
@mark.ui
def test_can_navigate_to_query_page(chrome_browser):
    local_browser = chrome_browser
    local_browser.get('http://localhost:5000/query')

    time.sleep(5)

    dev_browser = chrome_browser
    dev_browser.get('http://submissions-dev.hgsc.bcm.edu/qcweb/main/query')
    assert True

    time.sleep(5)
