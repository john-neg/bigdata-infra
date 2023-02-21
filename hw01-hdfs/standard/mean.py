import pandas as pd

df = pd.read_csv('../AB_NYC_2019.csv')

price = df["price"]
price = price.dropna()

print("Mean", price.mean())