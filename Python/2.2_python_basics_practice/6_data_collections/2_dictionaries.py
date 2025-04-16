my_dict = {
    "name": "Eduard",
    "age": 34,
    "is_active": True,
    "skills": ["Python", "SQL", "Docker"],
    "location": {"city": "Dublin", "country": "Ireland", "grades": [11, 22, 33, 44]},
    "score": 87.5,
    "verified": False,
    "email": "eduard@example.com",
    "github": "https://github.com/"
}
my_list_dicts = [
    {"name": "Alice", "age": 25, "city": "London"},
    {"name": "Bob", "age": 30, "city": "New York"},
    {"name": "Charlie", "age": 28, "city": "Paris"}
]

# 6_7_add_new_element_in_dict
my_dict['grade'] = 'A'
print(my_dict)

# 6_8_change_element_in_dict
my_dict['grade'] = 'B'
print(my_dict)

# 6_9_remove_element_from_dict
del my_dict['github']
print(my_dict)

# 6_10_access_to_element_by_key
print(f"Name of the student is : {my_dict['name']}")

# 6_11_verify_key_in_dict
if 'grade' in my_dict:
    print(f"Key 'grade' have been found in dict")
else:
    print(f"Key 'grade' is not found in dict")

# 6_12_change_element_in_nested_dict
my_dict['location']['city'] = 'Galway'
print(my_dict)

# 6_13_change_ element_in_list_inside_dict
print(my_dict['location']['grades'][0])
my_dict['location']['grades'][0] = 85
print(my_dict)

# 6_14_change_dict_element_inside_list
print(my_list_dicts[1])
my_list_dicts[1]['age'] = 25
print(my_list_dicts[1])

