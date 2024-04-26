# data_loader.py
import pandas as pd

def load_data(filepath):
    data = pd.read_csv(filepath)
    data['birth_date'] = pd.to_datetime(data['birth_date'])
    data.fillna({'value_euro': 0, 'wage_euro': 0, 'release_clause_euro': 0,
                 'national_team': 'Not Applicable', 'national_rating': 0,
                 'national_team_position': 'Not Applicable', 'national_jersey_number': 0}, inplace=True)
    return data
