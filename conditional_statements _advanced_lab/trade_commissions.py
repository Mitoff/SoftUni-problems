town = input()
the_sales = float(input())
commission = 0
valid = True

if town == "Sofia":
    if 0<= the_sales <= 500:
        commission = the_sales * 0.05
    elif 500<= the_sales <= 1000:
        commission = the_sales * 0.07
    elif 1000 <= the_sales <= 10000:
        commission = the_sales * 0.08
    elif the_sales > 10000:
        commission = the_sales * 0.12
    else:
        print('error')
        valid = False

elif town == "Varna":
    if 0<= the_sales <= 500:
        commission = the_sales * 0.045
    elif 500<= the_sales <= 1000:
        commission = the_sales * 0.075
    elif 1000 <= the_sales <= 10000:
        commission = the_sales * 0.10
    elif the_sales > 10000:
        commission = the_sales * 0.13
    else:
        print('error')
        valid = False

elif town == "Plovdiv":
    if 0<= the_sales <= 500:
        commission = the_sales * 0.055
    elif 500<= the_sales <= 1000:
        commission = the_sales * 0.08
    elif 1000 <= the_sales <= 10000:
        commission = the_sales * 0.12
    elif the_sales > 10000:
        commission = the_sales * 0.145
    else:
        print('error')
        valid = False
else:
    print('error')
    valid = False

if valid:
    print(f'{commission:.2f}')
