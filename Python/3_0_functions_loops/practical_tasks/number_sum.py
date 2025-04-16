                # Напишите программу, которая:
# Запрашивает у пользователя число n.
# Выводит все числа от 1 до n в одной строке, разделяя их пробелами.
# Выводит сумму всех чисел от 1 до n.
                # Пример работы программы:
# Введите число: 5
# Числа: 1 2 3 4 5
# Сумма чисел: 15
number = int(input("Type a number: "))
count_numbers = 0
list_numbers = []
for number in range(1, number):
    list_numbers.append(str(number))
    count_numbers += 1
    join_nums = " ".join(list_numbers)
print(f" Numbers: {join_nums}")
print(f" Sum of numbers: {count_numbers}")
