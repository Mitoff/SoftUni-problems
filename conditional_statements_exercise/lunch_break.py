import math
from math import ceil

name_of_serial = str(input())
duration_episode = int(input())
duration_break = int(input())

time_lunch = duration_break / 8
time_rest = duration_break / 4
time_lunch_rest = time_rest + time_lunch
spare_time_for_episode = (duration_break - time_lunch_rest)
spare_time = math.ceil(abs(spare_time_for_episode - duration_episode))

if spare_time_for_episode >= duration_episode:
    print(f'You have enough time to watch {name_of_serial} and left with {spare_time} minutes free time.')

if spare_time_for_episode < duration_episode:
    print(f"You don't have enough time to watch {name_of_serial}, you need {spare_time} more minutes.")