bug_reports = [
    "Issue 1 — High",
    "Issue 2 — Low",
    "Issue 3 — Medium",
    "Issue 4 — Critical",
    "Issue 5 — Low",
    "Issue 3 — Medium",
    "Issue 4 — Critical"
]
bug_input = input("Please type priority for search (High, Medium, Critical or Low): ")
for bug in bug_reports[:]:
    if 'Low' in bug_reports:
        print(bug)
    elif 'Medium' in bug_reports:
        print(bug)
    elif 'High' in bug_reports:
        print(bug)
    elif 'Critical' in bug_reports:
        print(bug)
    else:
        print('Issues not found!')
