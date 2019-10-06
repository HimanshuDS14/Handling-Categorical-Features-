import pandas as pd


data = pd.read_csv("50_Startups.csv")
print(data.head(10))

data["State"] = pd.get_dummies(data["State"] , drop_first=True)
print(data)