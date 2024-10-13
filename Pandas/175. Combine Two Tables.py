import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    combined_df = pd.merge(person, address, on='personId', how='left')
    result_df = combined_df[['firstName', 'lastName', 'city', 'state']]
    return result_df
    