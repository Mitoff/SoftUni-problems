from math import floor

age_lilly = int(input())
price_washing_machine = float(input())
price_toy = int(input())

number_of_toys = 0
saved_money = 0

for gosho in range(1, age_lilly + 1):
    if gosho % 2 == 0:
        saved_money += 10 * (gosho/2)
    else:
        number_of_toys += 1

brother_steal = floor(age_lilly / 2)
the_money = (saved_money - brother_steal) + (number_of_toys * price_toy)
diff = abs(the_money - price_washing_machine)

if the_money >= price_washing_machine:
    print(f'Yes! {diff:.2f}')
else:
    print(f'No! {diff:.2f}')

