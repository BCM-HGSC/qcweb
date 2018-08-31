"""Code here is about filtering and aggregating. There should be no plotting
code here."""

import pandas as pd

from .data import my_data, COLS_KEEP, RUN_FINISHED_DATE


def head():
    """Demonstration of a function that returns a data frame"""
    return my_data.at_head


def sub_demo():
    """Demonstration of a function that returns a data frame"""
    # select number of rows from dataframe
    at_sub = my_data.at.iloc[-1000:, :]
    return at_sub


def by_date_range(start, end):
    df = my_data.at[COLS_KEEP]
    return df[(df[RUN_FINISHED_DATE]>=start) & (df[RUN_FINISHED_DATE]<=end)].head()


def by_platform(platform):
    dfs = at[CURRENT_COLUMNS_KEEP]
    if platform == 'HiSeq X':
        df_pf = dfs[dfs['Machine Name'].str[:3] == 'E00']
    elif platform == 'HiSeq 2000':
        df_pf = dfs[dfs['Machine Name'].str[:3] == '700']
    elif platform == 'HiSeq 2500':
        df_pf = dfs[dfs['Machine Name'].str[:3] == 'D00']
    elif platform == 'MiSeq':
        df_pf = dfs[(dfs['Machine Name'].str[-3:] == '888') | (dfs['Machine Name'].str[-3:] == '178') ]
    elif platform == 'NovaSeq':
        df_pf = dfs[dfs['Machine Name'].str[:3] == 'A00']
    elif platform == 'GA':
        df_pf = dfs[dfs['Machine Name'].str[:3] == 'EAS']
    # print(len(df_pf))
    return df_pf
