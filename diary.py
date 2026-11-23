import json

def load_expenses():
    try:
        with open("expenses.json", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    
def save_expenses(expenses):
    with open("expenses.json", "w", encoding="utf-8") as f:
         json.dump(expenses, f, ensure_ascii=False, indent=2) 

date = input("Введите дату:")
category = input("Введите категорию:")
while  True:
    try:
        amount = float(input("сумму:"))
        break

    except ValueError:
        print("Вы ввели не число!!!")
    

expense = {"дата":date, "категория":category, "сумма":amount}

expenses = load_expenses()
expenses.append(expense)
save_expenses(expenses)
print("Запись Сохранена")