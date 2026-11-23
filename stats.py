import pandas as pd

df = pd.read_csv("data.csv")
total = df["сумма"].sum()
print(f"Всего: {total}")
by_cat = df.groupby("категория")["сумма"].sum()
report = by_cat.reset_index()
report["доля"] = report["сумма"] / total * 100
report["доля"] = report["доля"].round(1) 
report.to_csv("report.csv", index=False, encoding="utf-8-sig")
print("Отчёт сохранён")