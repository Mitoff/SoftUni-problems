price_of_excursion = float(input())
puzzles = int(input())
talking_doll = int(input())
teddy_bears = int(input())
minions = int(input())
kid_trucks = int(input())
count_toys = puzzles + talking_doll + teddy_bears + minions + kid_trucks
sum_toys = puzzles * 2.60 + talking_doll * 3 + teddy_bears * 4.10 + minions * 8.20 + kid_trucks * 2


if count_toys >= 50:
    total_price_toys = sum_toys - (sum_toys * 0.25)
else:
    total_price_toys = sum_toys

rent = total_price_toys * 0.10
left_money = abs(price_of_excursion - (total_price_toys - rent))
earned = total_price_toys - rent
if earned >= price_of_excursion:
    print(f'Yes! {left_money:.2f} lv left.')
else:
    print(f'Not enough money! {left_money:.2f} lv needed.')
