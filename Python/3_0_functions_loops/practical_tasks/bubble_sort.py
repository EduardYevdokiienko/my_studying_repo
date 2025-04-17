                # Напишите программу, которая:
# Запрашивает у пользователя список чисел через запятую.
# Реализует функцию bubble_sort(numbers), которая сортирует список чисел методом пузырька.
# Выводит отсортированный список.
                # Пример работы программы:
# Введите числа через запятую: 5, 2, 9, 1, 5, 6
# Отсортированный список: 1, 2, 5, 5, 6, 9

def bubble_sort(numbers):
    sorted_numbers = numbers.split(",")
    sorted_numbers.sort()
    sorted_numbers = ",".join(sorted_numbers)
    print(sorted_numbers)

numbers = input("please input numbers: ")
bubble_sort(numbers)
