age = float(input())
gender = input()

if gender == 'f':
    if age >= 16:
        print('Ms.')
    else:
        print('Miss')
elif gender == 'm':
    if age >= 16:
        print('Mr.')
    else:
        print('Master')

