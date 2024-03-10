import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

np.random.seed(42)

num_employees = 100

employee_ids = range(1, num_employees + 1)

# Generating employee names
employee_names = ['Employee' + str(i) for i in employee_ids]

# Generating departments
departments = np.random.choice(['HR', 'Finance', 'IT', 'Marketing'], num_employees)

# Generating salaries
salaries = np.random.randint(40000, 100000, num_employees)

today = datetime.now()
hire_dates = [today - timedelta(days=np.random.randint(365 * 5)) for _ in range(num_employees)]

office_data = {
    'EmployeeID': employee_ids,
    'EmployeeName': employee_names,
    'Department': departments,
    'Salary': salaries,
    'HireDate': hire_dates
}

office_df = pd.DataFrame(office_data)


# Creating a set for to get the unique columns
st_departments = set() 

for department in office_df['Department']: 
    st_departments.add(department)
    
departments = list(st_departments) 
average_salary = []

for department in departments:
    average_salary.append(office_df.query("Department == " + "'" + department + "'")['Salary'].describe().mean())
    
plt.bar(departments, average_salary, color='skyblue')

# Add labels and title
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Basic Bar Plot')

# Display the plot
plt.show()


