# **Задание:**
# 1. Создайте словарь с информацией о баге:
#     - ID.
#     - Название.
#     - Статус.
# 2. Измените статус баг-репорта.
# 3. Напишите текстовое объяснение о неизменяемых типах данных (например, `str`, `int`, `tuple`)
# в отдельном файле `data_types.txt`.
bug_dict = {
    'ID': 12345,
    'Description': 'The submit form button on the contact page does not work',
    'Status': 'Opened'
}
bug_dict['Status'] = 'Closed'
print(bug_dict)
