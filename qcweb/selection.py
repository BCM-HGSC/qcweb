"""Code here is about filtering and aggregating. There should be no plotting
code here."""

import pandas as pd

from .data import my_data, COLS_KEEP, COLUMNS_TO_KEEP


def head():
    """Demonstration of a function that returns a data frame"""
    return my_data.at_head


def sub_demo():
    """Demonstration of a function that returns a data frame"""
    # select number of rows from dataframe
    at_sub = my_data.at.iloc[-1000:, :]
    return at_sub
