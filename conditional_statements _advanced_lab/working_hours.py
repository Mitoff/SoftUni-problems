hours =  int(input())
day_of_week = input()

if 10 <= hours <= 18 and day_of_week in ('Monday Tuesday Wednesday Thursday Friday Saturday'):
    print('open')
else:
    print('closed')


