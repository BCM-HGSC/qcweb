"""Code here is about filtering and aggregating. There should be no plotting
code here."""

import pandas as pd

from .data import my_data, COLS_KEEP, RUN_FINISHED_DATE, CURRENT_COLUMNS_KEEP


def limit_rows(data, max_rows=20):
    result = data
    if len(data) > max_rows:
        num_last = max_rows // 2
        num_first = max_rows - num_last
        result = pd.concat([data.head(num_first), data.tail(num_last)])
    return result


def query_ses(platform, group, appl, start, end):
    filter_by_date = start and end
    is_filtering = platform or group or appl or filter_by_date
    result_df = my_data.at
    if platform:
        result_df = by_platform(result_df, platform)
    if group:
        result_df = by_group(result_df, group)
    if appl:
        result_df = by_appl(result_df, appl)
    if filter_by_date:
        result_df = by_date_range(result_df, start, end)
    return result_df


# write dataframe to a csv file format
def build_csv_data(data_frame):
    csv_data = data_frame.to_csv(path_or_buf=None,
                                 index=True, encoding='utf-8')
    return csv_data


def head():
    """Demonstration of a function that returns a data frame"""
    return my_data.at_head


def sub_demo():
    """Demonstration of a function that returns a data frame"""
    # select number of rows from dataframe
    at_sub = my_data.at.iloc[-1000:, :]
    return at_sub


def home_grp():
    """A function that returns a data frame"""
    return my_data.grp


def home_appl():
    """A function that returns a data frame"""
    return my_data.appl


def by_date_range(result_df, start, end):
    df = result_df
    # convert to datetime64[ns]
    df['Run Finished Date'] = df['Run Finished Date'].astype('datetime64[ns]')
    return df[(df[RUN_FINISHED_DATE] >= start)
              & (df[RUN_FINISHED_DATE] <= end)]


def by_platform(result_df, platform):
    df_pf = dfs = result_df
    platform = platform
    if platform == 'Any':
        df_pf = dfs
    elif platform == 'HiSeq X':
        df_pf = dfs[dfs['Machine Name'].str[:3] == 'E00']
    elif platform == 'HiSeq 2000':
        df_pf = dfs[dfs['Machine Name'].str[:3] == '700']
    elif platform == 'HiSeq 2500':
        df_pf = dfs[dfs['Machine Name'].str[:3] == 'D00']
    elif platform == 'MiSeq':
        df_pf = dfs[(dfs['Machine Name'].str[-3:] == '888')
                    | (dfs['Machine Name'].str[-3:] == '178')]
    elif platform == 'NovaSeq':
        df_pf = dfs[dfs['Machine Name'].str[:3] == 'A00']
    elif platform == 'GA':
        df_pf = dfs[dfs['Machine Name'].str[:3] == 'EAS']
    # print(len(df_pf))
    return df_pf


# TODO: implement QC group names
# complete list of current QC group names
CURRENT_GROUP_NAMES = '''
    TOPMed
    CCDG
    Complex
    CHARGE
    TEDDY
    Cancer
    Research
    Mendelian
    TCGA
    Metagenomic
    ADSP
    Gabriella
    Comparative
    Other
    Insects
    TG
    H3
    Ruii
    Virology
    BAC
'''.split()


def by_group(result_df, group):
    df_grp = dfs = result_df
    group = group
    if group == 'Any':
        df_grp = dfs
    else:
        df_grp = dfs[dfs['Group'] == group]
    return df_grp


def by_appl(result_df, appl):
    df_appl = dfs = result_df
    appl = appl
    if appl == 'Any':
        df_appl = dfs
    else:
        df_appl = dfs[dfs['Application'] == appl]
    return df_appl
