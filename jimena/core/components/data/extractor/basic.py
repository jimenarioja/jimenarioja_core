import pandas as pd

from jimena.core.components.data.extractor.core import DataExtractorCore
from jimena.core.components.tools.generic import ImportTools


class DataExtractorPandas(DataExtractorCore, ImportTools):

    def __init__(self):
        super().__init__()
        if self.module_exists(module_name=pd.__name__):
            self.csv = pd.read_csv
            self.json = pd.read_json


DataExtractorPandas().csv("csv_file.csv")
