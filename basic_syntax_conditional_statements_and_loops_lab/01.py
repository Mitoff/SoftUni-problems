floating_point = float(input())

if floating_point == 0:
    print('zero')

if floating_point < 0:
    if abs(floating_point) < 1:
        write = 'small negative'
        print(write)
    elif abs(floating_point) > 1000000:
        write = 'large negative'
        print(write)
    else:
        print('negative')
elif floating_point > 0:
    write = 'positive'
    if floating_point < 1:
        write = "small positive"
        print(write)
    elif floating_point > 1000000:
        write = "large positive"
        print(write)
    else:
        print('positive')
