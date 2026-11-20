import pandas as pd

df = pd.read_csv("data.csv")
total = df["сумма"].sum()
print(f"Всего: {total}")