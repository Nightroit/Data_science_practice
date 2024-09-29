import pandas as pd

data = pd.read_excel("./website_churn.xlsx")
total_users = len(data)  # Get the total number of users before filtering
data = data[data['Converted? (Yes/No)'] == "Yes"]
rows_length = len(data)
churn_rate = rows_length / total_users  # Calculate churn rate
print(f"Churn rate: {churn_rate:.4f}")
avg_visits_before_conversion = data['Page Visits Before Conversion'].mean()
print(f"Average visits before conversion: {avg_visits_before_conversion:.2f}")
