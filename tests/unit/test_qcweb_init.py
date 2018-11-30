import datetime
import time

from pytest import mark

from qcweb import parse_24h_time_str


test_time_data = [
    ('00:00:00', datetime.time(0,0)),
    ('12:00:00', datetime.time(12, 0)),
    ('23:59:59', datetime.time(23, 59, 59))
]


@mark.unit
@mark.parametrize("time_str, expected", test_time_data)
def test_parse_24h_time_str(time_str, expected):
    output = parse_24h_time_str(time_str)
    assert output == expected
