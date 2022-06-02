yard_sq_m = float(input())
price_m = 7.61
price_yard = yard_sq_m * price_m
discount = price_yard * 0.18
total_price = price_yard - discount
print(total_price)
print(discount)

