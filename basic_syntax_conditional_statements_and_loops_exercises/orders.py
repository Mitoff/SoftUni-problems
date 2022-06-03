number_of_orders = int(input())
total = 0
total_price = 0
for i in range(number_of_orders):

    price_per_capsule = float(input())
    days = int(input())
    capsules_per_day = int(input())

    price = days * price_per_capsule * capsules_per_day
    total_price += price
    total += price

print(f'The price for the coffee is: ${price:.2f}')
print(f'Total: ${total:.2f}')

