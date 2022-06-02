temperature_degrees = int(input())
time_of_the_day = input()
outfit = ''
shoes = ''

if time_of_the_day == "Morning":
    if 10 <= temperature_degrees <= 18:
        outfit = 'Sweatshirt'
        shoes = 'Sneakers'
    elif 18 < temperature_degrees <= 24:
        outfit = 'Shirt'
        shoes = 'Moccasins'
    elif temperature_degrees > 24:
        outfit = 'T-Shirt'
        shoes = 'Sandals'

elif time_of_the_day == "Afternoon":
    if 10 <= temperature_degrees <= 18:
        outfit = 'Shirt'
        shoes = 'Moccasins'
    elif 18 < temperature_degrees <= 24:
        outfit = 'T-Shirt'
        shoes = 'Sandals'
    elif temperature_degrees > 24:
        outfit = 'Swim Suit'
        shoes = 'Barefoot'

elif time_of_the_day == "Evening":
    if 10 <= temperature_degrees <= 18:
        outfit = 'Shirt'
        shoes = 'Moccasins'
    elif 18 < temperature_degrees <= 24:
        outfit = 'Shirt'
        shoes = 'Moccasins'
    elif temperature_degrees > 24:
        outfit = 'Shirt'
        shoes = 'Moccasins'

print(f"It's {temperature_degrees} degrees, get your {outfit} and {shoes}.")