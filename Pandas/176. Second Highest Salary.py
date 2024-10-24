import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    a = employee['salary'].drop_duplicates().nlargest(2)
    if len(a) >= 2:
        res = a.iloc[1]
    else:
        res = None
    out = pd.DataFrame({'SecondHighestSalary': [res]})
    return out
    