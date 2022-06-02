product = input()
day_of_week = input()
quantity = float(input())

if day_of_week in "Monday Tuesday Wednesday Thursday Friday":
    if product == "banana":
        price = 2.5
        total_price = quantity * price
        print(f"{total_price:.2f}")
    elif product == "apple":
        price = 1.2
        total_price = quantity * price
        print(f"{total_price:.2f}")
    elif product == "orange":
        price = 0.85
        total_price = quantity * price
        print(f"{total_price:.2f}")
    elif product == "grapefruit":
        price = 1.45
        total_price = quantity * price
        print(f"{total_price:.2f}")
    elif product == "kiwi":
        price = 2.70
        total_price = quantity * price
        print(f"{total_price:.2f}")
    elif product == "pineapple":
        price = 5.5
        total_price = quantity * price
        print(f"{total_price:.2f}")
    elif product == "grapes":
        price = 3.85
        total_price = quantity * price
        print(f"{total_price:.2f}")
    else:
        print(f"error")

elif day_of_week == "Saturday" or day_of_week == "Sunday":
    if product == "banana":
        price = 2.7
        total_price = quantity * price
        print(f"{total_price:.2f}")
    elif product == "apple":
        price = 1.25
        total_price = quantity * price
        print(f"{total_price:.2f}")
    elif product == "orange":
        price = 0.90
        total_price = quantity * price
        print(f"{total_price:.2f}")
    elif product == "grapefruit":
        price = 1.60
        total_price = quantity * price
        print(f"{total_price:.2f}")
    elif product == "kiwi":
        price = 3
        total_price = quantity * price
        print(f"{total_price:.2f}")
    elif product == "pineapple":
        price = 5.6
        total_price = quantity * price
        print(f"{total_price:.2f}")
    elif product == "grapes":
        price = 4.2
        total_price = quantity * price
        print(f"{total_price:.2f}")
    else:
        print(f"error")
else:
    print(f"error")