import datetime
import time

from pytest import mark

from qcweb import parse_24h_time_str

@mark.skip(reason="demonstration only")
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


    test_time_data = [
        ('00:00:00', datetime.time(0,0)),
        ('12:00:00', datetime.time(12, 0)),
        ('23:59:59', datetime.time(23, 59, 59))
    ]


    @mark.parametrize("time_str, expected", test_time_data)
    def test_parse_24h_time_str(self, time_str, expected):
        output = parse_24h_time_str(time_str)
        assert output == expected
