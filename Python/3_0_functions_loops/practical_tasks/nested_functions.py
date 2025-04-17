# Напишите программу, которая:
# Реализует основную функцию calculator(), которая:
# Спрашивает у пользователя два числа.
# Спрашивает операцию (+, , , /).
# Использует вложенные функции для выполнения каждой операции.
# Возвращает результат выбранной операции.
                # Пример работы программы:
# Введите первое число: 10
# Введите второе число: 5
# Выберите операцию (+, -, *, /): *
# Результат: 50

def calculator():
    first_num = int(input("Type first number : "))
    second_num = int(input("Type second number : "))
    operation = input("Type operation (+, -, *, /) : ")

    def add_nums():
        sum_nums = first_num + second_num
        return sum_nums

    def subtraction_nums():
        min_nums = first_num - second_num
        return min_nums

    def multiplication_nums():
        tim_nums = first_num * second_num
        return tim_nums

    def division_nums():
        dev_nums = first_num / second_num
        return dev_nums

    if operation == "+":
        result = add_nums()
    elif operation == "-":
        result = subtraction_nums()
    elif operation == "*":
        result = multiplication_nums()
    elif operation == "/":
        result = division_nums()
    else:
        print("Error")
    print(f"Результат: {result}")


calculator()
