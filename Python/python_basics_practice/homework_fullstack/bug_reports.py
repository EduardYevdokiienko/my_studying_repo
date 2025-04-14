# **Задание:**
# 1. Создайте список из 5 баг-репортов с разными приоритетами:
#     - `"Ошибка 1 — High"`.
#     - `"Ошибка 2 — Low"`.
#     - И так далее.
# 2. Реализуйте следующие функции:
#     - Добавление нового бага.
#     - Удаление бага с низким приоритетом.
#     - Сортировка багов по приоритету.
# **Результат:**
# Программа `bug_reports.py`, которая:
# - Работает со списком багов.
# - Реализует добавление, удаление и сортировку.

bug_reports = [
    "Issue 1 — High",
    "Issue 2 — Low",
    "Issue 3 — Medium",
    "Issue 4 — Critical",
    "Issue 5 — Low"
]
issues_priority = {
    'Low': 0,
    'Medium': 1,
    'High': 2,
    'Critical': 3
}
def add_bug_report(new_bug_report):
    if new_bug_report:
        bug_priority = input(f"Please type priority - Low, Medium, High, Critical : ")
        full_report = f"{new_bug_report} - {bug_priority}"
        bug_reports.append(full_report)
        print(" Thank you!")
    else:
        print("try again!")

issue_input = input("Please type your issue: ")
add_bug_report(issue_input)

print("\nUpdated bug report list:")
print(bug_reports)

def remove_low_issue():
    for bug in bug_reports[:]:
        if 'Low' in bug:
            bug_reports.remove(bug)

remove_low_issue()
print(bug_reports)


def sort_issues(issues):
    for priority in issues_priority:
        if priority in issues:
            return issues_priority[priority]
    return 999

sorted_priority = sorted(bug_reports, key=sort_issues)
print(sorted_priority)