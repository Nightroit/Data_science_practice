import mysql.connector
import pandas as pd

# Connect to MySQL
connection = mysql.connector.connect(
    user='',
    password='',
    host='',
    database=''
)

cursor = connection.cursor()

query_select = "SELECT * FROM Employee;"
cursor.execute(query_select)

result_set = cursor.fetchall()


column_names = []

for x in cursor.description:
    column_names.append(x[0])
    
dictionary = {}

for column_idx, column_name in enumerate(column_names):
    dictionary[column_name] = []
    
    for row in result_set:
        dictionary[column_name].append(row[column_idx])

print(pd.DataFrame(dictionary))

connection.close()


