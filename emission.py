import pandas as pd

class Emission:
    def __init__(self, filename):
        self.filename = filename
        self.df = pd.read_csv(self.filename)
        

    def lookup_emission_factor(col):
        return self.df[self.df['Lookup identifiers']== cols]['CO2e']

