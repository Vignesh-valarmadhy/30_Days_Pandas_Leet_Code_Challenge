import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    cust = customers[~customers['id'].isin(orders['customerId'])]
    df = cust[['name']].rename(columns = {'name':'Customers'})
    return df
    