def calculate(a, b, operator):
    if operator == "+":
        print(f"{a} + {b} = {a + b}")
    # 1 + 2 = 3
    elif operator == "-":
        print(f"{a} - {b} = {a - b}")
    elif operator == "*":
        print(f" {a} * {b} = {a * b}")
    elif operator == "/":
        if b != 0:
            print(f" {a} / {b} = {a / b}")
        else:
            print("Сан нолго болунбойт")
    else:
        print(f" {operator} мындай оператор жок")


a = int(input("Биринчи санды жаз: "))
b = int(input("Экинчи санды жаз: "))
operator = (input("Операторду киргиз + - * / : "))

calculate(a, b, operator)
