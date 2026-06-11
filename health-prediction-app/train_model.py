import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

data = pd.read_csv("patient_data.csv")

X = data[['Glucose','Haemoglobin','Cholesterol']]
y = data['Condition']

model = RandomForestClassifier()

model.fit(X,y)

pickle.dump(model,open('model.pkl','wb'))

print("Model Saved")