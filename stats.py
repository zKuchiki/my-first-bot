import pandas as pd
import sys
try:
    df = pd.read_csv("data.csv")
except FileNotFoundError:
    print("data.csv не найден.")
    sys.exit()
try:
    total = df["сумма"].sum()
    print(f"Всего: {total}")
    by_cat = df.groupby("категория")["сумма"].sum()
    report = by_cat.reset_index()
    report["доля"] = report["сумма"] / total * 100
    report["доля"] = report["доля"].round(1)
except KeyError as e:
    print(f"колонка не найдена в data.csv: {e}")
    sys.exit()
report.to_csv("report.csv", index=False, encoding="utf-8-sig")
print("Отчёт сохранён")