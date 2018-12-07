import datetime
import pytest

from pytest import mark


@mark.unit
def test_limit_row():
    assert True


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

    output_iso_str_start = start.isoformat(timespec='seconds')
    output_iso_str_end = end.isoformat(timespec='seconds')
    td = end - start
    output_hours = timedelta_to_hours(td)

    assert output_iso_str_start == expected_iso_str_start
    assert output_iso_str_end == expected_iso_str_end
    assert output_hours == expected_hours


def timedelta_to_hours(td):
    """convert timedelta to seconds & return hours"""
    days_to_sec = td.days * 86400
    seconds = td.seconds
    total_seconds = days_to_sec + seconds
    return total_seconds//3600


@mark.unit
def test_query_ses():
    assert True


@mark.unit
def test_build_csv_data():
    assert True


@mark.unit
def test_by_date_range():
    assert True


@mark.unit
def test_make_range():
    assert True


@mark.unit
def test_by_plotform():
    assert True


@mark.unit
def test_by_group():
    assert True


@mark.unit
def test_by_appl():
    assert True
