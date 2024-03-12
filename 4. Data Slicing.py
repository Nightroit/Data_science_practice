import pandas as pd

# Creating a sample DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emma'],
        'Age': [25, 30, 22, 35, 28],
        'Salary': [50000, 60000, 45000, 70000, 55000],
        'Department': ['HR', 'IT', 'Finance', 'IT', 'Marketing'],
        'Location': ['NY', 'CA', 'NY', 'CA', 'TX']}

df = pd.DataFrame(data)

# Task 1: Select a subset of the DataFrame where the 'Salary' is greater than 50,000, and include only the 'Name' and 'Location' columns in the result.
task_one_result = df.loc[df['Salary'] > 50000, ['Name', 'Location']]

# Task 2: Select rows where the 'Age' is less than 30 and the 'Location' is either 'NY' or 'CA'. Include all columns in the result.
task_two_result = df.loc[(df['Location'].isin(['CA', 'NY'])) & (df['Age'] > 30), ['Name', 'Salary']]

# Task 3:
task_two_result = df.loc[(df['Department'] == 'IT') & (df['Salary'] > 60000), ['Name', 'Age']]
