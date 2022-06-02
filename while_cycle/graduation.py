student_name = input()

year = 1
sum = 0
fail = 0

while year <= 12:
    if fail > 1:
        break
    grade = float(input())

    if grade < 4:
        fail += 1
        continue

    sum = sum + grade

    year += 1
if fail > 1:
    print(f'{student_name} has been excluded at {year} grade')
else:
    average_grade = sum / 12
    print(f'{student_name} graduated. Average grade: {average_grade:.2f}')