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
print(data)
