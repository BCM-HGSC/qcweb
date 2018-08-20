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


class MyData:
    def __init__(self):
        super(MyData, self).__init__()
        self.at = pd.read_pickle('data/2018_at.pickle.gzip')
        self.at_head = self.at.head()
        print('*** loaded the data')


my_data = MyData()
