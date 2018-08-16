"""Responsible for loading and holding the metadata that we are showing."""

import pandas as pd


RUN_FINISHED_DATE = 'Run Finished Date'
COLS_KEEP = ['Lane Barcode',
             'Metaproject',
             'Midpool Library',
             'Library',
             'Run Finished Date',
             'Total MB',
             'Prefix',
             'Group']

ADDITIONAL_COLS_KEEP = ['Application',
                        'Numeric Total MB']

COLUMNS_TO_KEEP = COLS_KEEP + ADDITIONAL_COLS_KEEP


class MyData:
    def __init__(self):
        super(MyData, self).__init__()
        # 2018 all time data
        self.at = pd.read_pickle('data/2018_at.pickle.gzip')
        self.at_head = self.at.head()
        # 2007 - 2018 all time data
        self.df_at = pd.read_pickle('data/at.pickle.gzip')
        self.df_at_head = self.df_at.head()
        print('*** loaded the data')


my_data = MyData()
