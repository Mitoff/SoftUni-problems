l=int(input())
w=int(input())
h=int(input())
percent = float(input())
volume = l*w*h
volume_liters = volume/1000
taken_volume = volume_liters * percent/100

wanted_volume = volume_liters - taken_volume
print(wanted_volume)