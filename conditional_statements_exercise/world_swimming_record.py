from math import floor

record = float(input())
meters_swimming = float(input())
time_for_meter = float(input())

time_ivan = meters_swimming * time_for_meter
add = floor(meters_swimming / 15) * 12.5
total_time_ivan = time_ivan + add
if total_time_ivan < record:
    print(f'Yes, he succeeded! The new world record is {total_time_ivan:.2f} seconds.')
deff = abs(total_time_ivan - record)
if total_time_ivan >= record:
    print(f'No, he failed! He was {deff:.2f} seconds slower.')