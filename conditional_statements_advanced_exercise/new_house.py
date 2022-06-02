type_flowers = input()
count_flowers = int(input())
budget = int(input())
price_flowers = 0
diff = 0

if type_flowers == 'Roses':
    price_flowers = count_flowers * 5
    if count_flowers > 80:
        price_flowers -= price_flowers * 0.10
elif type_flowers == 'Dahlias':
    price_flowers = count_flowers * 3.80
    if count_flowers > 90:
        price_flowers -= price_flowers * 0.15
elif type_flowers == 'Tulips':
    price_flowers = count_flowers * 2.80
    if count_flowers > 80:
        price_flowers -= price_flowers * 0.15
elif type_flowers == 'Narcissus':
    price_flowers = count_flowers * 3.00
    if count_flowers < 120:
        price_flowers += price_flowers * 0.15
elif type_flowers == 'Gladiolus':
    price_flowers = count_flowers * 2.50
    if count_flowers < 80:
        price_flowers += price_flowers * 0.20

diff = abs(price_flowers - budget)
if budget >= price_flowers:
    print(f'Hey, you have a great garden with {count_flowers} {type_flowers} and {diff:.2f} leva left.')
else:
    print(f'Not enough money, you need {diff:.2f} leva more.')


