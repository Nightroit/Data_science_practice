from datetime import datetime
import pandas as pd

df = pd.read_csv("./sales_data.csv")
rows = df.itertuples()
rows_length = len(df)
date_format = "%Y-%m-%d"  

# Task 1: Converting Purchase_Date from string to date object.

df['Purchase_Date'] = pd.to_datetime(df['Purchase_Date'], format="%Y-%m-%d %H:%M:%S.%f") 
print(type(df['Purchase_Date'][1]))
