cars = ['audi', 10, True, 'mazda', 10.5]
cars.pop(2)

print(cars)
print(len(cars))

cars.reverse()
print(cars)

my_cars = [5, 'BMW']
cars.extend(my_cars)

print(my_cars)


list_1 = [1, 5, 10, 'string']
list_2 = [5, 20, True]
lists = list_1 + list_2
print(lists)

merged_list = list_1.__add__(list_2)
print(merged_list)
