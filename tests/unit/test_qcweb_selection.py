import datetime
import pytest

from pytest import mark


@mark.unit
def test_limit_row():
    assert True




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
