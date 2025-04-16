# **Задание:**
# Напишите программу, которая:
# 1. Запрашивает у пользователя количество тест-кейсов, выполненных за каждый день недели.
# 2. Выводит:
#     - Общее количество тестов за неделю.
#     - Среднее количество тестов в день.
# 3. Выводит сообщение в зависимости от результата:
#     - Если среднее больше 10: `"Отличная работа!"`.
#     - Иначе: `"Попробуйте улучшить результат."`.
monday = int(input("How many test-cases on Monday? "))
tuesday = int(input("How many test-cases on Tuesday? "))
wednesday = int(input("How many test-cases on Wednesday? "))
thursday = int(input("How many test-cases on Thursday? "))
friday = int(input("How many test-cases on Friday? "))
sum_test_cases = monday + tuesday + wednesday + thursday + friday
daily_average = sum_test_cases // 5
if daily_average > 10:
    print("Well done!")
else:
    print("Try to improve your result")
