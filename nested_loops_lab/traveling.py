destination = (input())

while destination != 'End':
    price_trip = float(input())

    sum_cur_destination = 0
    while sum_cur_destination < price_trip:
        saved_money = float(input())
        sum_cur_destination += saved_money
    print(f'Going to {destination}!')

    destination = input()