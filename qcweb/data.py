"""Responsible for loading and holding the metadata that we are showing."""
import glob
import os
import pandas as pd
import pyarrow


RUN_FINISHED_DATE = 'RUN_FINISHED_DATE'

COLS_KEEP = ['LANE_BARCODE',
             'METAPROJECT_NAME',
             'MIDPOOL_LIBRARY',
             'LIBRARY',
             'RUN_FINISHED_DATE',
             'TOTAL_MB',
             'PREFIX',
             'GROUP']


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
                'REFERENCE_GENOME_ID',
                'RESULT_PATH']

STAT_COLUMNS = ['UNIQUE_ALIGNED_MB',
                'R1_PERCENT_ALIGN_PF',
                'R2_PERCENT_ALIGN_PF',
                'AVERAGE_COVERAGE',
                'CHIMERIC_RATE',
                'PER_10_COVERAGE_BASES',
                'PER_20_COVERAGE_BASES',
                'Q20_BASES',
                'VERIFYBAMID_CONTAMINATION_RATE']

RUN_DATE_COLUMNS = ['RUN_START_DATE',
                    'ANALYSIS_START_DATE',
                    'ANALYSIS_ALIGNMENT_STATS_FINISHED_DATE',
                    'ANALYSIS_FINISHED_DATE']

ADD1_COLUMNS = ['Group']

ADD2_COLUMNS = ['Application']

CURRENT_COLUMNS_KEEP = BASE_COLUMNS + ADD1_COLUMNS + ADD2_COLUMNS


class MyData:
    def __init__(self):
        super(MyData, self).__init__()
        print (n_file())
        self.at = pd.read_parquet(n_file())
        self.at_head = self.at.head()
        print('*** loaded the data with length of', len(self.at))


def n_file():
    list_f = glob.glob('data/'+"*.parquet")
    newest = max(list_f, key=os.path.getctime)
    return newest



my_data = MyData()
