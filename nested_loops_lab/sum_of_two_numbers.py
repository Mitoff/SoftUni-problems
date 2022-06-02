start_interval = int(input())
final_interval = int(input())
magic_number = int(input())
combination_counter = 0
condition = False

for num1 in range(start_interval, final_interval + 1):
    for num2 in range(start_interval, final_interval + 1):

        combination_counter += 1

        if num1 + num2 == magic_number:
            print(f"Combination N:{combination_counter} ({num1} + {num2} = {magic_number})")
            condition = True
            break

    if condition:
        break
if not condition:
    print(f"{combination_counter} combinations - neither equals {magic_number}")
