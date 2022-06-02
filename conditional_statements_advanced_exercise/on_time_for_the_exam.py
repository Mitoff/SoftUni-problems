hour_exam = int(input())
minutes_exam = int(input())
hour_of_arraival = int(input())
minutes_of_arrival = int(input())

time_for_exam = hour_exam * 60 + minutes_exam
time_for_arrival = hour_of_arraival * 60 + minutes_of_arrival

diff=abs(time_for_exam-time_for_arrival)

if time_for_arrival == time_for_exam:
    print("On time")

elif time_for_arrival > time_for_exam:
    print('Late')
    hour = diff // 60
    minutes = diff % 60

    if diff > 59:
        print(f'{hour}:{minutes:02d} hours after the start')
    else:
        print(f'{minutes} minutes after the start')

elif time_for_arrival < time_for_exam:
    if diff <= 30:
        print(f'On time')
        print(f'{diff} minutes before the start')
    else:
        print("Early")
        hour = diff // 60
        minutes = diff % 60
        if diff > 59:
            print(f'{hour}:{minutes:02d} hours before the start')
        else:
            print(f'{minutes} minutes before the start')
