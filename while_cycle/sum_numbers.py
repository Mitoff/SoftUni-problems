number = int(input())
sum = 0

while True:
    entered = int(input())
    sum = sum + entered

    if sum >= number:
        print(sum)
        break