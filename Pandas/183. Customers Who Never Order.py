import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    merged = customers.merge(orders, left_on='id', right_on='customerId', how='left')
    mask = merged['customerId'].isna()
    df = merged[mask]
    df = df['name'].rename('Customers')
    return pd.DataFrame(df)
    