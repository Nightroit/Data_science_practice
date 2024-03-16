import random
import pandas as pd
from sklearn.tree import DecisionTreeRegressor

# Number of data points
num_data_points = 1000

# Generate random data
flat_data = {
    'Rooms': [random.randint(1, 5) for _ in range(num_data_points)],
    'Bathroom': [random.randint(1, 4) for _ in range(num_data_points)],
    'Landsize': [random.randint(100, 1000) for _ in range(num_data_points)],
    'Lattitude': [random.uniform(-37.9, -37.7) for _ in range(num_data_points)],
    'Longtitude': [random.uniform(144.9, 145.2) for _ in range(num_data_points)],
    'Price': [random.randint(200000, 1000000) for _ in range(num_data_points)]
}

flat_data_df = pd.DataFrame(flat_data)
flat_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']



Y = flat_data['Price'] 
X = flat_data_df[flat_features]

melbourne_model = DecisionTreeRegressor(random_state = 1)
melbourne_model.fit(X, Y)

Rooms_inp = int(input("Enter the number of rooms: "))
Bathroom_inp = int(input("Enter the number of bathrooms: "))
Landsize = int(input("Enter the Landsize: "))
Lattitude = int(input("Enter Lattitude: "))
Longtitude = int(input("Enter Lattitude: "))

input_data = {
    'Rooms': [Rooms_inp],
    'Bathroom': [Bathroom_inp],
    'Landsize': [Landsize],
    'Lattitude': [Lattitude],
    'Longtitude': [Longtitude]
}

input_data = pd.DataFrame(input_data)
# Create DataFrame
print(melbourne_model.predict(input_data))
# Display the first few rows of the DataFrame
print(flat_data_df)

