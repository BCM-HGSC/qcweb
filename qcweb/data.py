"""Responsible for loading and holding the metadata that we are showing."""

import pandas as pd


RUN_FINISHED_DATE = 'Run Finished Date'

COLS_KEEP = ['LANE_BARCODE',
             'METAPROJECT_NAME',
             'LIBRARY',
             'LIBRARY',
             'RUN_FINISHED_DATE',
             'TOTAL_MB',
             'PREFIX',
             'Group']

BASE_COLUMNS = ['LANE_BARCODE',
                'RUN_NAME',
                'METAPROJECT_NAME',
                'MIDPOOL_LIBRARY',
                'LIBRARY',
                'RUN_FINISHED_DATE',
                'SAMPLE_EXTERNAL_ID',
                'INTERNAL_PROCESSING_SAMPLE_ID',
                'MACHINE_NAME',
                'TOTAL_MB',
                'REFERENCE_PATH_USED_ANALYSIS',
                'RESULT_PATH']
                
STAT_COLUMNS = ['UNIQUE_ALIGNED_MB',
                'R1_PERCENT_ALIGN_PF',
                'R2_PERCENT_ALIGN_PF',
                'AVERAGE_COVERAGE',
                'CHIMERIC_RATE',
                'PER_TEN_COVERAGE_BASES',
                'PER_TWENTY_COVERAGE_BASES',
                'Q20_BASES',
                'VERIFYBAMID_CONTAMINATION_RATE']

RUN_DATE_COLUMNS = ['Run Start Date',
                    'Analysis Start Date',
                    'Analysis Alignment Stats Finished Date',
                    'Analysis Finished Date']

ADD1_COLUMNS = ['Prefix',
                'Group']

ADD2_COLUMNS = ['Application',
                'Numeric Total MB']

CURRENT_COLUMNS_KEEP = BASE_COLUMNS + ADD1_COLUMNS + ADD2_COLUMNS


class MyData:
    def __init__(self):
        super(MyData, self).__init__()
        # self.at = pd.read_pickle('data/2018_at.pickle.gzip')
        #self.at = pd.read_pickle('data/at.pickle.gzip')
        self.at = pd.read_parquet('all_exemp_2018-12-12_ID.1999063.parquet')
        self.at_head = self.at.head()
        print('*** loaded the data with length of', len(self.at))


my_data = MyData()
