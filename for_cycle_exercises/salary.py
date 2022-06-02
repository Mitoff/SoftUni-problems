open_tabs = int(input())
salary = float(input())
condition = False

for gosho in range(open_tabs):
    current_opened_tab = input()

    if current_opened_tab == "Facebook":
        salary = salary - 150
    elif current_opened_tab == "Instagram":
        salary = salary - 100
    elif current_opened_tab == "Reddit":
        salary = salary - 50

    if salary <= 0:
        condition = True
        break

if not condition:
    print(int(salary))
else:
    print(f'You have lost your salary.')



