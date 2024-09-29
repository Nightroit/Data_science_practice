import pandas as pd

data = pd.read_excel("./data.xlsx")
rows_length = len(data)
probability = rows_length/data["Months Subscribed"].sum()

print("In every given month, the probability of a customer churning is: ", round(probability, 3))
