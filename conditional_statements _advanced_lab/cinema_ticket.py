day_of_week = input()
price = 0

if day_of_week in ('Monday Tuesday Friday'):
    price = 12

if day_of_week in ('Wednesday Thursday'):
    price = 14

if day_of_week in ('Saturday Sunday'):
    price = 16

print(price)