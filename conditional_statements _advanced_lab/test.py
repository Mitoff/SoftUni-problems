age = float(input())
gender = input()
student_status = input('Enter your student status Y/N: ')

if gender == 'f':
    if age >= 16:
        print('Ms')
        if student_status == "Y":
            print('Hello SoftUni')
        else:
            print('error')
elif gender == 'm':
    if age >= 16:
        print('Mr')
        if student_status == "Y":
            print('Hello SoftUni')
        else:
            print('error')


# тук се изтренираха три вложени if-а!!!!