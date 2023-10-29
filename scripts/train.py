import pickle
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

housing = pd.read_csv(
    "immo_data.csv",
    converters={'geo_plz': str},
)

housing = housing[housing.baseRent>100]
housing = housing[housing.baseRent<2000]

columns_to_drop = ["streetPlain", "scoutId", "picturecount", "livingSpace", "noRooms", "baseRentRange"]
housing = housing[[col for col in housing.columns if col not in columns_to_drop]]

predictors = [col for col in housing.columns \
              if (housing[col].isna().sum()==0 and housing[col].dtype not in ['O', 'bool'])]

housing = housing[predictors]

#split data into training and test sets
X = housing.drop('baseRent', axis=1)
y = housing['baseRent']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestRegressor(max_depth=10, n_estimators=50, random_state=42)

# Train the model
model.fit(X_train, y_train)

pickle.dump(model, open('scripts/model.pkl', 'wb')) 