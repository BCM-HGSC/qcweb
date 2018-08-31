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

BASE_COLUMNS = ['Lane Barcode',
                'Metaproject',
                'Midpool Library',
                'Library',
                'Collaborator Sample ID',
                'Internal Processing Sample ID',
                'Machine Name',
                'Total MB',
                'Average Coverage',
                'Chimeric rate',
                'Per 10 Coverage Bases',
                'Per 20 Coverage Bases',
                'Ref Genome Path',
                'Result Path',
                'Q20 Bases',
                'VerifyBamid Contamination Rate']

RUN_DATE_COLUMNS = ['Run Start Date',
                    'Run Finished Date',
                    'Analysis Start Date',
                    'Analysis Alignment Stats Finished Date',
                    'Analysis Finished Date']

ADD1_COLUMNS = ['Prefix',
                'Group']

ADD2_COLUMNS = ['Application',
                'Numeric Total MB']

CURRENT_COLUMNS_KEEP = BASE_COLUMNS + ADD1_COLUMNS


class MyData:
    def __init__(self):
        super(MyData, self).__init__()
        self.at = pd.read_pickle('data/2018_at.pickle.gzip')
        self.at_head = self.at.head()
        print('*** loaded the data')


my_data = MyData()
