from pytest import fixture

from selenium import webdriver

"""
Any fixture that was created in conftest becomes accessible anywhere inside
that directory and any directory below it.
"""


@fixture(scope='session')
def chrome_browser():
    browser = webdriver.Chrome()
    # return browser
    yield browser

    # teardown
    print("I am tearing down this.")
