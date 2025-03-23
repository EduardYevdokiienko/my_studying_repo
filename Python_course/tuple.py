my_tuple = (10, 5, 15, 10, 20, 10)

print(my_tuple.count(10))

index_1 = my_tuple.index(10)
index_2 = my_tuple.index(10, index_1 + 1)
index_3 = my_tuple.index(10, index_2 + 1)
print(index_1, index_2, index_3)

my_list = list(my_tuple)
my_list.append(55)
print(my_list)

my_tuple = tuple(my_list)

print(my_tuple)
