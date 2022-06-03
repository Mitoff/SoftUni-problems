n = int(input())

for _ in range(n):
    sms = int(input())

    if sms == 88:
        print('Hello')
        continue

    if sms == 86:
        print('How are you?')
        continue

    if sms !=88 and sms !=86 and sms < 88:
        print('GREAT!')

    if sms > 88:
        print('Bye.')
