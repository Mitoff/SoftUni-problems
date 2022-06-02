budget = float(input())
actors = int(input())
price_clothes_actor = float(input())

price_all_clothes = price_clothes_actor * actors
decor = budget * 0.10
if actors > 150:
    price_all_clothes -= price_all_clothes * 0.10
decor_and_clothes = decor + price_all_clothes
diff = abs(decor_and_clothes - budget)
if decor_and_clothes > budget:
    print(f'Not enough money!')
    print(f'Wingard needs {diff:.2f} leva more.')

if decor_and_clothes <= budget:
    print(f'Action!')
    print(f'Wingard starts filming with {diff:.2f} leva left.')




