"""Responsible for loading and holding the metadata that we are showing."""

import pandas as pd


RUN_FINISHED_DATE = 'RUN_FINISHED_DATE'

COLS_KEEP = ['LANE_BARCODE',
             'METAPROJECT',
             'MIDPOOL_LIBRARY',
             'LIBRARY',
             'RUN_FINISHED_DATE',
             'TOTAL_MB',
             'Group']

BASE_COLUMNS = ['LANE_BARCODE',
                'RUN_NAME',
                'METAPROJECT',
                'MIDPOOL_LIBRARY',
                'LIBRARY',
                'RUN_FINISHED_DATE',
                'SAMPLE_EXTERNAL_ID',
                'INTERNAL_PROCESSING_SAMPLE_ID',
                'MACHINE_NAME',
                'TOTAL_MB',
                'REFERENCEGENOME_PATH',
                'RESULT_PATH']

STAT_COLUMNS = ['Unique Aligned MB',
                '% Align Read 1',
                '% Align Read 2',
                'Average Coverage',
                'Chimeric rate',
                'Per 10 Coverage Bases',
                'Per 20 Coverage Bases',
                'Q20 Bases',
                'VerifyBamid Contamination Rate']

RUN_DATE_COLUMNS = ['RUN_START_DATE',
                    'ANALYSIS_START_DATE',
                    'ANALYSIS_ALIGNMENT_STATS_FINISHED_DATE',
                    'ANALYSIS_FINISHED_DATE']

ADD1_COLUMNS = ['Group']

ADD2_COLUMNS = ['Application',
                'TOTAL_MB']

CURRENT_COLUMNS_KEEP = BASE_COLUMNS + ADD1_COLUMNS + ADD2_COLUMNS


class MyData:
    def __init__(self):
        super(MyData, self).__init__()
        self.at = pd.read_parquet('data/all_2019-01-30_ID.2026876.parquet')
        self.at_head = self.at.head()
        self.grp = pd.read_pickle('data/grp.pickle.gzip')
        self.appl = pd.read_pickle('data/appl.pickle.gzip')
        print('*** loaded the data with length of', len(self.at))


my_data = MyData()
