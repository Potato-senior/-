print("Калькулятор")
num_1 = int(input("Введите первое число: "))
num_2 = int(input("Введите второе число: "))
print("Сложение +")
print("Вычисление -")
print("Умножение *")
print("Деление //")

operation = input("Выберите операцию: ")
if operation == "+":
    ravno = num_1 + num_2
    print(f"{num_1} + {num_2} = {ravno}")
elif operation == "-":
    ravno = num_1 - num_2
    print(f"{num_1} - {num_2} = {ravno}")
elif operation == "*":
    ravno = num_1 * num_2
    print(f"{num_1} * {num_2} = {ravno}")
elif operation == "//":
    if num_1 != 0:
        ravno = num_1 // num_2
        print(f"{num_1} // {num_2} = {ravno}")
    else:
        print("НА 0 ДЕЛИТЬ НЕЛЬЗЯ!!!!!!!!!!")
else:
    print("Неверное")
