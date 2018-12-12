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


ONE_DAY = datetime.timedelta(days=1)
MIDNIGHT = datetime.time.min

test_datetime_data = [
    ('2018-05-07', '2018-05-07', '00:00:00', '00:00:00', '2018-05-07T00:00:00', '2018-05-08T00:00:00', 24),
    ('2018-05-07', '2018-05-08', '00:00:00', '00:00:00', '2018-05-07T00:00:00', '2018-05-09T00:00:00', 48),
    ('2018-05-07', '2018-05-07', '00:00:00', '12:00:00', '2018-05-07T00:00:00', '2018-05-07T12:00:00', 12)
]

@mark.unit
@mark.parametrize("date_str_start, date_str_end, "
                  "time_str_start, time_str_end, "
                  "expected_iso_str_start, expected_iso_str_end, "
                  "expected_hours", test_datetime_data)
def test_datetime_str(date_str_start,
                      date_str_end,
                      time_str_start,
                      time_str_end,
                      expected_iso_str_start,
                      expected_iso_str_end,
                      expected_hours):
    date_start = datetime.datetime.strptime(date_str_start, "%Y-%m-%d").date()
    time_start = datetime.datetime.strptime(time_str_start, '%H:%M:%S').time()
    start = datetime.datetime.combine(date_start, time_start)

    date_end = datetime.datetime.strptime(date_str_end, "%Y-%m-%d").date()
    time_end = datetime.datetime.strptime(time_str_end, '%H:%M:%S').time()
    end = datetime.datetime.combine(date_end, time_end)
    if time_end == MIDNIGHT:
        end += ONE_DAY
        return end
    else:
        return end

    output_iso_str_start = start.isoformat(timespec='seconds')
    output_iso_str_end = end.isoformat(timespec='seconds')
    td = end - start
    output_hours = timedelta_to_hours(td)

    assert output_iso_str_start == expected_iso_str_start
    assert output_iso_str_end == expected_iso_str_end
    assert output_hours == expected_hours
