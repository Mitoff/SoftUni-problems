# NEDOWYRSHENA ZADACHA

month = input()
nights = int(input())

studio_price = 0
apartment_price = 0
studio_day = 0
apartment_day = 0

if month in "May October":
    studio_price = 50
    apartment_price = 65

    if 7 < nights <= 14:
        studio_day = studio_price - (studio_price * 0.05)

    elif nights > 14:
        studio_day = studio_price - (studio_price * 0.30)
        apartment_day = apartment_price - (apartment_price * 0.10)


elif month in "June September":
    studio_price = 75.20
    apartment_price = 68.70

    if nights > 14:
        studio_day = studio_price - (studio_price * 0.20)
        apartment_day = apartment_price - (apartment_price * 0.10)

    elif nights <= 14:
        studio_day = studio_price
        apartment_day = apartment_price


elif month in "July August":
    studio_price = 76
    apartment_price = 77

    if nights > 14:
        apartment_day = apartment_price - (apartment_price * 0.10)


apartment = apartment_day * nights
studio = studio_price * nights

print(f'Apartment: {apartment:.2f} lv.')
print(f'Studio: {studio:.2f} lv.')



