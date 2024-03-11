import pandas as pd
from datetime import datetime

original_data = {
    'patient_id': [1, 2, 3, 4, 5],
    'patient_name': ['John Doe', 'Jane Smith', 'Bob Johnson', 'Alice Brown', 'Charlie White'],
    'admission_date': ['2022-01-05', '2022-02-10', '2022-03-15', '2022-04-20', '2022-05-25'],
    'temperature': [98.6, 99.2, 'N/A', 98.5, 100.0],
    'heart_rate': [75, 80, 85, 'N/A', 90],
    'blood_pressure': ['120/80', '130/90', 'N/A', '110/70', '125/85'],
    'diagnosis': ['Fever', 'Common Cold', 'Injury', 'N/A', 'Flu']
}

# Task 1 
data = pd.DataFrame(original_data)
data.replace('N/A', None, inplace=True)
data.dropna(inplace=True)


# Task 2: seperate the systolic and diastolic value from the blood_pressure column.
blood_pressure_systolic = []
blood_pressure_diastolic = []

for values in data['blood_pressure']: 
    blood_pressure_systolic.append(values.split('/')[0])
    blood_pressure_diastolic.append(values.split('/')[1])

del original_data['blood_pressure']
original_data['blood_pressure_systolic'] = blood_pressure_systolic
original_data['blood_pressure_diastolic']  = blood_pressure_diastolic

print(original_data)
    
