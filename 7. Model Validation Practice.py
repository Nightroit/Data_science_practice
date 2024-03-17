from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
import pandas as pd

def mean_absolute_error(val_y, val_predictions): 
    
    diff_sum = 0
    num = 0
    
    for x in zip(val_y, val_predictions): 
        diff_sum += abs(x[0]-x[1])
        num += 1
    
    return round(diff_sum / num, 2)

melbourne_file_path = './melb_data.csv'
melbourne_data = pd.read_csv(melbourne_file_path) 
melbourne_data = melbourne_data.dropna(axis=0)

melbourne_features = ['Price', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']

Y = melbourne_data.Rooms
X = melbourne_data[melbourne_features]

train_X, val_X, train_y, val_y = train_test_split(X, Y, random_state = 0)

melbourne_model = DecisionTreeRegressor(random_state=1)

melbourne_model.fit(train_X, train_y)

val_predictions = melbourne_model.predict(val_X)


print(mean_absolute_error(val_y, val_predictions))


