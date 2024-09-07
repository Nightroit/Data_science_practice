from datetime import datetime
import pandas as pd

df = pd.read_csv("./sales_data.csv")
rows = df.itertuples()
rows_length = len(df)
date_format = "%Y-%m-%d"  

# Task 1: Converting Purchase_Date from string to date object.

for i in range(rows_length):
    date_string =  df['Purchase_Date'][i].split(" ")[0]
    date_obj = datetime.strptime(date_string, date_format).date()
    df['Purchase_Date'][i] = date_obj

