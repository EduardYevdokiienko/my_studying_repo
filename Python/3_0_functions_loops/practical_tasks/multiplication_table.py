# Напишите программу, которая выводит таблицу умножения от 1 до 10.
            # Пример работы программы:
#   1  2  3  4  5  6  7  8  9 10
#   2  4  6  8 10 12 14 16 18 20
#   3  6  9 12 15 18 21 24 27 30
#   ...
#  10 20 30 40 50 60 70 80 90 100

for num in range(1, 10):
    for x in range(1, 10):
        print(num, "*", x, "=", num * x)

