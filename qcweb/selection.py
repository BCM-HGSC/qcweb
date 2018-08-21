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


def at_head():
    return my_data.df_at_head


def sub_appl():
    df_ats = my_data.df_at[COLUMNS_TO_KEEP]
    # groupby by Application
    df_appl = df_ats.groupby('Application')
    df_appl2 = (df_appl['Numeric Total MB'].sum()).reset_index()
    df_appl2['Total TB'] = (df_appl2['Numeric Total MB'] / 1_000_000)
    return df_appl2


def sub_group():
    df_ats = my_data.df_at[COLUMNS_TO_KEEP]
    # groupby by Group
    df_grp = df_ats.groupby('Group')
    df_grp2 = (df_grp['Numeric Total MB'].sum()).reset_index()
    df_grp2['Total TB'] = (df_grp2['Numeric Total MB'] / 1_000_000)
    return df_grp2
