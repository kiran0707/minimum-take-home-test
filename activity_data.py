import pandas as pd

class Activity_data:
    def __init__(self, filename):
        self.filename = filename
        self.df = pd.read_csv(self.filename)    

    def rename_col_lookup(self, lookup_alias, lookup_emission_field):
        self.df.rename(columns={lookup_alias: lookup_emission_field}, inplace=True) 

