import os.path
import pickle
import pandas as pd

# load the pickled model file
if os.path.isfile("scripts/model.pkl"):
    model = pickle.load(open('scripts/model.pkl', 'rb'))
else:
    model = pickle.load(open('assets/model.pkl', 'rb'))

# create a dataframe with custom values
custom_values = {'noRoomsRange': 3, 'livingSpaceRange': 4}
custom_df = pd.DataFrame(data=custom_values, index=[0])

# predict using the loaded model and custom values
prediction = model.predict(custom_df)

# [809.61110614]
print(prediction)
