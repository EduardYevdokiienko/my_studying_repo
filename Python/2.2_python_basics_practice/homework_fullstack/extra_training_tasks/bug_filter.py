bug_reports = [
    "Issue 1 — High",
    "Issue 2 — Low",
    "Issue 3 — Medium",
    "Issue 4 — Critical",
    "Issue 5 — Low",
    "Issue 6 — Medium",
    "Issue 7 — Critical"
]
found_bugs = []
bug_input = input("Please type priority for search (High, Medium, Critical or Low): ").capitalize()

for bug in bug_reports:
    if bug_input in bug:
        found_bugs.append(bug)
if len(found_bugs) > 0:
    print(f"Found bugs: ")
    for item in found_bugs:
        print(item)
else:
    print("Bugs with the priority are not found!")
